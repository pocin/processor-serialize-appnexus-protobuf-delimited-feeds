"""




Decompress appnexus pixel_feed

Downloads are GZIP [handled by preceeding compressor] compressed files that
contain length-delimited Protocol buffer messages. Each record is a varint
specifying the length of the message, followed by the protobuf message itself.
"""
import logging
import os
import sys
import glob
import csv
import json

from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.json_format import MessageToDict

# from pixel_feed_pb2 import pixel_feed

import importlib

# PIXEL_FEED_HEADER = [f.name for f in pixel_feed.DESCRIPTOR.fields]

def find_all_files(datadir):
    logging.debug("Looking for files in '%s'", datadir)
    for path in glob.iglob(os.path.join(datadir, '**/*.pb'), recursive=True):
        if os.path.isfile(path):
            yield path

def message_class_factory(name):
    """
    Return the message class corresponding to the protouf feed

    This is possible because the protobuff messages are called the same
    as the .proto files

    Args:
        name: the feed name ex: ("pixel_feed", "bid_landscape_feed", ...)
    Returns (google.protobuf.Message):
        the correct protobuf message class to deserialize the proto files


    """
    logging.debug("Looking for '%s' protobuf class", name)
    MessageClass = getattr(importlib.import_module("protobuf_schemas." + name + '_pb2'), name)
    return MessageClass

def header_from_message_class(MessageClass):
    return [f.name for f in MessageClass.DESCRIPTOR.fields]

def _build_outpath_from_inpath(inpath):
    logging.debug("Buliding outpath from %s", inpath)
    infolder, name = os.path.split(inpath)
    outfolder = infolder.replace('/data/in/files', '/data/out/files')
    if not os.path.isdir(outfolder):
        os.makedirs(outfolder)
    basename, _ = os.path.splitext(name)
    outpath = os.path.join(outfolder, basename + '.csv')
    logging.debug("destination is %s", outpath)
    return outpath

def _process_file(inpath, MessageClass):
    """process one protobuf file (which is a size delimited)

    https://www.datadoghq.com/blog/engineering/protobuf-parsing-in-python/
    dummy infile might look like this

    <varint><binary_msg_of_len_varint><varint2><binary_msg_of_len_varint2>

    yields:
        deserialized feed instances as JSON objects
    """

    with open(inpath, 'rb') as f:
        buf = f.read()
        n = 0
        while n < len(buf):
            msg_len, new_pos = _DecodeVarint32(buf, n)
            n = new_pos
            msg_buf = buf[n:n+msg_len]
            n += msg_len
            feed = MessageClass()
            feed.ParseFromString(msg_buf)
            yield MessageToDict(feed, preserving_proto_field_name=True)


def process_file(inpath, outpath, MessageClass, header):

    logging.debug("Processing %s", inpath)
    with open(outpath, 'w') as fout:
        writer = csv.DictWriter(fout, fieldnames=header)
        for feed in _process_file(inpath, MessageClass):
            writer.writerow(feed)
    return outpath

def main(datadir, feed_name):
    FeedMessageClass = message_class_factory(feed_name)
    header = header_from_message_class(FeedMessageClass)
    for inpath in find_all_files(datadir):
        outpath = _build_outpath_from_inpath(inpath)
        process_file(inpath, outpath, FeedMessageClass, header=header)

    logging.debug("Done")


if __name__ == "__main__":
    try:
        if os.getenv("KBC_PARAMETER_DEBUG"):
            logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        else:
            logging.basicConfig(stream=sys.stdout, level=logging.INFO)
        logging.debug("Starting processor")
        feed_name = os.environ["KBC_PARAMETER_FEED_NAME"]
        main('/data/in/files/', feed_name)
    except (ValueError, KeyError) as err:
        logging.exception(err)
        sys.exit(1)
    except:
        logging.exception("Internal error")
        sys.exit(2)

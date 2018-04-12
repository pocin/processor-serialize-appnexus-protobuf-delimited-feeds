"""
Some tests
"""
import os
import logging
import pytest
from shutil import copyfile
import csv
from main import (_build_outpath_from_inpath,
                  find_all_files, process_file,
                  _process_file, main,
                  message_class_factory, header_from_message_class)
from protobuf_schemas.pixel_feed_pb2 import pixel_feed
import logging
logging.basicConfig(level=logging.DEBUG)


THIS_FILE = os.path.dirname(os.path.abspath(__file__))
TEST_INFILE = os.path.join(THIS_FILE, 'data/in/files/example_feed.pb')

def test_building_outpaths():
    tests = [
        ('/data/in/files/something.pb', '/data/out/files/something.csv'),
        ('/data/in/files/nested/deeply/something', '/data/out/files/nested/deeply/something.csv')
    ]
    for inpath, expected in tests:
        assert _build_outpath_from_inpath(inpath) == expected

def test_finding_files():
    files = set(find_all_files(THIS_FILE.rstrip('/')+ '/data'))
    def pj(fname):
        return os.path.join(THIS_FILE, 'data/in/files', fname)
    assert pj('example_feed.pb') in files
    assert pj('shouldnt_be_found') not in files

def test_parsing_file():
    feeds = _process_file(TEST_INFILE, MessageClass=pixel_feed)
    for feed in feeds:
        # is a unix timestamp
        assert isinstance(feed, dict)
        assert int(feed['date_time']) > 10000

def test_processing_file_to_csv(tmpdir):
    out = tmpdir.mkdir('out').join('output.csv')
    header = ["date_time", "auction_id_64", "user_id_64", "pixel_id",
              "order_id", "external_data", "http_referer", "hashed_user_id_64"]
    process_file(TEST_INFILE, out.strpath, pixel_feed, header=header)
    with open(out.strpath) as fout:
        feed = next(csv.DictReader(fout, fieldnames=header))
        assert int(feed['date_time']) > 10000
        assert 'order_id' in feed

def test_importing_message_class_based_on_feed_name():
    pixel_feed = message_class_factory('pixel_feed')
    header = header_from_message_class(pixel_feed)
    assert hasattr(pixel_feed, 'date_time')
    assert 'date_time' in header
    assert len(header) > 5

    std_feed = message_class_factory('standard_feed')
    assert callable(std_feed)

def test_main_machinery(tmpdir):
    datadir = tmpdir.mkdir('data')

    infilesdir = datadir.mkdir('in').mkdir('files')
    feed_inpath = infilesdir.join('example_feed.pb')
    outdir = datadir.mkdir('out').mkdir('files')
    assert os.path.isdir(outdir.strpath)
    outfile = outdir.strpath.rstrip('/') + '/example_feed.csv'

    copyfile(TEST_INFILE, feed_inpath.strpath)

    header = ["date_time", "auction_id_64", "user_id_64", "pixel_id",
              "order_id", "external_data", "http_referer", "hashed_user_id_64"]

    main(infilesdir.strpath, feed_name='pixel_feed')

    with pytest.raises(ImportError) as err:
        main(infilesdir.strpath, feed_name='doesnt_exist')

    with open(outfile) as fout:
        feed = next(csv.DictReader(fout, fieldnames=header))
        assert int(feed['date_time']) > 10000
        assert 'order_id' in feed

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: segment_feed.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='segment_feed.proto',
  package='',
  serialized_pb=_b('\n\x12segment_feed.proto\"\x9f\x01\n\x0csegment_feed\x12\x11\n\tdate_time\x18\x01 \x01(\x06\x12\x12\n\nuser_id_64\x18\x02 \x01(\x06\x12\x11\n\tmember_id\x18\x03 \x01(\x05\x12\x12\n\nsegment_id\x18\x04 \x01(\x05\x12\x17\n\x0fis_daily_unique\x18\x05 \x01(\x05\x12\x19\n\x11is_monthly_unique\x18\x06 \x01(\x05\x12\r\n\x05value\x18\x07 \x01(\x05\x42&\n$com.appnexus.data.protobuf.generated')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SEGMENT_FEED = _descriptor.Descriptor(
  name='segment_feed',
  full_name='segment_feed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date_time', full_name='segment_feed.date_time', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id_64', full_name='segment_feed.user_id_64', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='member_id', full_name='segment_feed.member_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='segment_id', full_name='segment_feed.segment_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_daily_unique', full_name='segment_feed.is_daily_unique', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_monthly_unique', full_name='segment_feed.is_monthly_unique', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='segment_feed.value', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=182,
)

DESCRIPTOR.message_types_by_name['segment_feed'] = _SEGMENT_FEED

segment_feed = _reflection.GeneratedProtocolMessageType('segment_feed', (_message.Message,), dict(
  DESCRIPTOR = _SEGMENT_FEED,
  __module__ = 'segment_feed_pb2'
  # @@protoc_insertion_point(class_scope:segment_feed)
  ))
_sym_db.RegisterMessage(segment_feed)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.appnexus.data.protobuf.generated'))
# @@protoc_insertion_point(module_scope)

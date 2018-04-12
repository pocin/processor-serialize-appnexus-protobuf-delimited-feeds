# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: includes/enums/video_context_enum.proto

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
  name='includes/enums/video_context_enum.proto',
  package='',
  serialized_pb=_b('\n\'includes/enums/video_context_enum.proto\"z\n\x12video_context_enum\"d\n\x0cVideoContext\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PREROLL\x10\x01\x12\x0b\n\x07MIDROLL\x10\x02\x12\x0c\n\x08POSTROLL\x10\x03\x12\r\n\tOUTSTREAM\x10\x04\x12\x10\n\x0c\x42\x41NNERSTREAM\x10\x05\x42,\n*com.appnexus.data.protobuf.generated.enums')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_VIDEO_CONTEXT_ENUM_VIDEOCONTEXT = _descriptor.EnumDescriptor(
  name='VideoContext',
  full_name='video_context_enum.VideoContext',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREROLL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIDROLL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTROLL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUTSTREAM', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANNERSTREAM', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=65,
  serialized_end=165,
)
_sym_db.RegisterEnumDescriptor(_VIDEO_CONTEXT_ENUM_VIDEOCONTEXT)


_VIDEO_CONTEXT_ENUM = _descriptor.Descriptor(
  name='video_context_enum',
  full_name='video_context_enum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VIDEO_CONTEXT_ENUM_VIDEOCONTEXT,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=165,
)

_VIDEO_CONTEXT_ENUM_VIDEOCONTEXT.containing_type = _VIDEO_CONTEXT_ENUM
DESCRIPTOR.message_types_by_name['video_context_enum'] = _VIDEO_CONTEXT_ENUM

video_context_enum = _reflection.GeneratedProtocolMessageType('video_context_enum', (_message.Message,), dict(
  DESCRIPTOR = _VIDEO_CONTEXT_ENUM,
  __module__ = 'includes.enums.video_context_enum_pb2'
  # @@protoc_insertion_point(class_scope:video_context_enum)
  ))
_sym_db.RegisterMessage(video_context_enum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n*com.appnexus.data.protobuf.generated.enums'))
# @@protoc_insertion_point(module_scope)
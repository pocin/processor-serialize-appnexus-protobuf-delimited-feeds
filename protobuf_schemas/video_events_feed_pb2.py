# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: video_events_feed.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import includes.enums.video_context_enum_pb2
import includes.enums.playback_method_enum_pb2
import includes.enums.view_result_type_enum_pb2
import includes.enums.view_non_measurable_reason_enum_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='video_events_feed.proto',
  package='',
  serialized_pb=_b('\n\x17video_events_feed.proto\x1a\'includes/enums/video_context_enum.proto\x1a)includes/enums/playback_method_enum.proto\x1a*includes/enums/view_result_type_enum.proto\x1a\x34includes/enums/view_non_measurable_reason_enum.proto\"\xbd\t\n\x11video_events_feed\x12\x11\n\tdate_time\x18\x01 \x01(\x06\x12\x15\n\rauction_id_64\x18\x02 \x01(\x06\x12\x17\n\x0f\x62uyer_member_id\x18\x03 \x01(\x05\x12\x18\n\x10seller_member_id\x18\x04 \x01(\x05\x12\x15\n\radvertiser_id\x18\x05 \x01(\x05\x12\x14\n\x0cpublisher_id\x18\x06 \x01(\x05\x12\x0f\n\x07site_id\x18\x07 \x01(\x05\x12\x0e\n\x06tag_id\x18\x08 \x01(\x05\x12\x1a\n\x12insertion_order_id\x18\t \x01(\x05\x12\x14\n\x0cline_item_id\x18\n \x01(\x05\x12\x13\n\x0b\x63\x61mpaign_id\x18\x0b \x01(\x05\x12\x13\n\x0b\x63reative_id\x18\x0c \x01(\x05\x12\x15\n\rcreative_freq\x18\r \x01(\x05\x12\x14\n\x0c\x63reative_rec\x18\x0e \x01(\x05\x12\x10\n\x08\x62rand_id\x18\x0f \x01(\x05\x12\x13\n\x07\x63ountry\x18\x10 \x01(\t:\x02--\x12\x16\n\x0e\x63reative_width\x18\x11 \x01(\x05\x12\x17\n\x0f\x63reative_height\x18\x12 \x01(\x05\x12\x0f\n\x07\x64\x65\x61l_id\x18\x13 \x01(\x05\x12\x18\n\x10video_was_served\x18\x14 \x01(\x05\x12\x15\n\rvideo_started\x18\x15 \x01(\x05\x12\x19\n\x11video_was_skipped\x18\x16 \x01(\x05\x12\x17\n\x0fvideo_had_error\x18\x17 \x01(\x05\x12\x18\n\x10video_hit_25_pct\x18\x18 \x01(\x05\x12\x18\n\x10video_hit_50_pct\x18\x19 \x01(\x05\x12\x18\n\x10video_hit_75_pct\x18\x1a \x01(\x05\x12\x17\n\x0fvideo_completed\x18\x1b \x01(\x05\x12\x10\n\x08imp_type\x18\x1c \x01(\x05\x12\x1b\n\x13\x61\x64vertiser_currency\x18\x1d \x01(\t\x12\x1a\n\x12publisher_currency\x18\x1e \x01(\t\x12\x13\n\x0bsite_domain\x18\x1f \x01(\t\x12\x16\n\x0e\x61pplication_id\x18  \x01(\t\x12\x16\n\x0emedia_cost_cpm\x18! \x01(\x01\x12\x16\n\x0e\x62ooked_revenue\x18\" \x01(\x01\x12\x1a\n\x12seller_revenue_cpm\x18# \x01(\x01\x12\x46\n\x0fplayback_method\x18$ \x01(\x0e\x32$.playback_method_enum.PlaybackMethod:\x07UNKNOWN\x12@\n\rvideo_context\x18% \x01(\x0e\x32 .video_context_enum.VideoContext:\x07UNKNOWN\x12\x19\n\x0eplayer_size_id\x18& \x01(\x05:\x01\x30\x12\x13\n\x0bsupply_type\x18\' \x01(\x05\x12\x43\n\x0bview_result\x18( \x01(\x0e\x32%.view_result_type_enum.ViewResultType:\x07UNKNOWN\x12\x65\n\x1aview_non_measurable_reason\x18) \x01(\x0e\x32\x38.view_non_measurable_reason_enum.ViewNonMeasurableReason:\x07UNKNOWN\x12\x15\n\nerror_code\x18* \x01(\x05:\x01\x30\x42&\n$com.appnexus.data.protobuf.generated')
  ,
  dependencies=[includes.enums.video_context_enum_pb2.DESCRIPTOR,includes.enums.playback_method_enum_pb2.DESCRIPTOR,includes.enums.view_result_type_enum_pb2.DESCRIPTOR,includes.enums.view_non_measurable_reason_enum_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_VIDEO_EVENTS_FEED = _descriptor.Descriptor(
  name='video_events_feed',
  full_name='video_events_feed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date_time', full_name='video_events_feed.date_time', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auction_id_64', full_name='video_events_feed.auction_id_64', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buyer_member_id', full_name='video_events_feed.buyer_member_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seller_member_id', full_name='video_events_feed.seller_member_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='advertiser_id', full_name='video_events_feed.advertiser_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='video_events_feed.publisher_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='site_id', full_name='video_events_feed.site_id', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag_id', full_name='video_events_feed.tag_id', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='insertion_order_id', full_name='video_events_feed.insertion_order_id', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line_item_id', full_name='video_events_feed.line_item_id', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='campaign_id', full_name='video_events_feed.campaign_id', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creative_id', full_name='video_events_feed.creative_id', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creative_freq', full_name='video_events_feed.creative_freq', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creative_rec', full_name='video_events_feed.creative_rec', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='brand_id', full_name='video_events_feed.brand_id', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country', full_name='video_events_feed.country', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("--").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creative_width', full_name='video_events_feed.creative_width', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creative_height', full_name='video_events_feed.creative_height', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deal_id', full_name='video_events_feed.deal_id', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_was_served', full_name='video_events_feed.video_was_served', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_started', full_name='video_events_feed.video_started', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_was_skipped', full_name='video_events_feed.video_was_skipped', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_had_error', full_name='video_events_feed.video_had_error', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_hit_25_pct', full_name='video_events_feed.video_hit_25_pct', index=23,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_hit_50_pct', full_name='video_events_feed.video_hit_50_pct', index=24,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_hit_75_pct', full_name='video_events_feed.video_hit_75_pct', index=25,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_completed', full_name='video_events_feed.video_completed', index=26,
      number=27, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imp_type', full_name='video_events_feed.imp_type', index=27,
      number=28, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='advertiser_currency', full_name='video_events_feed.advertiser_currency', index=28,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='publisher_currency', full_name='video_events_feed.publisher_currency', index=29,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='site_domain', full_name='video_events_feed.site_domain', index=30,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='application_id', full_name='video_events_feed.application_id', index=31,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_cost_cpm', full_name='video_events_feed.media_cost_cpm', index=32,
      number=33, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='booked_revenue', full_name='video_events_feed.booked_revenue', index=33,
      number=34, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seller_revenue_cpm', full_name='video_events_feed.seller_revenue_cpm', index=34,
      number=35, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='playback_method', full_name='video_events_feed.playback_method', index=35,
      number=36, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_context', full_name='video_events_feed.video_context', index=36,
      number=37, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_size_id', full_name='video_events_feed.player_size_id', index=37,
      number=38, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supply_type', full_name='video_events_feed.supply_type', index=38,
      number=39, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='view_result', full_name='video_events_feed.view_result', index=39,
      number=40, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='view_non_measurable_reason', full_name='video_events_feed.view_non_measurable_reason', index=40,
      number=41, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='video_events_feed.error_code', index=41,
      number=42, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=210,
  serialized_end=1423,
)

_VIDEO_EVENTS_FEED.fields_by_name['playback_method'].enum_type = includes.enums.playback_method_enum_pb2._PLAYBACK_METHOD_ENUM_PLAYBACKMETHOD
_VIDEO_EVENTS_FEED.fields_by_name['video_context'].enum_type = includes.enums.video_context_enum_pb2._VIDEO_CONTEXT_ENUM_VIDEOCONTEXT
_VIDEO_EVENTS_FEED.fields_by_name['view_result'].enum_type = includes.enums.view_result_type_enum_pb2._VIEW_RESULT_TYPE_ENUM_VIEWRESULTTYPE
_VIDEO_EVENTS_FEED.fields_by_name['view_non_measurable_reason'].enum_type = includes.enums.view_non_measurable_reason_enum_pb2._VIEW_NON_MEASURABLE_REASON_ENUM_VIEWNONMEASURABLEREASON
DESCRIPTOR.message_types_by_name['video_events_feed'] = _VIDEO_EVENTS_FEED

video_events_feed = _reflection.GeneratedProtocolMessageType('video_events_feed', (_message.Message,), dict(
  DESCRIPTOR = _VIDEO_EVENTS_FEED,
  __module__ = 'video_events_feed_pb2'
  # @@protoc_insertion_point(class_scope:video_events_feed)
  ))
_sym_db.RegisterMessage(video_events_feed)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.appnexus.data.protobuf.generated'))
# @@protoc_insertion_point(module_scope)

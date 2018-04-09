# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bid_landscape_feed.proto

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
  name='bid_landscape_feed.proto',
  package='',
  serialized_pb=_b('\n\x18\x62id_landscape_feed.proto\"\xed\x05\n\x12\x62id_landscape_feed\x12\x11\n\tdate_time\x18\x01 \x01(\x06\x12\x15\n\rauction_id_64\x18\x02 \x01(\x06\x12\x12\n\nuser_id_64\x18\x03 \x01(\x06\x12\x10\n\x08\x62rand_id\x18\x04 \x01(\x05\x12\x13\n\x0b\x63reative_id\x18\x05 \x01(\x05\x12\x18\n\x10\x61\x63tual_bid_price\x18\x06 \x01(\x01\x12\x18\n\x10\x62iased_bid_price\x18\x07 \x01(\x01\x12\x19\n\x11\x62id_reject_reason\x18\x08 \x01(\x05\x12\x13\n\x0bym_floor_id\x18\t \x01(\x05\x12\x12\n\nym_bias_id\x18\n \x01(\x05\x12\x11\n\tbidder_id\x18\x0b \x01(\x05\x12\x17\n\x0f\x62uyer_member_id\x18\x0c \x01(\x05\x12\x18\n\x10seller_member_id\x18\r \x01(\x05\x12\x1a\n\x12total_bid_modifier\x18\x0e \x01(\x01\x12\x1c\n\x11\x65xclusivity_level\x18\x0f \x01(\x05:\x01\x30\x12\x1d\n\x12ym_auction_tier_id\x18\x10 \x01(\x05:\x01\x30\x12\x15\n\nhard_floor\x18\x11 \x01(\x01:\x01\x30\x12\x1e\n\x13modified_hard_floor\x18\x12 \x01(\x01:\x01\x30\x12\x15\n\nsoft_floor\x18\x13 \x01(\x01:\x01\x30\x12\x1e\n\x13modified_soft_floor\x18\x14 \x01(\x01:\x01\x30\x12\x1b\n\x10\x62id_payment_type\x18\x15 \x01(\x05:\x01\x30\x12\x19\n\x0eis_winning_bid\x18\x16 \x01(\x05:\x01\x30\x12\x12\n\x07\x64\x65\x61l_id\x18\x17 \x01(\x05:\x01\x30\x12\x18\n\rad_profile_id\x18\x18 \x01(\x05:\x01\x30\x12\x1a\n\x0fis_mediated_bid\x18\x19 \x01(\x05:\x01\x30\x12\x19\n\x11raw_net_bid_price\x18\x1a \x01(\x01\x12\x1b\n\x13\x65xternal_request_id\x18\x1b \x01(\t\x12\x16\n\x0e\x62id_price_type\x18\x1c \x01(\x05\x12\x1b\n\x11hashed_user_id_64\x18\x1d \x01(\x0c:\x00\x42&\n$com.appnexus.data.protobuf.generated')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BID_LANDSCAPE_FEED = _descriptor.Descriptor(
  name='bid_landscape_feed',
  full_name='bid_landscape_feed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date_time', full_name='bid_landscape_feed.date_time', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auction_id_64', full_name='bid_landscape_feed.auction_id_64', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id_64', full_name='bid_landscape_feed.user_id_64', index=2,
      number=3, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='brand_id', full_name='bid_landscape_feed.brand_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creative_id', full_name='bid_landscape_feed.creative_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='actual_bid_price', full_name='bid_landscape_feed.actual_bid_price', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='biased_bid_price', full_name='bid_landscape_feed.biased_bid_price', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid_reject_reason', full_name='bid_landscape_feed.bid_reject_reason', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ym_floor_id', full_name='bid_landscape_feed.ym_floor_id', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ym_bias_id', full_name='bid_landscape_feed.ym_bias_id', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bidder_id', full_name='bid_landscape_feed.bidder_id', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buyer_member_id', full_name='bid_landscape_feed.buyer_member_id', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seller_member_id', full_name='bid_landscape_feed.seller_member_id', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_bid_modifier', full_name='bid_landscape_feed.total_bid_modifier', index=13,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exclusivity_level', full_name='bid_landscape_feed.exclusivity_level', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ym_auction_tier_id', full_name='bid_landscape_feed.ym_auction_tier_id', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hard_floor', full_name='bid_landscape_feed.hard_floor', index=16,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modified_hard_floor', full_name='bid_landscape_feed.modified_hard_floor', index=17,
      number=18, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='soft_floor', full_name='bid_landscape_feed.soft_floor', index=18,
      number=19, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modified_soft_floor', full_name='bid_landscape_feed.modified_soft_floor', index=19,
      number=20, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid_payment_type', full_name='bid_landscape_feed.bid_payment_type', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_winning_bid', full_name='bid_landscape_feed.is_winning_bid', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deal_id', full_name='bid_landscape_feed.deal_id', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ad_profile_id', full_name='bid_landscape_feed.ad_profile_id', index=23,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_mediated_bid', full_name='bid_landscape_feed.is_mediated_bid', index=24,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_net_bid_price', full_name='bid_landscape_feed.raw_net_bid_price', index=25,
      number=26, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external_request_id', full_name='bid_landscape_feed.external_request_id', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid_price_type', full_name='bid_landscape_feed.bid_price_type', index=27,
      number=28, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hashed_user_id_64', full_name='bid_landscape_feed.hashed_user_id_64', index=28,
      number=29, type=12, cpp_type=9, label=1,
      has_default_value=True, default_value=_b(""),
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
  serialized_start=29,
  serialized_end=778,
)

DESCRIPTOR.message_types_by_name['bid_landscape_feed'] = _BID_LANDSCAPE_FEED

bid_landscape_feed = _reflection.GeneratedProtocolMessageType('bid_landscape_feed', (_message.Message,), dict(
  DESCRIPTOR = _BID_LANDSCAPE_FEED,
  __module__ = 'bid_landscape_feed_pb2'
  # @@protoc_insertion_point(class_scope:bid_landscape_feed)
  ))
_sym_db.RegisterMessage(bid_landscape_feed)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.appnexus.data.protobuf.generated'))
# @@protoc_insertion_point(module_scope)

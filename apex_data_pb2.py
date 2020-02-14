# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apex_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='apex_data.proto',
  package='apex',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0f\x61pex_data.proto\x12\x04\x61pex\"Y\n\x12\x42\x61tchPrioriRequest\x12\r\n\x05idxes\x18\x01 \x03(\x05\x12\x0f\n\x07prioris\x18\x02 \x03(\x02\x12\x10\n\x08\x61\x63tor_id\x18\x03 \x01(\x05\x12\x11\n\ttimestamp\x18\x04 \x03(\x02\"\'\n\x13\x42\x61tchPrioriResponse\x12\x10\n\x08response\x18\x01 \x01(\x08\"5\n\x13UpdatePrioriRequest\x12\r\n\x05idxes\x18\x01 \x03(\x05\x12\x0f\n\x07prioris\x18\x02 \x03(\x02\"(\n\x14UpdatePrioriResponse\x12\x10\n\x08response\x18\x01 \x01(\x08\"!\n\x10RealBatchRequest\x12\r\n\x05idxes\x18\x01 \x03(\x05\"\x83\x01\n\x10RealDataResponse\x12\r\n\x05state\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\x05\x12\x0e\n\x06reward\x18\x03 \x01(\x02\x12\x12\n\nnext_state\x18\x04 \x01(\x0c\x12\x0c\n\x04\x64one\x18\x05 \x01(\x08\x12\x0b\n\x03idx\x18\x06 \x01(\x05\x12\x11\n\ttimestamp\x18\x07 \x01(\x02\"&\n\x11ParametersRequest\x12\x11\n\tparam_req\x18\x01 \x01(\x08\"=\n\x0fSingleParameter\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\x02\x12\r\n\x05shape\x18\x03 \x03(\x05\"5\n\x11SampleDataRequest\x12\x12\n\nbatch_size\x18\x01 \x01(\x05\x12\x0c\n\x04\x62\x65ta\x18\x02 \x01(\x02\"l\n\x12SampleDataResponse\x12\x11\n\tactor_ids\x18\x01 \x03(\x05\x12\x10\n\x08\x64\x61ta_ids\x18\x02 \x03(\x05\x12\x11\n\ttimestamp\x18\x03 \x03(\x02\x12\x0f\n\x07weights\x18\x04 \x03(\x02\x12\r\n\x05idxes\x18\x05 \x03(\x05\"\x9b\x01\n\x18SampleSingleDataResponse\x12\r\n\x05state\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\x05\x12\x0e\n\x06reward\x18\x03 \x01(\x02\x12\x12\n\nnext_state\x18\x04 \x01(\x0c\x12\x0c\n\x04\x64one\x18\x05 \x01(\x08\x12\x0e\n\x06weight\x18\x06 \x01(\x02\x12\x0b\n\x03idx\x18\x07 \x01(\x05\x12\x11\n\ttimestamp\x18\x08 \x01(\x02\"M\n\x14\x41\x63torRegisterRequest\x12\x10\n\x08\x61\x63tor_ip\x18\x01 \x01(\t\x12\x10\n\x08\x61\x63tor_id\x18\x02 \x01(\x05\x12\x11\n\tdata_port\x18\x03 \x01(\t\")\n\x15\x41\x63torRegisterResponse\x12\x10\n\x08response\x18\x01 \x01(\x08\"#\n\x12\x43\x61\x63heUpdateRequest\x12\r\n\x05idxes\x18\x01 \x03(\x05\"\'\n\x13\x43\x61\x63heUpdateResponse\x12\x10\n\x08response\x18\x01 \x01(\x08\x32P\n\x0fSendBatchPriori\x12=\n\x04Send\x12\x18.apex.BatchPrioriRequest\x1a\x19.apex.BatchPrioriResponse\"\x00\x32J\n\x0cSendRealData\x12:\n\x04Send\x12\x16.apex.RealBatchRequest\x1a\x16.apex.RealDataResponse\"\x00\x30\x01\x32I\n\nSampleData\x12;\n\x04Send\x12\x17.apex.SampleDataRequest\x1a\x18.apex.SampleDataResponse\"\x00\x32T\n\x11UpdateBatchPriori\x12?\n\x04Send\x12\x19.apex.UpdatePrioriRequest\x1a\x1a.apex.UpdatePrioriResponse\"\x00\x32K\n\rSendParameter\x12:\n\x04Send\x12\x17.apex.ParametersRequest\x1a\x15.apex.SingleParameter\"\x00\x30\x01\x32R\n\rRegisterActor\x12\x41\n\x04Send\x12\x1a.apex.ActorRegisterRequest\x1a\x1b.apex.ActorRegisterResponse\"\x00\x32L\n\x0b\x43\x61\x63heUpdate\x12=\n\x04Send\x12\x18.apex.CacheUpdateRequest\x1a\x19.apex.CacheUpdateResponse\"\x00\x62\x06proto3')
)




_BATCHPRIORIREQUEST = _descriptor.Descriptor(
  name='BatchPrioriRequest',
  full_name='apex.BatchPrioriRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idxes', full_name='apex.BatchPrioriRequest.idxes', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prioris', full_name='apex.BatchPrioriRequest.prioris', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actor_id', full_name='apex.BatchPrioriRequest.actor_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='apex.BatchPrioriRequest.timestamp', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=114,
)


_BATCHPRIORIRESPONSE = _descriptor.Descriptor(
  name='BatchPrioriResponse',
  full_name='apex.BatchPrioriResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='apex.BatchPrioriResponse.response', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=155,
)


_UPDATEPRIORIREQUEST = _descriptor.Descriptor(
  name='UpdatePrioriRequest',
  full_name='apex.UpdatePrioriRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idxes', full_name='apex.UpdatePrioriRequest.idxes', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prioris', full_name='apex.UpdatePrioriRequest.prioris', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=210,
)


_UPDATEPRIORIRESPONSE = _descriptor.Descriptor(
  name='UpdatePrioriResponse',
  full_name='apex.UpdatePrioriResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='apex.UpdatePrioriResponse.response', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=252,
)


_REALBATCHREQUEST = _descriptor.Descriptor(
  name='RealBatchRequest',
  full_name='apex.RealBatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idxes', full_name='apex.RealBatchRequest.idxes', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=287,
)


_REALDATARESPONSE = _descriptor.Descriptor(
  name='RealDataResponse',
  full_name='apex.RealDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='apex.RealDataResponse.state', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='apex.RealDataResponse.action', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward', full_name='apex.RealDataResponse.reward', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_state', full_name='apex.RealDataResponse.next_state', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='done', full_name='apex.RealDataResponse.done', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='idx', full_name='apex.RealDataResponse.idx', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='apex.RealDataResponse.timestamp', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=421,
)


_PARAMETERSREQUEST = _descriptor.Descriptor(
  name='ParametersRequest',
  full_name='apex.ParametersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_req', full_name='apex.ParametersRequest.param_req', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=461,
)


_SINGLEPARAMETER = _descriptor.Descriptor(
  name='SingleParameter',
  full_name='apex.SingleParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='apex.SingleParameter.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='apex.SingleParameter.values', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='apex.SingleParameter.shape', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=463,
  serialized_end=524,
)


_SAMPLEDATAREQUEST = _descriptor.Descriptor(
  name='SampleDataRequest',
  full_name='apex.SampleDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='apex.SampleDataRequest.batch_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beta', full_name='apex.SampleDataRequest.beta', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=526,
  serialized_end=579,
)


_SAMPLEDATARESPONSE = _descriptor.Descriptor(
  name='SampleDataResponse',
  full_name='apex.SampleDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actor_ids', full_name='apex.SampleDataResponse.actor_ids', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_ids', full_name='apex.SampleDataResponse.data_ids', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='apex.SampleDataResponse.timestamp', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weights', full_name='apex.SampleDataResponse.weights', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='idxes', full_name='apex.SampleDataResponse.idxes', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=581,
  serialized_end=689,
)


_SAMPLESINGLEDATARESPONSE = _descriptor.Descriptor(
  name='SampleSingleDataResponse',
  full_name='apex.SampleSingleDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='apex.SampleSingleDataResponse.state', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='apex.SampleSingleDataResponse.action', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward', full_name='apex.SampleSingleDataResponse.reward', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_state', full_name='apex.SampleSingleDataResponse.next_state', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='done', full_name='apex.SampleSingleDataResponse.done', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='apex.SampleSingleDataResponse.weight', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='idx', full_name='apex.SampleSingleDataResponse.idx', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='apex.SampleSingleDataResponse.timestamp', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=692,
  serialized_end=847,
)


_ACTORREGISTERREQUEST = _descriptor.Descriptor(
  name='ActorRegisterRequest',
  full_name='apex.ActorRegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actor_ip', full_name='apex.ActorRegisterRequest.actor_ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actor_id', full_name='apex.ActorRegisterRequest.actor_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_port', full_name='apex.ActorRegisterRequest.data_port', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=849,
  serialized_end=926,
)


_ACTORREGISTERRESPONSE = _descriptor.Descriptor(
  name='ActorRegisterResponse',
  full_name='apex.ActorRegisterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='apex.ActorRegisterResponse.response', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=928,
  serialized_end=969,
)


_CACHEUPDATEREQUEST = _descriptor.Descriptor(
  name='CacheUpdateRequest',
  full_name='apex.CacheUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idxes', full_name='apex.CacheUpdateRequest.idxes', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=971,
  serialized_end=1006,
)


_CACHEUPDATERESPONSE = _descriptor.Descriptor(
  name='CacheUpdateResponse',
  full_name='apex.CacheUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='apex.CacheUpdateResponse.response', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1008,
  serialized_end=1047,
)

DESCRIPTOR.message_types_by_name['BatchPrioriRequest'] = _BATCHPRIORIREQUEST
DESCRIPTOR.message_types_by_name['BatchPrioriResponse'] = _BATCHPRIORIRESPONSE
DESCRIPTOR.message_types_by_name['UpdatePrioriRequest'] = _UPDATEPRIORIREQUEST
DESCRIPTOR.message_types_by_name['UpdatePrioriResponse'] = _UPDATEPRIORIRESPONSE
DESCRIPTOR.message_types_by_name['RealBatchRequest'] = _REALBATCHREQUEST
DESCRIPTOR.message_types_by_name['RealDataResponse'] = _REALDATARESPONSE
DESCRIPTOR.message_types_by_name['ParametersRequest'] = _PARAMETERSREQUEST
DESCRIPTOR.message_types_by_name['SingleParameter'] = _SINGLEPARAMETER
DESCRIPTOR.message_types_by_name['SampleDataRequest'] = _SAMPLEDATAREQUEST
DESCRIPTOR.message_types_by_name['SampleDataResponse'] = _SAMPLEDATARESPONSE
DESCRIPTOR.message_types_by_name['SampleSingleDataResponse'] = _SAMPLESINGLEDATARESPONSE
DESCRIPTOR.message_types_by_name['ActorRegisterRequest'] = _ACTORREGISTERREQUEST
DESCRIPTOR.message_types_by_name['ActorRegisterResponse'] = _ACTORREGISTERRESPONSE
DESCRIPTOR.message_types_by_name['CacheUpdateRequest'] = _CACHEUPDATEREQUEST
DESCRIPTOR.message_types_by_name['CacheUpdateResponse'] = _CACHEUPDATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BatchPrioriRequest = _reflection.GeneratedProtocolMessageType('BatchPrioriRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHPRIORIREQUEST,
  '__module__' : 'apex_data_pb2'
  # @@protoc_insertion_point(class_scope:apex.BatchPrioriRequest)
  })
_sym_db.RegisterMessage(BatchPrioriRequest)

BatchPrioriResponse = _reflection.GeneratedProtocolMessageType('BatchPrioriResponse', (_message.Message,), {
  'DESCRIPTOR' : _BATCHPRIORIRESPONSE,
  '__module__' : 'apex_data_pb2'
  # @@protoc_insertion_point(class_scope:apex.BatchPrioriResponse)
  })
_sym_db.RegisterMessage(BatchPrioriResponse)

UpdatePrioriRequest = _reflection.GeneratedProtocolMessageType('UpdatePrioriRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPRIORIREQUEST,
  '__module__' : 'apex_data_pb2'
  # @@protoc_insertion_point(class_scope:apex.UpdatePrioriRequest)
  })
_sym_db.RegisterMessage(UpdatePrioriRequest)

UpdatePrioriResponse = _reflection.GeneratedProtocolMessageType('UpdatePrioriResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPRIORIRESPONSE,
  '__module__' : 'apex_data_pb2'
  # @@protoc_insertion_point(class_scope:apex.UpdatePrioriResponse)
  })
_sym_db.RegisterMessage(UpdatePrioriResponse)

RealBatchRequest = _reflection.GeneratedProtocolMessageType('RealBatchRequest', (_message.Message,), {
  'DESCRIPTOR' : _REALBATCHREQUEST,
  '__module__' : 'apex_data_pb2'
  # @@protoc_insertion_point(class_scope:apex.RealBatchRequest)
  })
_sym_db.RegisterMessage(RealBatchRequest)

RealDataResponse = _reflection.GeneratedProtocolMessageType('RealDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _REALDATARESPONSE,
  '__module__' : 'apex_data_pb2'
  # @@protoc_insertion_point(class_scope:apex.RealDataResponse)
  })
_sym_db.RegisterMessage(RealDataResponse)

ParametersRequest = _reflection.GeneratedProtocolMessageType('ParametersRequest', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETERSREQUEST,
  '__module__' : 'apex_data_pb2'
  # @@protoc_insertion_point(class_scope:apex.ParametersRequest)
  })
_sym_db.RegisterMessage(ParametersRequest)

SingleParameter = _reflection.GeneratedProtocolMessageType('SingleParameter', (_message.Message,), {
  'DESCRIPTOR' : _SINGLEPARAMETER,
  '__module__' : 'apex_data_pb2'
  # @@protoc_insertion_point(class_scope:apex.SingleParameter)
  })
_sym_db.RegisterMessage(SingleParameter)

SampleDataRequest = _reflection.GeneratedProtocolMessageType('SampleDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLEDATAREQUEST,
  '__module__' : 'apex_data_pb2'
  # @@protoc_insertion_point(class_scope:apex.SampleDataRequest)
  })
_sym_db.RegisterMessage(SampleDataRequest)

SampleDataResponse = _reflection.GeneratedProtocolMessageType('SampleDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLEDATARESPONSE,
  '__module__' : 'apex_data_pb2'
  # @@protoc_insertion_point(class_scope:apex.SampleDataResponse)
  })
_sym_db.RegisterMessage(SampleDataResponse)

SampleSingleDataResponse = _reflection.GeneratedProtocolMessageType('SampleSingleDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLESINGLEDATARESPONSE,
  '__module__' : 'apex_data_pb2'
  # @@protoc_insertion_point(class_scope:apex.SampleSingleDataResponse)
  })
_sym_db.RegisterMessage(SampleSingleDataResponse)

ActorRegisterRequest = _reflection.GeneratedProtocolMessageType('ActorRegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTORREGISTERREQUEST,
  '__module__' : 'apex_data_pb2'
  # @@protoc_insertion_point(class_scope:apex.ActorRegisterRequest)
  })
_sym_db.RegisterMessage(ActorRegisterRequest)

ActorRegisterResponse = _reflection.GeneratedProtocolMessageType('ActorRegisterResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTORREGISTERRESPONSE,
  '__module__' : 'apex_data_pb2'
  # @@protoc_insertion_point(class_scope:apex.ActorRegisterResponse)
  })
_sym_db.RegisterMessage(ActorRegisterResponse)

CacheUpdateRequest = _reflection.GeneratedProtocolMessageType('CacheUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CACHEUPDATEREQUEST,
  '__module__' : 'apex_data_pb2'
  # @@protoc_insertion_point(class_scope:apex.CacheUpdateRequest)
  })
_sym_db.RegisterMessage(CacheUpdateRequest)

CacheUpdateResponse = _reflection.GeneratedProtocolMessageType('CacheUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CACHEUPDATERESPONSE,
  '__module__' : 'apex_data_pb2'
  # @@protoc_insertion_point(class_scope:apex.CacheUpdateResponse)
  })
_sym_db.RegisterMessage(CacheUpdateResponse)



_SENDBATCHPRIORI = _descriptor.ServiceDescriptor(
  name='SendBatchPriori',
  full_name='apex.SendBatchPriori',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1049,
  serialized_end=1129,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='apex.SendBatchPriori.Send',
    index=0,
    containing_service=None,
    input_type=_BATCHPRIORIREQUEST,
    output_type=_BATCHPRIORIRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SENDBATCHPRIORI)

DESCRIPTOR.services_by_name['SendBatchPriori'] = _SENDBATCHPRIORI


_SENDREALDATA = _descriptor.ServiceDescriptor(
  name='SendRealData',
  full_name='apex.SendRealData',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=1131,
  serialized_end=1205,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='apex.SendRealData.Send',
    index=0,
    containing_service=None,
    input_type=_REALBATCHREQUEST,
    output_type=_REALDATARESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SENDREALDATA)

DESCRIPTOR.services_by_name['SendRealData'] = _SENDREALDATA


_SAMPLEDATA = _descriptor.ServiceDescriptor(
  name='SampleData',
  full_name='apex.SampleData',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=1207,
  serialized_end=1280,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='apex.SampleData.Send',
    index=0,
    containing_service=None,
    input_type=_SAMPLEDATAREQUEST,
    output_type=_SAMPLEDATARESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SAMPLEDATA)

DESCRIPTOR.services_by_name['SampleData'] = _SAMPLEDATA


_UPDATEBATCHPRIORI = _descriptor.ServiceDescriptor(
  name='UpdateBatchPriori',
  full_name='apex.UpdateBatchPriori',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  serialized_start=1282,
  serialized_end=1366,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='apex.UpdateBatchPriori.Send',
    index=0,
    containing_service=None,
    input_type=_UPDATEPRIORIREQUEST,
    output_type=_UPDATEPRIORIRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_UPDATEBATCHPRIORI)

DESCRIPTOR.services_by_name['UpdateBatchPriori'] = _UPDATEBATCHPRIORI


_SENDPARAMETER = _descriptor.ServiceDescriptor(
  name='SendParameter',
  full_name='apex.SendParameter',
  file=DESCRIPTOR,
  index=4,
  serialized_options=None,
  serialized_start=1368,
  serialized_end=1443,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='apex.SendParameter.Send',
    index=0,
    containing_service=None,
    input_type=_PARAMETERSREQUEST,
    output_type=_SINGLEPARAMETER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SENDPARAMETER)

DESCRIPTOR.services_by_name['SendParameter'] = _SENDPARAMETER


_REGISTERACTOR = _descriptor.ServiceDescriptor(
  name='RegisterActor',
  full_name='apex.RegisterActor',
  file=DESCRIPTOR,
  index=5,
  serialized_options=None,
  serialized_start=1445,
  serialized_end=1527,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='apex.RegisterActor.Send',
    index=0,
    containing_service=None,
    input_type=_ACTORREGISTERREQUEST,
    output_type=_ACTORREGISTERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_REGISTERACTOR)

DESCRIPTOR.services_by_name['RegisterActor'] = _REGISTERACTOR


_CACHEUPDATE = _descriptor.ServiceDescriptor(
  name='CacheUpdate',
  full_name='apex.CacheUpdate',
  file=DESCRIPTOR,
  index=6,
  serialized_options=None,
  serialized_start=1529,
  serialized_end=1605,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='apex.CacheUpdate.Send',
    index=0,
    containing_service=None,
    input_type=_CACHEUPDATEREQUEST,
    output_type=_CACHEUPDATERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CACHEUPDATE)

DESCRIPTOR.services_by_name['CacheUpdate'] = _CACHEUPDATE

# @@protoc_insertion_point(module_scope)

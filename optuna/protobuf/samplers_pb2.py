# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: optuna/protobuf/samplers.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='optuna/protobuf/samplers.proto',
  package='optuna.samplers',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1eoptuna/protobuf/samplers.proto\x12\x0foptuna.samplers\"x\n\x07Sampler\x12*\n\x03tpe\x18\x01 \x01(\x0b\x32\x1b.optuna.samplers.TPESamplerH\x00\x12\x30\n\x06random\x18\x02 \x01(\x0b\x32\x1e.optuna.samplers.RandomSamplerH\x00\x42\x0f\n\rsampler_oneof\"\xd4\x01\n\nTPESampler\x12\x16\n\x0e\x63onsider_prior\x18\x01 \x01(\x08\x12\x14\n\x0cprior_weight\x18\x02 \x01(\x02\x12\x1b\n\x13\x63onsider_magic_clip\x18\x03 \x01(\x08\x12\x1a\n\x12\x63onsider_endpoints\x18\x04 \x01(\x08\x12\x18\n\x10n_startup_trials\x18\x05 \x01(\r\x12\x17\n\x0fn_ei_candidates\x18\x06 \x01(\r\x12\r\n\x05gamma\x18\x07 \x01(\r\x12\x0f\n\x07weights\x18\x08 \x03(\r\x12\x0c\n\x04seed\x18\t \x01(\r\"\x1d\n\rRandomSampler\x12\x0c\n\x04seed\x18\x01 \x01(\rb\x06proto3')
)




_SAMPLER = _descriptor.Descriptor(
  name='Sampler',
  full_name='optuna.samplers.Sampler',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tpe', full_name='optuna.samplers.Sampler.tpe', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='random', full_name='optuna.samplers.Sampler.random', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='sampler_oneof', full_name='optuna.samplers.Sampler.sampler_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=51,
  serialized_end=171,
)


_TPESAMPLER = _descriptor.Descriptor(
  name='TPESampler',
  full_name='optuna.samplers.TPESampler',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='consider_prior', full_name='optuna.samplers.TPESampler.consider_prior', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prior_weight', full_name='optuna.samplers.TPESampler.prior_weight', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consider_magic_clip', full_name='optuna.samplers.TPESampler.consider_magic_clip', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consider_endpoints', full_name='optuna.samplers.TPESampler.consider_endpoints', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_startup_trials', full_name='optuna.samplers.TPESampler.n_startup_trials', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_ei_candidates', full_name='optuna.samplers.TPESampler.n_ei_candidates', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gamma', full_name='optuna.samplers.TPESampler.gamma', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weights', full_name='optuna.samplers.TPESampler.weights', index=7,
      number=8, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seed', full_name='optuna.samplers.TPESampler.seed', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=174,
  serialized_end=386,
)


_RANDOMSAMPLER = _descriptor.Descriptor(
  name='RandomSampler',
  full_name='optuna.samplers.RandomSampler',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seed', full_name='optuna.samplers.RandomSampler.seed', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=388,
  serialized_end=417,
)

_SAMPLER.fields_by_name['tpe'].message_type = _TPESAMPLER
_SAMPLER.fields_by_name['random'].message_type = _RANDOMSAMPLER
_SAMPLER.oneofs_by_name['sampler_oneof'].fields.append(
  _SAMPLER.fields_by_name['tpe'])
_SAMPLER.fields_by_name['tpe'].containing_oneof = _SAMPLER.oneofs_by_name['sampler_oneof']
_SAMPLER.oneofs_by_name['sampler_oneof'].fields.append(
  _SAMPLER.fields_by_name['random'])
_SAMPLER.fields_by_name['random'].containing_oneof = _SAMPLER.oneofs_by_name['sampler_oneof']
DESCRIPTOR.message_types_by_name['Sampler'] = _SAMPLER
DESCRIPTOR.message_types_by_name['TPESampler'] = _TPESAMPLER
DESCRIPTOR.message_types_by_name['RandomSampler'] = _RANDOMSAMPLER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Sampler = _reflection.GeneratedProtocolMessageType('Sampler', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLER,
  __module__ = 'optuna.protobuf.samplers_pb2'
  # @@protoc_insertion_point(class_scope:optuna.samplers.Sampler)
  ))
_sym_db.RegisterMessage(Sampler)

TPESampler = _reflection.GeneratedProtocolMessageType('TPESampler', (_message.Message,), dict(
  DESCRIPTOR = _TPESAMPLER,
  __module__ = 'optuna.protobuf.samplers_pb2'
  # @@protoc_insertion_point(class_scope:optuna.samplers.TPESampler)
  ))
_sym_db.RegisterMessage(TPESampler)

RandomSampler = _reflection.GeneratedProtocolMessageType('RandomSampler', (_message.Message,), dict(
  DESCRIPTOR = _RANDOMSAMPLER,
  __module__ = 'optuna.protobuf.samplers_pb2'
  # @@protoc_insertion_point(class_scope:optuna.samplers.RandomSampler)
  ))
_sym_db.RegisterMessage(RandomSampler)


# @@protoc_insertion_point(module_scope)

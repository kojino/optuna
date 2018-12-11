# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: optuna/protobuf/pruners.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='optuna/protobuf/pruners.proto',
  package='optuna.pruners',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1doptuna/protobuf/pruners.proto\x12\x0eoptuna.pruners\"H\n\x06Pruner\x12.\n\x06median\x18\x01 \x01(\x0b\x32\x1c.optuna.pruners.MedianPrunerH\x00\x42\x0e\n\x0cpruner_oneof\"A\n\x0cMedianPruner\x12\x19\n\x11n_start_up_trials\x18\x01 \x01(\r\x12\x16\n\x0en_warmup_steps\x18\x02 \x01(\rb\x06proto3')
)




_PRUNER = _descriptor.Descriptor(
  name='Pruner',
  full_name='optuna.pruners.Pruner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='median', full_name='optuna.pruners.Pruner.median', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
      name='pruner_oneof', full_name='optuna.pruners.Pruner.pruner_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=49,
  serialized_end=121,
)


_MEDIANPRUNER = _descriptor.Descriptor(
  name='MedianPruner',
  full_name='optuna.pruners.MedianPruner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n_start_up_trials', full_name='optuna.pruners.MedianPruner.n_start_up_trials', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_warmup_steps', full_name='optuna.pruners.MedianPruner.n_warmup_steps', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=123,
  serialized_end=188,
)

_PRUNER.fields_by_name['median'].message_type = _MEDIANPRUNER
_PRUNER.oneofs_by_name['pruner_oneof'].fields.append(
  _PRUNER.fields_by_name['median'])
_PRUNER.fields_by_name['median'].containing_oneof = _PRUNER.oneofs_by_name['pruner_oneof']
DESCRIPTOR.message_types_by_name['Pruner'] = _PRUNER
DESCRIPTOR.message_types_by_name['MedianPruner'] = _MEDIANPRUNER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pruner = _reflection.GeneratedProtocolMessageType('Pruner', (_message.Message,), dict(
  DESCRIPTOR = _PRUNER,
  __module__ = 'optuna.protobuf.pruners_pb2'
  # @@protoc_insertion_point(class_scope:optuna.pruners.Pruner)
  ))
_sym_db.RegisterMessage(Pruner)

MedianPruner = _reflection.GeneratedProtocolMessageType('MedianPruner', (_message.Message,), dict(
  DESCRIPTOR = _MEDIANPRUNER,
  __module__ = 'optuna.protobuf.pruners_pb2'
  # @@protoc_insertion_point(class_scope:optuna.pruners.MedianPruner)
  ))
_sym_db.RegisterMessage(MedianPruner)


# @@protoc_insertion_point(module_scope)

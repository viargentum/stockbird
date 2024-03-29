# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stockbird/protos/mentions.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stockbird/protos/mentions.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fstockbird/protos/mentions.proto\"R\n\x07Mention\x12\x0e\n\x06\x61uthor\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x1d\n\x07\x63ommand\x18\x04 \x01(\x0e\x32\x0c.CommandType\"5\n\x08\x42\x65stMove\x12\x0b\n\x03\x66\x65n\x18\x01 \x01(\t\x12\x12\n\x05\x64\x65pth\x18\x02 \x01(\x05H\x00\x88\x01\x01\x42\x08\n\x06_depth\")\n\tStartGame\x12\x12\n\x05\x64\x65pth\x18\x01 \x01(\x05H\x00\x88\x01\x01\x42\x08\n\x06_depth*,\n\x0b\x43ommandType\x12\r\n\tBEST_MOVE\x10\x00\x12\x0e\n\nSTART_GAME\x10\x01\x62\x06proto3'
)

_COMMANDTYPE = _descriptor.EnumDescriptor(
  name='CommandType',
  full_name='CommandType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BEST_MOVE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='START_GAME', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=217,
  serialized_end=261,
)
_sym_db.RegisterEnumDescriptor(_COMMANDTYPE)

CommandType = enum_type_wrapper.EnumTypeWrapper(_COMMANDTYPE)
BEST_MOVE = 0
START_GAME = 1



_MENTION = _descriptor.Descriptor(
  name='Mention',
  full_name='Mention',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='author', full_name='Mention.author', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='Mention.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='Mention.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='command', full_name='Mention.command', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=35,
  serialized_end=117,
)


_BESTMOVE = _descriptor.Descriptor(
  name='BestMove',
  full_name='BestMove',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fen', full_name='BestMove.fen', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='depth', full_name='BestMove.depth', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='_depth', full_name='BestMove._depth',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=119,
  serialized_end=172,
)


_STARTGAME = _descriptor.Descriptor(
  name='StartGame',
  full_name='StartGame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='depth', full_name='StartGame.depth', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='_depth', full_name='StartGame._depth',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=174,
  serialized_end=215,
)

_MENTION.fields_by_name['command'].enum_type = _COMMANDTYPE
_BESTMOVE.oneofs_by_name['_depth'].fields.append(
  _BESTMOVE.fields_by_name['depth'])
_BESTMOVE.fields_by_name['depth'].containing_oneof = _BESTMOVE.oneofs_by_name['_depth']
_STARTGAME.oneofs_by_name['_depth'].fields.append(
  _STARTGAME.fields_by_name['depth'])
_STARTGAME.fields_by_name['depth'].containing_oneof = _STARTGAME.oneofs_by_name['_depth']
DESCRIPTOR.message_types_by_name['Mention'] = _MENTION
DESCRIPTOR.message_types_by_name['BestMove'] = _BESTMOVE
DESCRIPTOR.message_types_by_name['StartGame'] = _STARTGAME
DESCRIPTOR.enum_types_by_name['CommandType'] = _COMMANDTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Mention = _reflection.GeneratedProtocolMessageType('Mention', (_message.Message,), {
  'DESCRIPTOR' : _MENTION,
  '__module__' : 'stockbird.protos.mentions_pb2'
  # @@protoc_insertion_point(class_scope:Mention)
  })
_sym_db.RegisterMessage(Mention)

BestMove = _reflection.GeneratedProtocolMessageType('BestMove', (_message.Message,), {
  'DESCRIPTOR' : _BESTMOVE,
  '__module__' : 'stockbird.protos.mentions_pb2'
  # @@protoc_insertion_point(class_scope:BestMove)
  })
_sym_db.RegisterMessage(BestMove)

StartGame = _reflection.GeneratedProtocolMessageType('StartGame', (_message.Message,), {
  'DESCRIPTOR' : _STARTGAME,
  '__module__' : 'stockbird.protos.mentions_pb2'
  # @@protoc_insertion_point(class_scope:StartGame)
  })
_sym_db.RegisterMessage(StartGame)


# @@protoc_insertion_point(module_scope)

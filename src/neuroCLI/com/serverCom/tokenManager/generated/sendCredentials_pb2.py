# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: sendCredentials.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'sendCredentials.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15sendCredentials.proto\x12\x1ctokenManager.sendCredentials\"2\n\x0fsendCredentials\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"J\n\x19VerifyCredentialsResponse\x12\x12\n\x05token\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0f\n\x07success\x18\x02 \x01(\x08\x42\x08\n\x06_token2\x97\x01\n\x18VerifyCredentialsService\x12{\n\x11verifyCredentials\x12-.tokenManager.sendCredentials.sendCredentials\x1a\x37.tokenManager.sendCredentials.VerifyCredentialsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sendCredentials_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SENDCREDENTIALS']._serialized_start=55
  _globals['_SENDCREDENTIALS']._serialized_end=105
  _globals['_VERIFYCREDENTIALSRESPONSE']._serialized_start=107
  _globals['_VERIFYCREDENTIALSRESPONSE']._serialized_end=181
  _globals['_VERIFYCREDENTIALSSERVICE']._serialized_start=184
  _globals['_VERIFYCREDENTIALSSERVICE']._serialized_end=335
# @@protoc_insertion_point(module_scope)
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/msp/msp_config.proto

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
  name='hfc/protos/msp/msp_config.proto',
  package='msp',
  syntax='proto3',
  serialized_pb=_b('\n\x1fhfc/protos/msp/msp_config.proto\x12\x03msp\")\n\tMSPConfig\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0e\n\x06\x63onfig\x18\x02 \x01(\x0c\"\x83\x03\n\x0f\x46\x61\x62ricMSPConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nroot_certs\x18\x02 \x03(\x0c\x12\x1a\n\x12intermediate_certs\x18\x03 \x03(\x0c\x12\x0e\n\x06\x61\x64mins\x18\x04 \x03(\x0c\x12\x17\n\x0frevocation_list\x18\x05 \x03(\x0c\x12\x32\n\x10signing_identity\x18\x06 \x01(\x0b\x32\x18.msp.SigningIdentityInfo\x12@\n\x1forganizational_unit_identifiers\x18\x07 \x03(\x0b\x32\x17.msp.FabricOUIdentifier\x12.\n\rcrypto_config\x18\x08 \x01(\x0b\x32\x17.msp.FabricCryptoConfig\x12\x16\n\x0etls_root_certs\x18\t \x03(\x0c\x12\x1e\n\x16tls_intermediate_certs\x18\n \x03(\x0c\x12+\n\x0f\x66\x61\x62ric_node_ous\x18\x0b \x01(\x0b\x32\x12.msp.FabricNodeOUs\"^\n\x12\x46\x61\x62ricCryptoConfig\x12\x1d\n\x15signature_hash_family\x18\x01 \x01(\t\x12)\n!identity_identifier_hash_function\x18\x02 \x01(\t\"~\n\x0fIdemixMSPConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03ipk\x18\x02 \x01(\x0c\x12*\n\x06signer\x18\x03 \x01(\x0b\x32\x1a.msp.IdemixMSPSignerConfig\x12\x15\n\rrevocation_pk\x18\x04 \x01(\x0c\x12\r\n\x05\x65poch\x18\x05 \x01(\x03\"\xa9\x01\n\x15IdemixMSPSignerConfig\x12\x0c\n\x04\x63red\x18\x01 \x01(\x0c\x12\n\n\x02sk\x18\x02 \x01(\x0c\x12&\n\x1eorganizational_unit_identifier\x18\x03 \x01(\t\x12\x0c\n\x04role\x18\x04 \x01(\x05\x12\x15\n\renrollment_id\x18\x05 \x01(\t\x12)\n!credential_revocation_information\x18\x06 \x01(\x0c\"R\n\x13SigningIdentityInfo\x12\x15\n\rpublic_signer\x18\x01 \x01(\x0c\x12$\n\x0eprivate_signer\x18\x02 \x01(\x0b\x32\x0c.msp.KeyInfo\"7\n\x07KeyInfo\x12\x16\n\x0ekey_identifier\x18\x01 \x01(\t\x12\x14\n\x0ckey_material\x18\x02 \x01(\x0c\"Q\n\x12\x46\x61\x62ricOUIdentifier\x12\x13\n\x0b\x63\x65rtificate\x18\x01 \x01(\x0c\x12&\n\x1eorganizational_unit_identifier\x18\x02 \x01(\t\"\x8b\x01\n\rFabricNodeOUs\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x12\x35\n\x14\x63lient_ou_identifier\x18\x02 \x01(\x0b\x32\x17.msp.FabricOUIdentifier\x12\x33\n\x12peer_ou_identifier\x18\x03 \x01(\x0b\x32\x17.msp.FabricOUIdentifierB_\n!org.hyperledger.fabric.protos.mspB\x10MspConfigPackageZ(github.com/hyperledger/fabric/protos/mspb\x06proto3')
)




_MSPCONFIG = _descriptor.Descriptor(
  name='MSPConfig',
  full_name='msp.MSPConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='msp.MSPConfig.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='msp.MSPConfig.config', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=81,
)


_FABRICMSPCONFIG = _descriptor.Descriptor(
  name='FabricMSPConfig',
  full_name='msp.FabricMSPConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='msp.FabricMSPConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='root_certs', full_name='msp.FabricMSPConfig.root_certs', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intermediate_certs', full_name='msp.FabricMSPConfig.intermediate_certs', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='admins', full_name='msp.FabricMSPConfig.admins', index=3,
      number=4, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revocation_list', full_name='msp.FabricMSPConfig.revocation_list', index=4,
      number=5, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signing_identity', full_name='msp.FabricMSPConfig.signing_identity', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizational_unit_identifiers', full_name='msp.FabricMSPConfig.organizational_unit_identifiers', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='crypto_config', full_name='msp.FabricMSPConfig.crypto_config', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tls_root_certs', full_name='msp.FabricMSPConfig.tls_root_certs', index=8,
      number=9, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tls_intermediate_certs', full_name='msp.FabricMSPConfig.tls_intermediate_certs', index=9,
      number=10, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fabric_node_ous', full_name='msp.FabricMSPConfig.fabric_node_ous', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=471,
)


_FABRICCRYPTOCONFIG = _descriptor.Descriptor(
  name='FabricCryptoConfig',
  full_name='msp.FabricCryptoConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature_hash_family', full_name='msp.FabricCryptoConfig.signature_hash_family', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identity_identifier_hash_function', full_name='msp.FabricCryptoConfig.identity_identifier_hash_function', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=473,
  serialized_end=567,
)


_IDEMIXMSPCONFIG = _descriptor.Descriptor(
  name='IdemixMSPConfig',
  full_name='msp.IdemixMSPConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='msp.IdemixMSPConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipk', full_name='msp.IdemixMSPConfig.ipk', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signer', full_name='msp.IdemixMSPConfig.signer', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revocation_pk', full_name='msp.IdemixMSPConfig.revocation_pk', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epoch', full_name='msp.IdemixMSPConfig.epoch', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=569,
  serialized_end=695,
)


_IDEMIXMSPSIGNERCONFIG = _descriptor.Descriptor(
  name='IdemixMSPSignerConfig',
  full_name='msp.IdemixMSPSignerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cred', full_name='msp.IdemixMSPSignerConfig.cred', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sk', full_name='msp.IdemixMSPSignerConfig.sk', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizational_unit_identifier', full_name='msp.IdemixMSPSignerConfig.organizational_unit_identifier', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='msp.IdemixMSPSignerConfig.role', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enrollment_id', full_name='msp.IdemixMSPSignerConfig.enrollment_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='credential_revocation_information', full_name='msp.IdemixMSPSignerConfig.credential_revocation_information', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=698,
  serialized_end=867,
)


_SIGNINGIDENTITYINFO = _descriptor.Descriptor(
  name='SigningIdentityInfo',
  full_name='msp.SigningIdentityInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_signer', full_name='msp.SigningIdentityInfo.public_signer', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private_signer', full_name='msp.SigningIdentityInfo.private_signer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=869,
  serialized_end=951,
)


_KEYINFO = _descriptor.Descriptor(
  name='KeyInfo',
  full_name='msp.KeyInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_identifier', full_name='msp.KeyInfo.key_identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_material', full_name='msp.KeyInfo.key_material', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=953,
  serialized_end=1008,
)


_FABRICOUIDENTIFIER = _descriptor.Descriptor(
  name='FabricOUIdentifier',
  full_name='msp.FabricOUIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='certificate', full_name='msp.FabricOUIdentifier.certificate', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizational_unit_identifier', full_name='msp.FabricOUIdentifier.organizational_unit_identifier', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1010,
  serialized_end=1091,
)


_FABRICNODEOUS = _descriptor.Descriptor(
  name='FabricNodeOUs',
  full_name='msp.FabricNodeOUs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable', full_name='msp.FabricNodeOUs.enable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_ou_identifier', full_name='msp.FabricNodeOUs.client_ou_identifier', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peer_ou_identifier', full_name='msp.FabricNodeOUs.peer_ou_identifier', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1094,
  serialized_end=1233,
)

_FABRICMSPCONFIG.fields_by_name['signing_identity'].message_type = _SIGNINGIDENTITYINFO
_FABRICMSPCONFIG.fields_by_name['organizational_unit_identifiers'].message_type = _FABRICOUIDENTIFIER
_FABRICMSPCONFIG.fields_by_name['crypto_config'].message_type = _FABRICCRYPTOCONFIG
_FABRICMSPCONFIG.fields_by_name['fabric_node_ous'].message_type = _FABRICNODEOUS
_IDEMIXMSPCONFIG.fields_by_name['signer'].message_type = _IDEMIXMSPSIGNERCONFIG
_SIGNINGIDENTITYINFO.fields_by_name['private_signer'].message_type = _KEYINFO
_FABRICNODEOUS.fields_by_name['client_ou_identifier'].message_type = _FABRICOUIDENTIFIER
_FABRICNODEOUS.fields_by_name['peer_ou_identifier'].message_type = _FABRICOUIDENTIFIER
DESCRIPTOR.message_types_by_name['MSPConfig'] = _MSPCONFIG
DESCRIPTOR.message_types_by_name['FabricMSPConfig'] = _FABRICMSPCONFIG
DESCRIPTOR.message_types_by_name['FabricCryptoConfig'] = _FABRICCRYPTOCONFIG
DESCRIPTOR.message_types_by_name['IdemixMSPConfig'] = _IDEMIXMSPCONFIG
DESCRIPTOR.message_types_by_name['IdemixMSPSignerConfig'] = _IDEMIXMSPSIGNERCONFIG
DESCRIPTOR.message_types_by_name['SigningIdentityInfo'] = _SIGNINGIDENTITYINFO
DESCRIPTOR.message_types_by_name['KeyInfo'] = _KEYINFO
DESCRIPTOR.message_types_by_name['FabricOUIdentifier'] = _FABRICOUIDENTIFIER
DESCRIPTOR.message_types_by_name['FabricNodeOUs'] = _FABRICNODEOUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MSPConfig = _reflection.GeneratedProtocolMessageType('MSPConfig', (_message.Message,), dict(
  DESCRIPTOR = _MSPCONFIG,
  __module__ = 'hfc.protos.msp.msp_config_pb2'
  # @@protoc_insertion_point(class_scope:msp.MSPConfig)
  ))
_sym_db.RegisterMessage(MSPConfig)

FabricMSPConfig = _reflection.GeneratedProtocolMessageType('FabricMSPConfig', (_message.Message,), dict(
  DESCRIPTOR = _FABRICMSPCONFIG,
  __module__ = 'hfc.protos.msp.msp_config_pb2'
  # @@protoc_insertion_point(class_scope:msp.FabricMSPConfig)
  ))
_sym_db.RegisterMessage(FabricMSPConfig)

FabricCryptoConfig = _reflection.GeneratedProtocolMessageType('FabricCryptoConfig', (_message.Message,), dict(
  DESCRIPTOR = _FABRICCRYPTOCONFIG,
  __module__ = 'hfc.protos.msp.msp_config_pb2'
  # @@protoc_insertion_point(class_scope:msp.FabricCryptoConfig)
  ))
_sym_db.RegisterMessage(FabricCryptoConfig)

IdemixMSPConfig = _reflection.GeneratedProtocolMessageType('IdemixMSPConfig', (_message.Message,), dict(
  DESCRIPTOR = _IDEMIXMSPCONFIG,
  __module__ = 'hfc.protos.msp.msp_config_pb2'
  # @@protoc_insertion_point(class_scope:msp.IdemixMSPConfig)
  ))
_sym_db.RegisterMessage(IdemixMSPConfig)

IdemixMSPSignerConfig = _reflection.GeneratedProtocolMessageType('IdemixMSPSignerConfig', (_message.Message,), dict(
  DESCRIPTOR = _IDEMIXMSPSIGNERCONFIG,
  __module__ = 'hfc.protos.msp.msp_config_pb2'
  # @@protoc_insertion_point(class_scope:msp.IdemixMSPSignerConfig)
  ))
_sym_db.RegisterMessage(IdemixMSPSignerConfig)

SigningIdentityInfo = _reflection.GeneratedProtocolMessageType('SigningIdentityInfo', (_message.Message,), dict(
  DESCRIPTOR = _SIGNINGIDENTITYINFO,
  __module__ = 'hfc.protos.msp.msp_config_pb2'
  # @@protoc_insertion_point(class_scope:msp.SigningIdentityInfo)
  ))
_sym_db.RegisterMessage(SigningIdentityInfo)

KeyInfo = _reflection.GeneratedProtocolMessageType('KeyInfo', (_message.Message,), dict(
  DESCRIPTOR = _KEYINFO,
  __module__ = 'hfc.protos.msp.msp_config_pb2'
  # @@protoc_insertion_point(class_scope:msp.KeyInfo)
  ))
_sym_db.RegisterMessage(KeyInfo)

FabricOUIdentifier = _reflection.GeneratedProtocolMessageType('FabricOUIdentifier', (_message.Message,), dict(
  DESCRIPTOR = _FABRICOUIDENTIFIER,
  __module__ = 'hfc.protos.msp.msp_config_pb2'
  # @@protoc_insertion_point(class_scope:msp.FabricOUIdentifier)
  ))
_sym_db.RegisterMessage(FabricOUIdentifier)

FabricNodeOUs = _reflection.GeneratedProtocolMessageType('FabricNodeOUs', (_message.Message,), dict(
  DESCRIPTOR = _FABRICNODEOUS,
  __module__ = 'hfc.protos.msp.msp_config_pb2'
  # @@protoc_insertion_point(class_scope:msp.FabricNodeOUs)
  ))
_sym_db.RegisterMessage(FabricNodeOUs)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!org.hyperledger.fabric.protos.mspB\020MspConfigPackageZ(github.com/hyperledger/fabric/protos/msp'))
# @@protoc_insertion_point(module_scope)

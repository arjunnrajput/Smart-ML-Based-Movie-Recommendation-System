from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='input-config.proto',
  package='tensorflow_examples.lite.examples.recommendation.ml_v2.configs',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x12input-config.proto\x12>tensorflow_examples.lite.examples.recommendation.ml_v2.configs\"\xd9\x01\n\x07\x46\x65\x61ture\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x01 \x01(\t\x12\x61\n\x0c\x66\x65\x61ture_type\x18\x02 \x01(\x0e\x32K.tensorflow_examples.lite.examples.recommendation.ml_v2.configs.FeatureType\x12\x12\n\nvocab_name\x18\x03 \x01(\t\x12\x12\n\nvocab_size\x18\x04 \x01(\x03\x12\x15\n\rembedding_dim\x18\x05 \x01(\x03\x12\x16\n\x0e\x66\x65\x61ture_length\x18\x06 \x01(\x03\"\xcc\x01\n\x0c\x46\x65\x61tureGroup\x12Y\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32G.tensorflow_examples.lite.examples.recommendation.ml_v2.configs.Feature\x12\x61\n\x0c\x65ncoder_type\x18\x02 \x01(\x0e\x32K.tensorflow_examples.lite.examples.recommendation.ml_v2.configs.EncoderType\"\xc9\x02\n\x0bInputConfig\x12k\n\x15global_feature_groups\x18\x01 \x03(\x0b\x32L.tensorflow_examples.lite.examples.recommendation.ml_v2.configs.FeatureGroup\x12m\n\x17\x61\x63tivity_feature_groups\x18\x02 \x03(\x0b\x32L.tensorflow_examples.lite.examples.recommendation.ml_v2.configs.FeatureGroup\x12^\n\rlabel_feature\x18\x03 \x01(\x0b\x32G.tensorflow_examples.lite.examples.recommendation.ml_v2.configs.Feature*-\n\x0b\x46\x65\x61tureType\x12\n\n\x06STRING\x10\x00\x12\x07\n\x03INT\x10\x01\x12\t\n\x05\x46LOAT\x10\x02*)\n\x0b\x45ncoderType\x12\x07\n\x03\x42OW\x10\x00\x12\x07\n\x03\x43NN\x10\x01\x12\x08\n\x04LSTM\x10\x02'
)

_FEATURETYPE = _descriptor.EnumDescriptor(
  name='FeatureType',
  full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.FeatureType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=845,
  serialized_end=890,
)
_sym_db.RegisterEnumDescriptor(_FEATURETYPE)

FeatureType = enum_type_wrapper.EnumTypeWrapper(_FEATURETYPE)
_ENCODERTYPE = _descriptor.EnumDescriptor(
  name='EncoderType',
  full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.EncoderType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOW', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CNN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LSTM', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=892,
  serialized_end=933,
)
_sym_db.RegisterEnumDescriptor(_ENCODERTYPE)

EncoderType = enum_type_wrapper.EnumTypeWrapper(_ENCODERTYPE)
STRING = 0
INT = 1
FLOAT = 2
BOW = 0
CNN = 1
LSTM = 2



_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_name', full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.Feature.feature_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_type', full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.Feature.feature_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vocab_name', full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.Feature.vocab_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vocab_size', full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.Feature.vocab_size', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='embedding_dim', full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.Feature.embedding_dim', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_length', full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.Feature.feature_length', index=5,
      number=6, type=3, cpp_type=2, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=304,
)


_FEATUREGROUP = _descriptor.Descriptor(
  name='FeatureGroup',
  full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.FeatureGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.FeatureGroup.features', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoder_type', full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.FeatureGroup.encoder_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=511,
)


_INPUTCONFIG = _descriptor.Descriptor(
  name='InputConfig',
  full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.InputConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='global_feature_groups', full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.InputConfig.global_feature_groups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activity_feature_groups', full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.InputConfig.activity_feature_groups', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label_feature', full_name='tensorflow_examples.lite.examples.recommendation.ml_v2.configs.InputConfig.label_feature', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=514,
  serialized_end=843,
)

_FEATURE.fields_by_name['feature_type'].enum_type = _FEATURETYPE
_FEATUREGROUP.fields_by_name['features'].message_type = _FEATURE
_FEATUREGROUP.fields_by_name['encoder_type'].enum_type = _ENCODERTYPE
_INPUTCONFIG.fields_by_name['global_feature_groups'].message_type = _FEATUREGROUP
_INPUTCONFIG.fields_by_name['activity_feature_groups'].message_type = _FEATUREGROUP
_INPUTCONFIG.fields_by_name['label_feature'].message_type = _FEATURE
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['FeatureGroup'] = _FEATUREGROUP
DESCRIPTOR.message_types_by_name['InputConfig'] = _INPUTCONFIG
DESCRIPTOR.enum_types_by_name['FeatureType'] = _FEATURETYPE
DESCRIPTOR.enum_types_by_name['EncoderType'] = _ENCODERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), {
  'DESCRIPTOR' : _FEATURE,
  '__module__' : 'input_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_examples.lite.examples.recommendation.ml_v2.configs.Feature)
  })
_sym_db.RegisterMessage(Feature)

FeatureGroup = _reflection.GeneratedProtocolMessageType('FeatureGroup', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREGROUP,
  '__module__' : 'input_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_examples.lite.examples.recommendation.ml_v2.configs.FeatureGroup)
  })
_sym_db.RegisterMessage(FeatureGroup)

InputConfig = _reflection.GeneratedProtocolMessageType('InputConfig', (_message.Message,), {
  'DESCRIPTOR' : _INPUTCONFIG,
  '__module__' : 'input_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_examples.lite.examples.recommendation.ml_v2.configs.InputConfig)
  })
_sym_db.RegisterMessage(InputConfig)


# @@protoc_insertion_point(module_scope)
# pyformat: enable

 
"""Tests for label_encoder."""
import tensorflow as tf

from configs import input_config_generated_pb2 as input_config_pb2
from model import label_encoder


class LabelEncoderTest(tf.test.TestCase):

  def _create_test_input_config(self):
    """Generate test input_config_pb2.InputConfig proto."""
    feature_context_movie_id = input_config_pb2.Feature(
        feature_name='context_movie_id',
        feature_type=input_config_pb2.FeatureType.INT,
        vocab_size=3952,
        embedding_dim=4)
    feature_context_movie_rating = input_config_pb2.Feature(
        feature_name='context_movie_rating',
        feature_type=input_config_pb2.FeatureType.FLOAT)
    feature_group_1 = input_config_pb2.FeatureGroup(
        features=[feature_context_movie_id, feature_context_movie_rating],
        encoder_type=input_config_pb2.EncoderType.BOW)

    feature_label = input_config_pb2.Feature(
        feature_name='label_movie_id',
        feature_type=input_config_pb2.FeatureType.INT,
        vocab_size=3952,
        embedding_dim=4)

    input_config = input_config_pb2.InputConfig(
        activity_feature_groups=[feature_group_1],
        label_feature=feature_label)
    return input_config

  def test_label_encoder(self):
    input_config = self._create_test_input_config()
    input_label_encoder = label_encoder.LabelEncoder(
        input_config=input_config)
    input_label_movie_id = tf.constant([[1], [2]])
    inputs = {
        'label_movie_id': input_label_movie_id
    }
    label_embedding = input_label_encoder(inputs)
    print(label_embedding.shape)
    self.assertAllEqual([2, 4], list(label_embedding.shape))

if __name__ == '__main__':
  tf.test.main()

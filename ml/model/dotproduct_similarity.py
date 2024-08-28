
"""Dotproduct similarity layer."""
from typing import Optional

import tensorflow as tf


class DotProductSimilarity(tf.keras.layers.Layer):
  """Layer to comput dotproduct similarities for context/label embedding.

    The top_k is an integer to represent top_k ids to compute among label ids.
    if top_k is None, top_k computation will be ignored.
  """

  def call(self,
           context_embeddings: tf.Tensor,
           label_embeddings: tf.Tensor,
           top_k: Optional[int] = None):
    """Generate dotproduct similarity matrix and top values/indices.

    Args:
      context_embeddings: Context embeddings generated with input context
        sequence. The shape of tensor should be [batch_size, embedding_dim] for
        training mode, and [1, embedding_dim] for inference mode.
      label_embeddings: Label embeddings generated for candidate label items.
        The shape of tensor should be [num_items, embedding_dim].
      top_k: The number of top values to compute. If it's not set, top values
        and indices will not be computed.

    Returns:
      Dotproduct similarity matrix with shape [num_label_items, 1] and top
      values/indices if top_k is set.
    """
    if tf.keras.backend.ndim(label_embeddings) == 3:
      label_embeddings = tf.squeeze(label_embeddings, 1)
    dotproduct = tf.matmul(
        context_embeddings, label_embeddings, transpose_b=True)
    if top_k:
      top_values, top_indices = tf.math.top_k(
          tf.squeeze(dotproduct), top_k, sorted=True)
      top_ids = tf.identity(top_indices, name='top_prediction_ids')
      top_scores = tf.identity(
          tf.math.sigmoid(top_values), name='top_prediction_scores')
      return [dotproduct, top_ids, top_scores]
    else:
      return [dotproduct]

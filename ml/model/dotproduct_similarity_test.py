
"""Tests for dotproduct_similarity."""
import tensorflow as tf

from model import dotproduct_similarity


class DotproductSimilarityTest(tf.test.TestCase):

  def test_dotproduct(self):
    context_embeddings = tf.constant([[0.1, 0.1, 0.1, 0.1],
                                      [0.2, 0.2, 0.2, 0.2]])
    label_embeddings = tf.constant([[0.1, 0.1, 0.1, 0.1], [0.1, 0.1, 0.1, 0.1]])
    similarity_layer = dotproduct_similarity.DotProductSimilarity()
    dotproduct = similarity_layer(context_embeddings, label_embeddings)
    dotproduct, top_ids, top_scores = similarity_layer(context_embeddings,
                                                       label_embeddings, 1)
    self.assertAllClose(tf.constant([[0.04, 0.04], [0.08, 0.08]]), dotproduct)
    self.assertAllEqual(tf.constant([[0], [0]]), top_ids)
    self.assertAllEqual([2, 1], list(top_scores.shape))

if __name__ == '__main__':
  tf.test.main()

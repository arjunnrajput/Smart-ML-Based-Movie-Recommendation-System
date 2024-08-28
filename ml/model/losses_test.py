 
"""Tests for the keras losses."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from model import losses


class KerasLossesTest(tf.test.TestCase):

  def test_batch_softmax_loss(self):
    batch_softmax = losses.BatchSoftmax()
    true_label = tf.constant([[2], [0], [1]], dtype=tf.int32)
    logits = tf.constant([
        [0.8, 0.1, 0.2, 0.3],
        [0.2, 0.7, 0.1, 0.5],
        [0.5, 0.4, 0.9, 0.2]
    ], dtype=tf.float32)
    self.assertBetween(
        batch_softmax.call(y_true=true_label, y_pred=logits).numpy(),
        1.3, 1.4)

  def test_global_softmax_loss(self):
    global_softmax = losses.GlobalSoftmax()
    true_label = tf.constant([[2], [0], [1]], dtype=tf.int32)
    logits = tf.constant([
        [0.8, 0.1, 0.2, 0.3],
        [0.2, 0.7, 0.1, 0.5],
        [0.5, 0.4, 0.9, 0.2]
    ], dtype=tf.float32)
    self.assertBetween(
        global_softmax.call(y_true=true_label, y_pred=logits).numpy(), 1.5, 1.6)


if __name__ == '__main__':
  tf.test.main()

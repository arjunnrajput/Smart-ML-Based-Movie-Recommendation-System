
"""Class to hold model architecture configuration."""
from typing import List
import attr


@attr.s(auto_attribs=True)
class ModelConfig(object):
  """Class to hold parameters for model architecture configuration.

  Attributes:
      hidden_layer_dims: List of hidden layer dimensions.
      eval_top_k: Top k to evaluate.
      conv_num_filter_ratios: Number of filter ratios for the Conv1D layer.
      conv_kernel_size: Size of the Conv1D layer kernel size.
      lstm_num_units: Number of units for the LSTM layer.
      num_predictions: Number of predictions to return with serving mode, which
      has default value 10.
  """
  hidden_layer_dims: List[int]
  eval_top_k: List[int]
  conv_num_filter_ratios: List[int]
  conv_kernel_size: int
  lstm_num_units: int
  num_predictions: int = 10

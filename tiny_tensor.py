# This is a toy implementation of an autodiff library
# with an API similar to PyTorch. Tensor data is stored 
# internally as numpy arrays.

import numpy as np


class TinyTensor():
  """
  A TinyTensor is a tensor object that holds:
    - data: a numpy array
    - grad: the local gradient of the tensor w.r.t. the graph
    - requires_grad: a boolean value dictating whether a 
                     gradient should be tracked for self
    - prev_op: the previous operation that resulted in self

    All operations, built-in or otherwise, result in a new
    TinyTensor object with its 'data' field containing the
    result of the subsequent operation.
  """
  def __init__(self,
               data,
               grad=None,
               requires_grad=True,
               prev_op=None):
    
    if not (isinstance(data, np.ndarray) or
            isinstance(data, int) or
            isinstance(data, float)):
      raise Exception("Data Value Error")
    else:
       self.data = np.array(data)
    
    self.data = data
    self.grad = grad
    self.requires_grad = requires_grad
    self.prev_op = prev_op

  ######################
  # Built-in Operators #
  ######################

  def __add__(self, right):
    pass

  def __radd__(self, right):
    pass

  def __sub__(self, right):
    pass

  def __mul__(self, right):
    pass

  def __truediv__(self, right):
    pass

  def __pow__(self, right):
    pass

  def __repr__(self):
    return {"data": self.data,\
            "grad": self.grad,\
            "requires_grad": self.requires_grad,\
            "prev_op": self.prev_op}

  def __str__(self):
    return f"TinyTensor(data={self.data},\
            grad={self.grad},\
            requires_grad={self.requires_grad},\
            prev_op={self.prev_op})"

  #########################
  # TinyTensor Operations #
  #########################
  
  def dot(self):
    pass

  def exp(self):
    pass

  def max(self):
    pass

  def log(self, base=np.e):
    pass


if __name__ == "__main__":
  a = np.array([1, 2, 3])
  print(isinstance(a, np.ndarray))
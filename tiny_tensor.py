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
                     (defaults to 'True')
    - prev_op: the previous operation that resulted in self

    All operations, built-in or otherwise, result in a new
    TinyTensor object with its 'data' field containing the
    result of the subsequent operation.


  """
  def __init__(self,
               data=[],
               grad=None,
               requires_grad=True,
               prev_op=None):
    
    if isinstance(data, np.ndarray):
      self.data = data
    elif (isinstance(data, float) or
          isinstance(data, int) or
          isinstance(data, list)):
      self.data = np.array(data)
    else:
      raise TypeError("TinyTensor data must be initialized " +
                      "with a value of type: int, float, " +
                      "list, or np.array")
    
    self.data = data
    self.grad = grad
    self.requires_grad = requires_grad
    self.prev_op = prev_op

  #####################################
  # Built-in Operators for TinyTensor # 
  #####################################

  def __add__(self, right):
    pass

  def __radd__(self, left):
    self.__add__(left)

  def __sub__(self, right):
    pass

  def __rsub__(self, left):
    self.__sub__(left)

  def __mul__(self, right):
    pass

  def __rmul__(self, left):
    self.__mul__(left)

  def __truediv__(self, right):
    pass

  def __rtruediv__(self, left):
    pass

  def __pow__(self, right):
    pass

  def __imul__(self, right):
    pass

  def __iadd__(self, right):
    pass

  def __isub__(self, right):
    pass

  def __itruediv(self, right):
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

  #################################
  # TinyTensor Interal Operations #
  #################################

  def dot(self, right):
    if not isinstance(right, TinyTensor):
      raise TypeError("Arguments must be of type TinyTensor")

  def backward(self):
    pass


##################################
# TinyTensor External Operations #
##################################

def dot(left, right):
  if not (isinstance(right, TinyTensor) and
          isinstance(left, TinyTensor)):
    raise TypeError("Arguments must be of type TinyTensor")

def exp(tensor):
  if not isinstance(tensor, TinyTensor):
      raise TypeError("Arguments must be of type TinyTensor")

def max(**kwargs):
  pass

def log(tensor, base=np.e):
  if not isinstance(tensor, TinyTensor):
      raise TypeError("Arguments must be of type TinyTensor")

def sin(tensor):
  if not isinstance(tensor, TinyTensor):
      raise TypeError("Arguments must be of type TinyTensor")

def cos(tensor):
  if not isinstance(tensor, TinyTensor):
      raise TypeError("Arguments must be of type TinyTensor")
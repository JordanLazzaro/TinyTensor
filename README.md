# TinyTensor
TinyTensor is a toy implementation of an Automatic Differentiation library
made with the goal of gaining a deeper understanding of how libraries like
[PyTorch](https://github.com/pytorch/pytorch) and
[Tensorflow](https://github.com/tensorflow/tensorflow) compute gradients.

## What is an Automatic Differentiation Library?
[Automatic Differentiation](https://en.wikipedia.org/wiki/Automatic_differentiation),
or "AutoDiff", is a way of splitting up numeric operations into a set of atomic units
such that the derivatives (or gradients in the case of tensors) of those units can be
computed locally.

With these atomic units as building blocks, we can construct a computational
graph (taking the form of a
[Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)) to
represent more complex operations. We can then, using the chain rule, compute the
gradients of the constituent atomic units w.r.t. the final output of the graph in a
process known as [Back-Propagation](https://en.wikipedia.org/wiki/Backpropagation).

These gradients, of course, are then used to perform updates on their associated
tensors (which generally represent the parameters of a Machine Learning model) in
the process of training by various update rules such as [SGD](https://en.wikipedia.org/wiki/Stochastic_gradient_descent).

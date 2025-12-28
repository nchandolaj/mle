'''
torchvision.datasets.MNIST
'''
import numpy as np
import torch
import torchvision


def sigmoid(z):
    '''
    Activation function
    z is a vector or Numpy array
    '''
    return 1.0 / (1.0 + np.exp(-z))


class Network(object):

  def __init__(self, sizes):
    '''
    sizes: number of neurons in the respective layers, e.g. [2, 3,  1], 
           i.e., 2 neuron in the first (input) layer, 3 neurons in the second layer, 
           and 1 neuron in the third (final) layer
    '''
    self.num_layers = len(sizes)
    self.sizes = sizes
    
    # np.random.randn() - generate Gaussian distributions with mean 0 and std dev 1
    # First layer is input layer. Hence, we omit any biases.
    self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
    self.weights = [np.random.randn(y, x)
                    for x, y in zip(sizes[:-1], sizes[1:])]
             

  def feedforward(self, a):
    '''
    Return the output of the network if 'a' is input.
    '''
    for b, w in zip(self.biases, self.weights):
      a = sigmoid (np.dot(w, a) + b)
    return a


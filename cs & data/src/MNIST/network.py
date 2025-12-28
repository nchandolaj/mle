'''
torchvision.datasets.MNIST
'''
import numpy as np
import random 

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


  def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
    ''' 
    Train the neural network using mini-batch stochastic gradient descent.
    Input: 
      training_data - a list of tuples "(x, y)"
      eta - learning rate
    '''
    # test_Data is an optional argument
    if test_data: n_test = len(test_data)

    n = len(training_data)
    
    # epoch loop
    for j in xrange(epochs):

      # good to shuffle training data
      random.shuffle(training_data)
      
      #form mini btaches for training / SGD
      mini_batches = [
        training_data[k: k + mini_batch_size]
        for k in xrange(0, n, mini_batch_size)
      ]

      for mini_batch in mini_batches:
        self.update_mini_batch(mini_batch, eta)
      
      if test_data:
        print "Epoch {0}: {1} {2}".format(
          j, self.evaluate(test_data), n_test
        )
      else:
        print "Epoch {0} complete".format(j)
      
  def update_mini_batch(self, mini_batch, eta):
    '''
    Update network's parameters - weights & biases by applying 
    gradient descent using backpropagation to a single mini-batch.
    Input:
      mini_batch - list of tuples "(x, y)"
      eta - learning rate
    '''
    nabla_b = [np.zeros(b.shape) for b in self.biases]
    nabla_w = [np.zeros(w.shape) for w in self.weights]
    
    # loop with individual items withion mini_batch
    for x, y in mini_batch:

      # get gradient
      delta_nabla_b, delta_nabla_w = self.backprop(x, y)

      # maintain a list of biases and weights for each item within batch
      nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
      nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
    
    # update parameters once for each mini batch
    self.weights = [w - (eta/len(mini_batch)) * nw 
                    for w, nw in zip(self.weights, nabla_w)]
    self.biases = [b - (eta/len(mini_batch)) * nb 
                    for b, nb in zip(self.biases, nabla_b)]
    
  def backprop(self, x, y):
    '''
    Return a tuple ``(nabla_b, nable_w)`` representing the gradient
    '''
    nable_b = [np.zeros(b.shape) for b in self.biases]
    nable_w = [np.zeros(w.shape) for w in self.weights]

    #feedforward
    activation = x
    activations = [x] # for all layers

    zs = [] # list of z vectors

    for b, w in zip(self.biases, self.weights):
      z = np.dot(w, )

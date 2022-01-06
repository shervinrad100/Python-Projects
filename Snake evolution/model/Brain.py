# BUG
# the network_shape is misunderstood because you get an error on line 28
# TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

import random
import numpy as np


class Brain():
    """
     The brain can make a decision to turn left or right or go straight (output shape should always be 3)
    """
    
    chosen_colours = set()
    
    def __init__(self, network_shape, output='tanh'):
        """
        network shape is a list of tuples of length 2 representing layer information input and output shapes. I.e.
            network_shape = [(1,12),(12,12),(12,1)] is a 3 layer network. 
        First layer has 1 input and 12 outputs, second is 12 inputs and outputs and last layer has 12 inputs and a single output
        """
        self.colour = Brain.set_colour()
        # create network structure
        self.weights, self.biases = [], []
        self.output = Brain._activation(output)
        # initialise the weights (Glorot Normal initialisation as a factor of shape)
        for i in range(len(network_shape)-1):
            shape = (network_shape[i], network_shape[i+1])
            std = np.sqrt(2 / sum(shape))
            weights = np.random.normal(0, std, shape)
            bias = np.random.normal(0, std, (1,  network_shape[i+1])) 
            self.weights.append(weights)
            self.biases.append(bias)
 
    @staticmethod
    def set_colour():
        col = tuple(random.randint(0,25) *10 for _ in range(3)) 
        while Brain.chosen_colours.intersection(set(col)):
            col = tuple(random.randint(0,25) *10 for _ in range(3)) 
        return col       

    @staticmethod
    def _activation(type):
        if type == "softmax":
            return lambda X : np.exp(X) / np.sum(np.exp(X), axis=1).reshape(-1, 1)
        elif type == "tanh":
            return lambda X: np.tanh(np.sum(X))
        elif type == 'sigmoid':
            return lambda X : (1 / (1 + np.exp(-X)))
        else:
            raise ValueError('Invalid activation. Select from ["softmax", "sigmoid", "tanh"]') 

    def predict(self, X):
        """
        input a numpy ndarray 
        X must have ndim == 2 first dimension being the input and 2nd being the output
        """
        # if processing hidden layers, input shape must match layer inputs
        if X.ndim != 2:
            raise ValueError("Input has dimensions {}. Expected X.ndim == 2".format(X.ndim))
        # if processing input layer, input shape must match input layer dimensions
        if X.shape[1] != self.weights[0].shape[0]:
            raise ValueError('Input has {} features, expected {}'.format(X.shape[1], self.weights[0].shape[0]))
        for i, (weights, bias) in enumerate(zip(self.weights, self.biases)):
            X = np.dot(X, weights) + np.dot(np.ones(X.shape[0], 1), bias) # X = X.W + B
            if i == len(self.weights) - 1:
                X = self.output(X) # _activation(type)
            else:
                X = max(0,X) # ReLU
        return np.argmax(X, axis=1).reshape((-1, 1))

    def mutate(self, mutation_std=0.05):
        """Mutate the Brain's weights in place."""
        for i in range(len(self.weights)):
            self.weights[i] += np.random.normal(0, mutation_std, self.weights[i].shape)
            self.biases[i] += np.random.normal(0, mutation_std, self.biases[i].shape)

    def see(self):
        pass
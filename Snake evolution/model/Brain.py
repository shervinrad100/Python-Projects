# BUG
# why matrix mismatch? output seems to be just one number?
# what if decision has two numbers that are max? 
# TODO
# ValueError to explain why matrix dimensions dont match

import random
import numpy as np


class Brain:
    """
     The brain can make a decision to turn left or right or go straight (output shape should always be 3)
    """
    
    chosen_colours = set()
    
    def __init__(self, network_shape, activation_function='tanh'):
        """
        Class will initialise with a network shape as a list of integers representing number of nodes in each layer. 
        I.e. network_shape = [6,12,3] is a 3 layer network with 6, 12 and 3 neurons in each layer respectively.
        """
        self.colour = Brain.set_colour()
        # create network structure
        self.network_shape = network_shape
        self.weights, self.biases = [], []
        self.output = Brain._activation(activation_function)
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
        if type == "softmax": # needs to be checked 
            return lambda X : np.exp(X) / np.sum(np.exp(X), axis=1).reshape(-1, 1)
        elif type == "tanh":
            return lambda X: np.tanh(X)
        elif type == 'sigmoid':
            return lambda X : (1 / (1 + np.exp(-X)))
        else:
            raise ValueError('Invalid activation. Select from ["softmax", "sigmoid", "tanh"]')

    def decision(self, X):
        """
        X is a numpy array with shape (1,network_shape[0]) that will be fed through the network
        output will be a tuple of len(network_shape[-1])
        
        """
        for i, (W, B) in enumerate(zip(self.weights, self.biases)):
            try:
                X = np.dot(X, W) + B 
            except ValueError:
                print("Matrix Shape mismatch")
            if i == len(self.weights) - 1:
                X = self.output(X).reshape(-1) # _activation(type)
            else:
                X = np.clip(X, 0, np.inf) # ReLU
        return [0 if i != max(X) else 1 for i in X] 

    def mutate(self, mutation_std=0.05):
        """Mutate the Brain's weights in place."""
        for i in range(len(self.weights)):
            self.weights[i] += np.random.normal(0, mutation_std, self.weights[i].shape)
            self.biases[i] += np.random.normal(0, mutation_std, self.biases[i].shape)

    def see(self, food=True, lethal=False):
        food_coord, lethal_coord = None, None
        if not lethal_coord == None:
            return np.array([*food_coord, *lethal_coord]).reshape(1,self.network_shape[0])
        else:
            return np.array(food_coord).reshape(1,self.network_shape[0])
        pass


# tests
# network_shape = [6,12,12,12,3]
# bren = Brain(network_shape)
# food_coord = (1,0,0)
# lethal_coord = (0,0,1)
# input = np.array([*food_coord, *lethal_coord]).reshape(1,network_shape[0])
# move = bren.decision(input)
# print(move)
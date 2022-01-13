# BUG 

# TODO
# make snake have sense of direction (move direction from game to snake)
# have snake output absolute matrix with directions instead of relative L,F,R
# make snake direction customisable
# implement print method for better logging

import random as rn
import pygame
import numpy as np

class Snake():
    """
    snake occupies a space from head to tail and cant go back on itself.
    """
    angles = (np.pi/2, 0, -np.pi/2)
    rotation_matrix = lambda phi: ((np.around(np.cos(phi), decimals=4), -np.sin(phi)),
                                    (np.sin(phi), np.around(np.cos(phi), decimals=4))) 
    rotation_2d = lambda phi, dxdy: np.dot(rotation_matrix(phi), np.transpose(dxdy))

    def __init__(self, world, init_len=1, init_pos=None, brain = None):
        """
        init with world object so that snake can spawn at a random location on that world
        body is a list of (x,y) coordinates
        if we want to initialise a snake with a larger body than 1 block it will spawn horizontally
        if you choose a length other than 1, it may be best to select initial spawn position (init_pos) so you dont go off grid
        """
        self.world = world
        if init_pos:
            x,y = init_pos
        else:
            x = rn.randint(world.width //2 - world.width//4, world.width //2 + world.width//4)
            y = rn.randint(world.height //2 - world.height//4, world.height //2 + world.height//4)
        self.periphery_relative = None
        self.direction = (1,0)
        self.body = []
        for i in range(0,init_len):
            self.body.append((x-i, y))
        self.alive = True
        self.length = len(self.body)
        self.brain = brain


    def grow(self):
        """
        grows snake size by 1
        """
        self.length += 1

    def move(self, dx, dy):                   
        """
        determines old head position and updates given a dierction
        """
        # get head position and update it 
        (x, y) = self.body[0] 
        x += dx 
        y += dy 
        # if snake has not grown we move the body otherwise we add 1 block to snake body
        if self.length == len(self.body):
            self.body.pop()
        self.body.insert(0,(x,y))
        # if snake is head is out of bounds or overlaps itself it dies
        if self.body[0] in self.body[1:]:
            self.alive = False
            return self.alive
        elif x < - self.world.blocksize//2 or y < - self.world.blocksize//2 or x > self.world.width or y > self.world.height:
            self.alive = False
            return self.alive
        else:
            return self.alive

    def see(self, food, worldwide=False):
        """
        will make the snake observe and returns a tuple with the direction of where the stimulus is
        when lethal = True it will return two tuples with the second being the direction of the lethal objects
        rotate direction eigenvector and if it collides with food return 1 for lethals return -1
        if worldwide vision then will return a flattened matrix of x,y coordinates each with len world.width, world.height
        """
        head_pos = self.body[0]
        if worldwide:
            xs, ys = np.zeros((self.world.width, self.world.height))
            xs[food.x], ys[food.y] = 1, 1
            xs[head_pos[0]], ys[head_pos[1]] = -1, -1
            return np.array([*xs, *ys]).reshape(1,self.brain.network_shape[0])
        # L,F,R directions relative to head direction
        self.periphery_relative = [Snake.rotation_2d(phi, self.direction) for phi in Snake.angles]
        # L,F,R directions absolute coordinates
        periphery_absolute = list(tuple(map(sum, zip(periphery, head_pos))) for periphery in self.periphery_relative)
        # L,F,R direction of food relative to head direction
        food_dir = [1 if  dxdy == (food.x, food.y) else 0 for dxdy in periphery_absolute]
        lethal_dir = [-1 if (dxdy in self.body) or # eat tail
                        (dxdy[0] >= self.world.width) or (dxdy[1] >= self.world.height) or # out of bounds
                        (dxdy[0] <= 0) or (dxdy[1]<= 0) # out of bounds
                        else 0 
                        for dxdy in periphery_absolute]
        return np.array([*food_dir, *lethal_dir]).reshape(1,self.brain.network_shape[0])


    def draw(self):
        """
        Draw the body of the snake.
        """
        size = self.world.blocksize
        self.head_rect = pygame.Rect(*self.body[0], size, size)
        for (x,y) in self.body:
            rect = pygame.Rect(x, y, size, size)
            pygame.draw.rect(self.world.window, (250,250,250), rect)
 
# from World import World
# from Brain import Brain
# from Food import Food
# werld = World(100,100)
# fewd = Food(werld)
# network_shape = [6,12,12,12,3]
# bren = Brain(network_shape)
# snek = Snake(werld, brain=bren)
# vision = snek.see(fewd)
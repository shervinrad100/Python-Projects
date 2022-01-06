# TODO
# make snake have sense of direction (move direction from game to snake)
# have snake or Brain check front/left/right for food/wall

import random as rn
import pygame

class Snake():
    """
    snake occupies a space from head to tail and cant go back on itself.
    """
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
        self.direction = None
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

    def draw(self):
        """
        Draw the body of the snake.
        """
        size = self.world.blocksize
        self.head_rect = pygame.Rect(*self.body[0], size, size)
        for (x,y) in self.body:
            rect = pygame.Rect(x, y, size, size)
            pygame.draw.rect(self.world.window, (250,250,250), rect)
 

            
import random as rn
import pygame

class Snake:
    """
    snake occupies a space from head to tail and cant go back on itself.
    """
    def __init__(self, world, init_len=1, init_pos=None, render=True):
        """
        init with world object so that snake can spawn at a random location on that world
        body is a list of (x,y) coordinates
        if we want to initialise a snake with a larger body than 1 block it will spawn horizontally
        if you choose a length other than 1, it may be best to select initial spawn position (init_pos) so you dont go off grid
        """
        self.world = world
        self.render = render
        if init_pos:
            x,y = init_pos
        else:
            x = rn.randint(world.width //2 - world.width//4, world.width //2 + world.width//4)
            y = rn.randint(world.height //2 - world.height//4, world.height //2 + world.height//4)

        self.body = []
        for i in range(0,init_len):
            self.body.append((x-i, y))
        
        self.length = len(self.body)


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
        if self.render:
            x += dx * self.world.blocksize
            y += dy * self.world.blocksize
        # if snake has not grown we move the body otherwise we add 1 block to snake body
        if self.length == len(self.body):
            self.body.pop()
        self.body.insert(0,(x,y))
        # if snake is head is out of bounds or overlaps itself it dies
        if self.body[0] in self.body[1:]:
            return False
        elif x < 0 or y < 0 or x > self.world.width or y > self.world.height:
            return False
        else:
            return True

    def draw(self):
        """
        Draw the body of the snake.
        """
        for (x,y) in self.body:
            size = self.world.blocksize
            rect = pygame.Rect(x, y, size, size)
            pygame.draw.rect(self.world.window, (250,250,250), rect)

 

            
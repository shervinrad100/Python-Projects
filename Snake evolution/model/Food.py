import random as rn 
import pygame

class Food():
    """
    only occupies one space and spawns randomly on a world
    """
    def __init__(self, world, blocksize=10):
        """init with world object"""
        self.world = world
        self.blocksize = blocksize
        self.x = rn.randint(0, world.width - blocksize)
        self.y = rn.randint(0, world.height - blocksize)

    def draw(self):
        size = self.world.blocksize
        self.rect = pygame.Rect(self.x, self.y, size, size)
        pygame.draw.rect(self.world.window, (250,0,0), self.rect)

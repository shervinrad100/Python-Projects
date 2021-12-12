import random as rn 

class Food():
    """
    only occupies one space and spawns randomly on a world
    """
    def __init__(self, world):
        """init with world object"""
        
        self.x = rn.randint(0, world.width - 1)
        self.y = rn.randint(0, world.length - 1)
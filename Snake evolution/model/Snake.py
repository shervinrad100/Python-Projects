import random as rn

class Snake:
    """
    snake occupies a space from head to tail and cant go back on itself.
    """
    def __init__(self, world, init_len=1, init_pos=None):
        """
        init with world object so that snake can spawn at a random location on that world
        body is a list of (x,y) coordinates
        if we want to initialise a snake with a larger body than 1 block it will spawn horizontally
        if you choose a length other than 1, it may be best to select initial spawn position (init_pos) so you dont go off grid
        """
        try:
            x,y = init_pos
        except:
            x = rn.randint(0, world.width - 1)
            y = rn.randint(0, world.length - 1)

        self.world = world
        self.body = []
        for i in range(0,init_len):
            self.body.append((x-i, y))
        self.length = len(self.body)
        
        self.DNA = ()
        self.brain = None

    def grow(self):
        """grows snake size by 1
        it will be called when snake movement overlaps it with food"""
        self.length += 1

    def move(self, dx, dy, food):                   
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
            return False
        elif x < 0 or y < 0 or x > self.world.width or y > self.world.height:
            return False
        else:
            return True
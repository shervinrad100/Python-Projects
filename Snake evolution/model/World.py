

class World:
    """
    the grid coordinates of our world
    """
    def __init__(self, window, width, height, blocksize, screen_colour=(0,0,0)):
        """init with a width and height"""
        self.window = window
        self.width = width
        self.height = height
        self.blocksize = blocksize

        self.screen_colour = screen_colour

    def draw(self):
        self.window.fill(self.screen_colour)
        
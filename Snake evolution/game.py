from model.Food import Food
from model.Snake import Snake
from model.World import World
import pygame
import time
import random
import sys
import json
import os


#####################
#  PARAMETERS
WHITE = (250,250,250)
RED = (250,0,0)
# RIGHT = (1 , 0)
# LEFT  = (-1, 0)
# UP    = (0 , 1)
# DOWN  = (0 ,-1)

# set up file dirs
try:
    if "savefiles" in os.listdir():
        with open("savefiles/highscore.txt", "r") as file:
            highscore = int(file.readline().strip())
    else:
        os.mkdir("savefiles")
except:
    highscore = 0

# read config from file
try:
    with open("config.txt", "r") as file:
        CONFIG = json.load(file)
except:
    CONFIG = {
    "window_x_lim": 500,
    "rendering": True,
    "window_y_lim": 300,
    "blocksize": 10,
    "snake_speed": 10,
    "fontsize" : 50    
}

score = 0
#####################

def render_text(window, txt, colour, loc=None, alpha=255):
    """
    render text on display window
    """
    txt_surf = font.render(txt, False, colour)
    txt_surf.set_alpha(alpha)
    
    if loc == "middle":
        rect_loc = txt_surf.get_rect(center = (world.width//2, world.height//2))
    elif loc == "topleft":
        rect_loc = txt_surf.get_rect(topleft = (10,10))

    if loc != None:
        window.blit(txt_surf, rect_loc)
    else:
        return txt_surf


def pause_screen(font, world):
    """
    pause the game and show global highscore
    """
    window.fill((120,120,120))
    render_text(window, "PAUSE", RED, "middle")
    render_text(window, "HIGHSCORE {}".format(highscore), WHITE, "topleft", alpha=127)
    pygame.display.update()
    fps.tick(CONFIG["snake_speed"])
    

def gameover_screen(font, window, score, highscore):
    """
    show gameover screen with highscore and player final score
    """
    surfaces = [render_text(window, "GAMEOVER", RED),
                render_text(window, "YOUR SCORE: {}".format(score), RED),
                render_text(window, "HIGHSCORE: {}".format(highscore), RED) ]
    rects = [surfaces[surf].get_rect(center = (world.width//2, surf*CONFIG["fontsize"]+CONFIG["fontsize"])) for surf in range(len(surfaces))]

    window.fill((120,120,120))
    for i in range(len(surfaces)):
        window.blit(surfaces[i], rects[i])

    pygame.display.update()
    fps.tick(CONFIG["snake_speed"])


# Initialising pygame
pygame.init()
pygame.display.set_caption('Snake')
window = pygame.display.set_mode((CONFIG["window_x_lim"], CONFIG["window_y_lim"]))
fps = pygame.time.Clock()
font = pygame.font.Font(None, CONFIG["fontsize"])

# init world 
world = World(CONFIG["window_x_lim"], CONFIG["window_y_lim"], CONFIG["blocksize"], window=window)
snake1 = Snake(world, init_len=1)
move_input = tuple(map(lambda dx: dx * CONFIG["blocksize"], snake1.direction))
food = Food(world, world.blocksize)

# main game loop
while True:
    # take inputs
    for event in pygame.event.get():
        # window close event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # user input 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_input = (0,-1 * world.blocksize)
            if event.key == pygame.K_DOWN:
                move_input = (0,1* world.blocksize)
            if event.key == pygame.K_LEFT:
                move_input = (-1* world.blocksize,0)
            if event.key == pygame.K_RIGHT:
                move_input = (1* world.blocksize,0)
            if event.key == pygame.K_ESCAPE:
                pause = True
                while pause:
                    pause_screen(font, world)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        # user input 
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                pause = False

    # draw world map, score, snake and food
    world.draw()
    render_text(window, "Score {}".format(str(score)), WHITE, "topleft", alpha=127)
    snake1.draw()
    food.draw()
    #pygame.draw.rect(window, RED, pygame.Rect(0, 0, 2*world.blocksize, world.height))

    # if vectors are orthogonal you can change direction else ignore
    if sum([x1y1*x2y2 for x1y1,x2y2 in list(zip(move_input, snake1.direction))]) == 0:
        snake1.direction = move_input

    # snake finds food
    snakehead = snake1.body[0]
    if snake1.body[0] == (food.x, food.y) or food.rect.colliderect(snake1.head_rect):
        snake1.grow()
        food = Food(world, world.blocksize)
        score += 1

	# Moving the snake
    if not snake1.move(*snake1.direction):
        if score > highscore: 
            highscore = score
            with open("savefiles/highscore.txt", "w") as file:
                file.write(str(highscore))
        gameover_screen(font, window, score, highscore)
        time.sleep(3)
        pygame.quit()
        sys.exit()

    # refresh screen 
    pygame.display.update()
    fps.tick(CONFIG["snake_speed"])

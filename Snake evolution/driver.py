from model.Food import Food
from model.Snake import Snake
from model.World import World
import pygame
import time
import random
import sys
import json
import os

# TODO:
# snake needs to know if its in vacinity of food, wall or self
    # food_obj = (food.x-snake.body[0][0])**2 + (food.y-snake.body[0][1])**2
# have your DNA and params in a script and load it in for better data management 
# write brain module and import into snake

# BUG
# snake movement is jumpy so computer wont register 
    # the collisions dont coincide because of that 

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
except:
    highscore = 0

# read config from file
try:
    with open("config.txt", "r") as file:
        CONFIG = json.load(file)
except:
    CONFIG = {
    "window_x_lim": 400,
    "rendering": True,
    "window_y_lim": 300,
    "blocksize": 10,
    "snake_speed": 15,
    "fontsize" : 50,
    "ini_direction": [
        1,
        0
    ] 
    
}

score = 0
direction = tuple(CONFIG["ini_direction"])
move_input = direction
#####################

def render_text(window, txt, colour, loc=None, alpha=255):
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
    window.fill((120,120,120))
    render_text(window, "PAUSE", RED, "middle")
    render_text(window, "HIGHSCORE {}".format(highscore), WHITE, "topleft", alpha=127)
    pygame.display.update()
    fps.tick(CONFIG["snake_speed"])
    

def gameover_screen(font, window, score, highscore):

    surfaces = [render_text(window, "GAMEOVER", RED),
                render_text(window, "YOUR SCORE: {}".format(score), RED),
                render_text(window, "HIGHSCORE: {}".format(highscore), RED) ]
    rects = [surfaces[surf].get_rect(center = (world.width//2, surf*CONFIG["fontsize"]+CONFIG["fontsize"])) for surf in range(len(surfaces))]

    window.fill((120,120,120))
    for i in range(len(surfaces)):
        window.blit(surfaces[i], rects[i])

    pygame.display.update()
    fps.tick(CONFIG["snake_speed"])


#####################

# Initialising pygame
pygame.init()
pygame.display.set_caption('Snake')
window = pygame.display.set_mode((CONFIG["window_x_lim"], CONFIG["window_y_lim"]))
fps = pygame.time.Clock()
font = pygame.font.Font(None, CONFIG["fontsize"])

# init world 
world = World(window, CONFIG["window_x_lim"], CONFIG["window_y_lim"], CONFIG["blocksize"])
snake1 = Snake(world, init_len=1)
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
                move_input = (0,-1)
            if event.key == pygame.K_DOWN:
                move_input = (0,1)
            if event.key == pygame.K_LEFT:
                move_input = (-1,0)
            if event.key == pygame.K_RIGHT:
                move_input = (1,0)
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

    # render
    world.draw()

    # display text 
    # (window, txt, colour, loc=None, alpha=255)
    render_text(window, "Score {}".format(str(score)), WHITE, "topleft", alpha=127)
    snake1.draw()
    food.draw()

    # if vectors are orthogonal you can change direction else ignore
    if sum([x1y1*x2y2 for x1y1,x2y2 in list(zip(move_input, direction))]) == 0:
        direction = move_input

    # snake finds food
    snakehead = snake1.body[0]
    if snake1.body[0] == (food.x, food.y) or food.rect.colliderect(pygame.Rect(snakehead[0], snakehead[1], world.blocksize, world.blocksize)):
        snake1.grow()
        food = Food(world, world.blocksize)
        score += 1

	# Moving the snake
    if not snake1.move(*direction):
        if score > highscore: 
            highscore = score
            with open("highscore.txt", "w") as file:
                file.write(str(highscore))
        gameover_screen(font, window, score, highscore)
        time.sleep(3)
        pygame.quit()
        sys.exit()

    

    # refresh screen 
    pygame.display.update()
    fps.tick(CONFIG["snake_speed"])

from model.Food import Food
from model.Snake import Snake
from model.World import World
import pygame
import time
import random
import sys

# TODO:
# snake needs to know if its in vacinity of food, wall or self
    # food_obj = (food.x-snake.body[0][0])**2 + (food.y-snake.body[0][1])**2
# have your DNA and params in a script and load it in for better data management 
# write brain module and import into snake

# BUG
# snake movement is jumpy so computer wont register 
    # the collisions dont coincide because of that 

# PARAMETERS
snake_speed = 15
window_x_lim = 600
window_y_lim = 400
blocksize = 10
score = 0
rendering = True
direction = (1,0)
move_input = direction
# RIGHT = (1 , 0)
# LEFT  = (-1, 0)
# UP    = (0 , 1)
# DOWN  = (0 ,-1)


# Initialising pygame
pygame.init()
pygame.display.set_caption('Snake')
window = pygame.display.set_mode((window_x_lim, window_y_lim))
fps = pygame.time.Clock()
font = pygame.font.Font(None, 50)

# init world 
world = World(window, window_x_lim, window_y_lim, blocksize)
snake1 = Snake(world, init_len=1)
food = Food(world)

def pause_screen(font, world):
    window.fill((120,120,120))
    pause_txt = font.render("PAUSE", False, (250,0,0))
    window.blit(
        pause_txt,
        score_text.get_rect(center = (world.width//2, world.height//2))
    )
    pygame.display.update()
    fps.tick(snake_speed)
    
def gameover_screen(font, world):
    window.fill((120,120,120))
    gameover_txt = font.render("GAMEOVER", False, (250,0,0))
    window.blit(
        gameover_txt,
        gameover_txt.get_rect(center = (window_x_lim//2, window_y_lim//2))
    )
    pygame.display.update()
    fps.tick(snake_speed)

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
    score_text = font.render("Score {}".format(str(score)), False, (250,250,250))
    score_rect = score_text.get_rect(topleft = (10,10))
    window.blit(score_text, score_rect)  
    snake1.draw()
    food.draw()

    # if vectors are orthogonal you can change direction else ignore
    if sum([x1y1*x2y2 for x1y1,x2y2 in list(zip(move_input, direction))]) == 0:
        direction = move_input

    # snake finds food
    snakehead = snake1.body[0]
    if snake1.body[0] == (food.x, food.y) or food.rect.colliderect(pygame.Rect(snakehead[0], snakehead[1], world.blocksize, world.blocksize)):
        snake1.grow()
        food = Food(world)
        score += 1

	# Moving the snake
    if not snake1.move(*direction):
        gameover_screen(font, window)
        time.sleep(3)
        pygame.quit()
        sys.exit()

    

    # refresh screen 
    pygame.display.update()
    fps.tick(snake_speed)

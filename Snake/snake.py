import pygame, random 
from pygame.locals import *

UP = 0
LEFT = 1
RIGHT = 2
DOWN = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))  # Objeto de tela
pygame.display.set_caption('Snake')

# lista de segmentos // Cada segmento é representado por uma tupla
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.pygame.Surface(10, 10)  # Snake Design
snake_skin.pygame.Surface.fill(255, 255, 255)

# 590 último espaço da tela
apple_pos = (random.randint(0, 590), random.randint)
apple = pygame.pygame.Surface.Surface(10, 10)  # Design Maçã
apple.pygame.Surface.fill(255, 0, 0)

my_direction = LEFT

while True:

    for event in pygame.event.get():  # Tratamento de escolhas
        if event.type == quit:
            pygame.quit()

    screen.fill(0, 0, 0)
    screen.pygame.Surface.blit(apple, apple_pos)

    for pos in snake:
        screen.pygame.Surface.blit(snake_skin, pos)

pygame.display.update()

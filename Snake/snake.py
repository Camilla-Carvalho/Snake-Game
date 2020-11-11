import pygame
from pygame.locals import *
 
UP = 0
LEFT = 1
RIGHT = 2
DOWN = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))  # Objeto de tela
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)] #lista de segmentos // Cada segmento é representado por uma tupla 
my_direction = LEFT

while True:

    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
    screen = fill(0, 0, 0)

    for pos in s

pygame.display.update()


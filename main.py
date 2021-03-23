import pygame
from pygame.locals import *

screenDimension=(500,500)
screen=pygame.display.set_mode(screenDimension, 0, 32)

while True:
    pygame.display.flip()


    #isso aqui sempre no final, exitará o pygame quando clicar no x
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit(0)


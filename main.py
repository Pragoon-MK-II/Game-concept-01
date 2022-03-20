import pygame
from Player import Player
from constants import *

def main():
    clock = pygame.time.Clock()
    background = pygame.image.load('Images/UI.png')
    background = pygame.transform.scale(background, (1028, 724))
    running = True
    player = Player()


    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, (0, 100))
        player.update()
        pygame.display.flip()
main()

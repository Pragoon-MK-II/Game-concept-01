import pygame
from Boss import Boss
from Player import Player
from constants import *


def main():
    clock = pygame.time.Clock()
    background = pygame.image.load('Images/UI.png')
    background = pygame.transform.scale(background, (width, height))
    running = True
    player = Player()
    boss1= Boss(screen)
    while running:
        clock.tick(60)
        collide = pygame.Rect.colliderect(player.rect, boss1.rect)
        if collide:
            player.die()
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 100))
        player.update()
        boss1.update()
        pygame.display.flip()





main()

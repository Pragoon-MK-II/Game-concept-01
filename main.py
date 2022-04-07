import pygame
from Boss import Boss
from Player import Player
from constants import *

def startscreen():
    pygame.init()
    background = pygame.image.load('Images/pointW.jpg')
    background = pygame.transform.scale(background, (width, height))
    running = True
    font = pygame.font.Font(None, 24)
    text = font.render('START', True, (100,0,0))
    textRect = text.get_rect()
    textRect.center = (1000 // 2, 900 // 2)
    while running:
        screen.blit(background, (0, 100))
        screen.blit(text, textRect)
        pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    pygame.mixer.music.play(-1)
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





startscreen()
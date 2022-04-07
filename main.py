import pygame
from Boss import Boss
from Player import Player
from constants import *


def startscreen():
    pygame.init()
    background = pygame.image.load('Images/pointW.jpg')
    background = pygame.transform.scale(background, optimal)
    running = True
    font = pygame.font.Font(None, 24)
    textY = 900
    textX = 1000
    exitt = font.render('EXIT', True, (100, 0, 0))
    text = font.render('START', True, (100, 0, 0))
    textRect = text.get_rect()
    exitRect = exitt.get_rect()
    textRect.center = [textX // 2, textY // 2]
    exitRect.center = [(textX // 2), (textY // 2)+50]
    print(exitRect.center)
    print(textRect.center)
    while running:
        for event in pygame.event.get():
            mpos = pygame.mouse.get_pos()
            if textRect.center[0] + 10 > mpos[0] > textRect.center[0]-30 and \
            textRect.center[1]-30 < mpos[1] < 10 + textRect.center[1]:
                print(mpos)
                main()
            if exitRect.center[0] + 10 > mpos[0] > exitRect.center[0]-30 and \
            exitRect.center[1]-30 < mpos[1] < 10 + exitRect.center[1]:
                exit()
        screen.blit(background, (0, 100))
        screen.blit(text, textRect)
        screen.blit(exitt, exitRect)
        pygame.display.flip()


def main():
    clock = pygame.time.Clock()
    pygame.mixer.music.play(-1)
    background = pygame.image.load('Images/UI.png')
    background = pygame.transform.scale(background, (width, height))
    running = True
    player = Player()
    boss1 = Boss(screen)
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

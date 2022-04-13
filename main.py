import time as t
import pygame
from Boss import Boss
from Player import Player
from constants import *
from Boss import *


def startscreen():
    pygame.init()
    background = pygame.image.load('Images/pointW.jpg')
    background = pygame.transform.scale(background, optimal)
    running = True
    font = pygame.font.Font(None, 24)
    textY = 850
    textX = 1000
    exitt = font.render('EXIT', True, (100, 0, 0))
    text = font.render('START', True, (100, 0, 0))
    textRect = text.get_rect()
    exitRect = exitt.get_rect()
    textRect.center = [textX // 2, textY // 2]
    exitRect.center = [(textX // 2), (textY // 2) + 50]
    while running:
        for event in pygame.event.get():
            mpos = pygame.mouse.get_pos()
            if textRect.center[0] + 30 > mpos[0] > textRect.center[0] - 30 and \
                    textRect.center[1] - 10 < mpos[1] < 10 + textRect.center[1]:
                main()
            if exitRect.center[0] + 10 > mpos[0] > exitRect.center[0] - 30 and \
                    exitRect.center[1] - 10 < mpos[1] < 10 + exitRect.center[1]:
                exit()
        screen.blit(background, (0, 0))
        screen.blit(text, textRect)
        screen.blit(exitt, exitRect)
        pygame.display.flip()


def main():
    clock = pygame.time.Clock()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("music/120 BPM CUT.wav"))
    background = pygame.image.load('Images/UI.png')
    background = pygame.transform.scale(background, (width, height))
    running = True
    player = Player()
    boss1 = Boss(screen)
    while running:
        clock.tick(60)
        collide = pygame.Rect.colliderect(player.rect, boss1.rect)
        for bullet in boss1.bullets:
            collide2 = pygame.Rect.colliderect(player.rect, bullet)
            if collide2:
                pygame.mixer.quit()
                avocado.play()
                player.die()

        if collide:
            player.die()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys[K_SPACE]:
                pygame.mixer.pause()
                youDied.play()
                t.sleep(1)
                exit()
        screen.blit(background, (0, 0))
        player.update()

        boss1.update()
        pygame.display.flip()
    pygame.mixer.music.stop()


startscreen()

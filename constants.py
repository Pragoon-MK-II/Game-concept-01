import pygame
from pygame import *

screen = pygame.display.set_mode((1028, 926))

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

X_C = 100
Y_C = 100
pygame.mixer.init()
pygame.mixer.music.load('music/Lavender Town cut.mp3')
import pygame

screen = pygame.display.set_mode((1028, 926))

width = 70
height = 70

X_C=100
Y_C=100

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"
CENTER = "CENTER"

DIRECTION_DICT = {UP: {"x": 0, "y": -1},
                  CENTER: {"x": 0, "y": 0},
                  DOWN: {"x": 0, "y": 1},
                  LEFT: {"x": -1, "y": 0},
                  RIGHT: {"x": 1, "y": 0}}

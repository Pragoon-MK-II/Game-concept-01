import time as t
from constants import *


class Player:
    def __init__(self):
        self.front_image = pygame.image.load('Images/front.png')
        self.front_image = pygame.transform.scale(self.front_image, (100, 100))
        self.back_image = pygame.image.load('Images/back.png')
        self.back_image = pygame.transform.scale(self.back_image, (100, 100))
        self.dead_image = pygame.image.load('Images/sickass.png')
        self.dead_image = pygame.transform.scale(self.dead_image, (100, 100))
        self.rect = self.front_image.get_rect()
        self.rect.x = 600
        self.rect.y = 700
        self.direction = "DOWN"
        self.alive = True


    def die(self):
        self.alive = False
        screen.blit(self.dead_image, (self.rect.x, self.rect.y))
        t.sleep(1)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 70:
            self.direction = "UP"
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.y < height:
            self.direction = "DOWN"
            self.rect.y += 5
        if keys[pygame.K_LEFT] and self.rect.x > 180:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.x < 760:
            self.rect.x += 5

        if self.direction == "UP":
            screen.blit(self.back_image, (self.rect.x, self.rect.y))
        elif self.direction == "DOWN":
            screen.blit(self.front_image, (self.rect.x, self.rect.y))

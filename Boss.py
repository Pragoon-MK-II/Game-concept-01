import pygame.sprite
from Bullet import Bullet
import random
from constants import *
import math


class Boss:
    def __init__(self, screen):
        self.image = pygame.image.load('Images/supersuper.png')
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 100
        self.timer = 60
        self.screen = screen
        self.bullets = pygame.sprite.Group()

    def regular_attack(self):
        pass

    def update(self):
        seconds = 0
        if self.timer == 0:
            angle = random.randint(-50, 50)
            b = Bullet('Images/sprite0.png', self.rect.x, self.rect.y, 10, angle, self.screen)
            self.bullets.add(b)
            self.timer = 60
            seconds += 1

        else:
            self.timer -= 1

        if seconds == 5:
            i = 0
            x = 300
            angle2 = random.randint(1, 1)
            while i < 5:
                c = Bullet('Images/sprite0.png', x, 800, 10, angle2, self.screen)
                self.bullets.add(c)
                x += 80
                i += 1

        self.bullets.draw(self.screen)
        self.bullets.update()
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

import pygame.sprite
from Bullet import Bullet
import random
import math


class Boss:
    def __init__(self, screen):
        self.image = pygame.image.load('Images/supersuper.png')
        self.image = pygame.transform.scale(self.image, (600, 500))
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 100
        self.timer = 60
        self.screen = screen
        self.bullets = pygame.sprite.Group()

    def regular_attack(self):
        pass

    def update(self):
        if self.timer == 0:
            angle = random.randint(-90, 90)
            b = Bullet('Images/saskeee.png', self.rect.x, self.rect.y, 10, angle, self.screen)
            self.bullets.add(b)
            self.timer = 60
        else:
            self.timer -= 1
        self.bullets.draw(self.screen)
        self.bullets.update()
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

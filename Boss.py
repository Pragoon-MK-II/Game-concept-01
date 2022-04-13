import pygame.sprite
from Bullet import Bullet
import random
from constants import *
import math


class Boss:
    def __init__(self, screen):
        self.image = pygame.image.load('Images/supersuper.png')
        self.image = pygame.transform.scale(self.image, (300, 200) )
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 100
        self.timer = 60
        self.screen = screen
        self.seconds = 0
        self.bullets = pygame.sprite.Group()
        self.hypersecondtimer = 0.0


    def regular_attack(self):
        pass

    def update(self):
        if self.timer == 0:

            angle = random.randint(-50, 50)
            b = Bullet('Images/sprite0.png', self.rect.x, self.rect.y, 10, angle, self.screen, (80,80))
            self.bullets.add(b)
            self.timer = 60
            self.seconds += 1

        else:
            self.timer -= 1
            self.hypersecondtimer += 1

        if self.seconds == 5 or self.seconds == 7 or self.seconds == 9 and self.hypersecondtimer % 60 == 0:
            i = 0
            x = 100

            angle2 = random.randint(1, 1)
            bullet_list = []
            while i < 10:
                bullet_list.append(Bullet('Images/sprite0.png', x, self.rect.y, 10, angle2, self.screen, (80,80) ) )
                x += 80
                i += 1
            self.bullets.add(bullet_list)

        if self.seconds == 2 and self.hypersecondtimer % 60 == 0:
            d = Bullet('Images/BEAM.png', 450 , self.rect.y, 0, random.randint(1,1), self.screen, (100,height))

            self.bullets.add(d)


        self.bullets.draw(self.screen)
        self.bullets.update()
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

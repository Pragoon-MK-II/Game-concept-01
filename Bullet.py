import math as m
from constants import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed, angle, screen, scaling):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (scaling))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = int(scaling[0]/8)
        self.rect.height = int(scaling[1]/8)
        self.speed = speed
        self.angle = m.radians(angle)
        self.screen = screen

    def update(self):

        if 180 < self.rect.x < 780 and 70 < self.rect.y < height:
            self.rect.x += self.speed * m.sin(self.angle)
            self.rect.y += self.speed * m.cos(self.angle)
        else:
            self.kill()


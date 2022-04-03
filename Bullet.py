import pygame
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed, angle, screen):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (80, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.angle = math.radians(angle)
        self.screen = screen

    def update(self):
        self.rect.x += self.speed * math.sin(self.angle)
        self.rect.y += self.speed * math.cos(self.angle)

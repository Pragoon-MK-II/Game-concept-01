import time as t
from constants import *


class Player:
    def __init__(self):
        self.front_image = pygame.image.load('Images/front.png')
        self.front_image = pygame.transform.scale(self.front_image, (100, 100))

        self.back_image = pygame.image.load('Images/back.png')
        self.back_image = pygame.transform.scale(self.back_image, (100, 100))

        self.left_image = pygame.image.load('Images/left.png')
        self.left_image = pygame.transform.scale(self.left_image, (100, 100))

        self.right_image = pygame.image.load('Images/right.png')
        self.right_image = pygame.transform.scale(self.right_image, (100, 100))

        self.dead_image = pygame.image.load('Images/sickass.png')
        self.dead_image = pygame.transform.scale(self.dead_image, (100, 100))

        self.death_image = pygame.image.load('Images/avocado.jpg')
        self.death_image = pygame.transform.scale(self.death_image, (1028, 926))
        self.rect = self.front_image.get_rect()
        self.rect.x = 600
        self.rect.y = 700
        self.direction = "DOWN"

    def die(self):

        screen.blit(self.dead_image, (self.rect.x, self.rect.y))
        pygame.display.flip()
        t.sleep(1)
        screen.blit(self.death_image, (0, 0))
        pygame.display.flip()
        t.sleep(2)
        self.update()
        exit()


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 70:
            self.direction = "UP"
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.y < height:
            self.direction = "DOWN"
            self.rect.y += 5
        if keys[pygame.K_LEFT] and self.rect.x > 180:
            self.direction = "LEFT"
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.x < 760:
            self.direction = "RIGHT"
            self.rect.x += 5

        if self.direction == "UP":
            screen.blit(self.back_image, (self.rect.x, self.rect.y))
        elif self.direction == "DOWN":
            screen.blit(self.front_image, (self.rect.x, self.rect.y))
        elif self.direction == "LEFT":
            screen.blit(self.left_image, (self.rect.x, self.rect.y))
        elif self.direction == "RIGHT":
            screen.blit(self.right_image, (self.rect.x, self.rect.y))

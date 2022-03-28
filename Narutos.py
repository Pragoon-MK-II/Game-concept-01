from Player import *
class Naruto:
    def __init__(self):
        Player.__init__(self)
        clock = pygame.time.Clock()
        self.image = pygame.image.load('Images/saskeee.png')
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect=self.image.get_rect()
        self.rect.x = 180
        self.rect.y = 700

    def update(self):
        while(self.rect.x< 760):
            self.rect.x +=5

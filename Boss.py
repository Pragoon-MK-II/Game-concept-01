import pygame.sprite
from Bullet import Bullet
import random
from constants import *
import math


class Boss:
    def __init__(self, screen):
        self.image = pygame.image.load('Images/BLANK.png')
        self.image = pygame.transform.scale(self.image, (300, 200) )
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 100
        self.timer = 60
        self.screen = screen
        self.seconds = 0.0
        self.bullets = pygame.sprite.Group()
        self.hypersecondtimer = 0.0
        self.bpmR = 2


    def regular_attack(self):
        pass

    def update(self):
        if self.timer == 0:

            angle = random.randint(-50, 50)
            anglep = random.randint(-50, 50)
            angleL = random.randint(-50, 50)
            angleu = random.randint(-50, 50)
            b = Bullet('Images/sprite2.png', self.rect.x, self.rect.y, 7, angle, self.screen, (80,80), (10,10) )
            o = Bullet('Images/sprite2.png', self.rect.x, self.rect.y, 7, anglep, self.screen, (80,80), (10,10) )
            u = Bullet('Images/sprite2.png', self.rect.x, self.rect.y, 7, angleu, self.screen, (80, 80), (10, 10))
            self.bullets.add(b)
            self.bullets.add(o)
            self.bullets.add(u)
            if self.seconds > 20:
                l = Bullet('Images/sprite5.png', self.rect.x, self.rect.y, 3, angleL, self.screen, (80,80) , (10,10) )
                l2 = Bullet('Images/sprite5.png', self.rect.x, self.rect.y, 3, angleL, self.screen, (80, 80), (10, 10))
                l3 = Bullet('Images/sprite5.png', self.rect.x, self.rect.y, 3, angleL, self.screen, (80, 80), (10, 10))
                l4 = Bullet('Images/sprite5.png', self.rect.x, self.rect.y, 3, angleL, self.screen, (80, 80), (10, 10))
                self.bullets.add(l)
                self.bullets.add(l2)
                self.bullets.add(l3)
                self.bullets.add(l4)

            self.timer = 60
            if self.bpmR == 2:
                self.seconds += 0.5
            elif self.bpmR == 4:
                self.seconds += 0.25
            elif self.bpmR == 8: self.seconds += 0.125

        else:
            self.timer -= self.bpmR
            self.hypersecondtimer += 1

        if self.seconds % 10 == 0 and self.seconds < 50 and self.seconds != 0:
            if self.bpmR == 2:
                pygame.mixer.Channel(0).pause()
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("music/240 BPM CUT.wav"))
                self.bpmR = 4

            elif self.bpmR == 4:
                pygame.mixer.Channel(1).pause()
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("music/120 BPM CUT.wav"))
                self.bpmR = 2
            self.seconds+=1

        if self.seconds == 50:
            self.bpmR = 8
            pygame.mixer.Channel(1).pause()
            pygame.mixer.Channel(0).pause()
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("music/480 BPM CUT.wav"))


        if self.seconds > 5 and self.timer==0 and self.seconds<20:
            i = 0
            j = 0
            k = 0
            t = 0
            g = 0
            x = 100

            angle2 = random.randint(1, 1)
            angle3 = random.randint(45,45)
            angle4 = random.randint(-45,-45)

            bullet_list = []
            while i < 10:
                bullet_list.append(Bullet('Images/sprite0.png', x, self.rect.y, 10, angle2, self.screen, (80,80) , (10,10) ) )
                x += 80
                i += 1

            while j < 8:
                bullet_list.append(Bullet('Images/sprite3.png', 250, self.rect.y+200,7, angle3, self.screen, (80,80) , (10,10) ) )
                x += 80
                j += 1

            while k < 8:
                bullet_list.append(Bullet('Images/sprite4.png', width-300, self.rect.y+200, 7, angle4, self.screen, (80,80) , (10,10) ) )
                x -= 80
                k += 1

            while t < 8:
                bullet_list.append(Bullet('Images/sprite4.png', width-300, self.rect.y+300, 7, angle4, self.screen, (80,80) , (10,10) ) )
                x -= 80
                t += 1
            while g < 8:
                bullet_list.append(Bullet('Images/sprite4.png', 250, self.rect.y+300, 7, angle4, self.screen, (80,80) , (10,10) ) )
                x += 80
                g += 1
            self.bullets.add(bullet_list)

        #self.dead_image = pygame.image.load('Images/sickass.png')
        #self.dead_image = pygame.transform.scale(self.dead_image, (100, 100))


        if self.seconds == 1:
            warning = pygame.image.load('Images/WARNING.png')
            warning = pygame.transform.scale(warning, (100,150))
            screen.blit(warning, (450, 100))



        if self.seconds == 2 and self.timer==0 :
            d = Bullet('Images/BEAM.png', 450 , self.rect.y, 0, random.randint(1,1), self.screen, (100,height) , (40,height))
            e = Bullet('Images/BEAM.png', 250, self.rect.y, 0, random.randint(1, 1), self.screen, (100, height), (40,height))
            f = Bullet('Images/BEAM.png', 650, self.rect.y, 0, random.randint(1, 1), self.screen, (100, height), (40,height))
            g = Bullet('Images/New Piskel (1).png', 210, 300, 0, random.randint(1,1), self.screen, (620, 100), (width,40))
            h = Bullet('Images/New Piskel (1).png', 210, 500, 0, random.randint(1, 1), self.screen, (620, 100),(width, 40))

            #self.bullets.add(d)
            #self.bullets.add(e)
            #self.bullets.add(f)
            #self.bullets.add(g)
            #self.bullets.add(h)

        if self.seconds == 3 and self.timer == 0:
            i = 0

            while i<9:
                #self.bullets[i].kill()
                i += 1


        if self.seconds > 20 and self.timer == 0:
            i = 0
            x = 250
            angle2 = random.randint(90,90)
            bullet_list = []
            y = 1000

            while i < 10:
                bullet_list.append(
                    Bullet('Images/sprite1.png', x, y, 5, angle2, self.screen, (80, 80), (10, 10)))
                y -= 100
                i += 1
            self.bullets.add(bullet_list)




        if self.seconds > 30 and self.timer == 0:
            i = 0
            x = 100

            angle2 = random.randint(1, 1)
            bullet_list = []
            while i < 10:
                bullet_list.append(
                    Bullet('Images/sprite0.png', x, self.rect.y, 8, angle2, self.screen, (80, 80), (10, 10)))
                x += 80
                i += 1
            self.bullets.add(bullet_list)

        if self.seconds > 50 and self.timer == 0:
            i = 0
            x = 250
            y = 1000
            angle2 = random.randint(1, 1)
            angle3 = random.randint(-1,-1)
            bullet_list = []
            while i < 10:
                bullet_list.append(
                    Bullet('Images/sprite5.png', x, self.rect.y, 8, angle2, self.screen, (80, 80), (10, 10)))
                x += 80
                i += 1
            while j < 10:
                bullet_list.append(
                    Bullet('Images/sprite5.png', x, y, 8, angle2, self.screen, (80, 80), (10, 10)))
                y -= 80
                j += 1
            self.bullets.add(bullet_list)







        self.bullets.draw(self.screen)
        self.bullets.update()
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

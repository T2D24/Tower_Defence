import pygame
import random
from config import *
from levels import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Enemy, self).__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, SIZE)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = 10 + random.randint(-7, 10)
        self.vel_x = 3
        self.path = level1
        self.vel_y = 3
        self.reward = 2 + random.randint(-1, 3)
        self.dmg = 3 + random.randint(1, 3)

    def update(self):
        self.dead()
        self.moving()

    def moving(self):       # переписать этот метод, а то это полное говно
        '''for dot in self.path:
            while True:
                if self.rect.x < dot[0]:
                    self.rect.x += self.vel_x
                elif self.rect.x > dot[0]:
                    self.rect.x -= self.vel_x
                if self.rect.y > dot[1]:
                    self.rect.y -= self.vel_y
                elif self.rect.y < dot[1]:
                    self.rect.y += self.vel_y
                    '''
        if self.rect.y > 0:
            self.rect.y -= self.vel_y

        if self.rect.y <= 0:
            self.rect.y = 0

        if self.rect.y == 0 and self.rect.x < 800:
            self.rect.x += self.vel_x

        if self.rect.right >= 800:
            self.rect.right = 800

        if self.rect.y <= 600 and self.rect.right == 800:
            self.rect.top += 2 * self.vel_y

        if self.rect.bottom >= 600:
            self.dead()

    def dead(self):
        if self.hp <= 0 or self.rect.bottom >= 600:
            return 1, self.kill()


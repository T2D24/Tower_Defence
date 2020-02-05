import pygame
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
        self.hp = 30
        self.vel_x = 3
        self.path = level1
        self.vel_y = 3

    def update(self):
        self.dead()
        self.moving()

    def moving(self):
        for dot in self.path:
            while True:
                if self.rect.x < dot[0]:
                    self.rect.x += self.vel_x
                elif self.rect.x > dot[0]:
                    self.rect.x -= self.vel_x
                if self.rect.y > dot[1]:
                    self.rect.y -= self.vel_y
                elif self.rect.y < dot[1]:
                    self.rect.y += self.vel_y

                if (self.rect.x >= dot[0] and self.rect.y >= dot[1]) or (
                        self.rect.x >= dot[0] and self.rect.y <= dot[1]) or (
                        self.rect.x <= dot[0] and self.rect.y >= dot[1]) or (
                        self.rect.x <= dot[0] and self.rect.y <= dot[1]):
                    break



            else:
                exit()

    def dead(self):
        if self.hp <= 0:
            self.kill()

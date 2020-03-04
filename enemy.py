import pygame
import random
from config import *
from levels import *
from animation import Animation


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemy, self).__init__()
        self.anim = Animation(ENEMY_1_WALK, x, y)
        self.image = self.anim.image
        self.rect = self.anim.rect
        self.hp = 10 + random.randint(-7, 10)
        self.vel_x = 1
        self.path = level1
        self.vel_y = 1
        self.reward = 2 + random.randint(-1, 3)
        self.dmg = 3 + random.randint(1, 3)
        self.hp_fix = self.hp

    def maskMake(self):
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.anim.update()
        self.image = self.anim.image
        self.maskMake()
        self.dead()
        self.moving()
        self.health_bar()
        # print(self.rect.x, " ", self.rect.y)
        
    def moving(self):       # переписать этот метод, а то это полное говно РУСТАМ ПЛЕЗ МЕН ДУ ИТ ПИДАРАС ЕБАНЫЙ СДЕЛАЙ ХОТЬ ЧТО НИБУДЬ УРОД!!!!
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

    def health_bar(self):
        height = 10 
        width = (self.hp * self.rect.width) / self.hp_fix
        pygame.draw.line(self.image, (200, 0, 0), (0, 0), (self.rect.width, 0), height)
        pygame.draw.line(self.image, (0, 200, 0), (0,0), (width, 0), height)



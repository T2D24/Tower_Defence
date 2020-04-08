import pygame
import random
from config import *
from levels import *
from animation import Animation


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemy, self).__init__()
        if random.randint(0, 1) == 1:
            self.anim = Animation(ENEMY_2_WALK, x, y, (SIZE[0] + 25, SIZE[1]), True, False)
        else:
            self.anim = Animation(ENEMY_1_WALK, x, y, (SIZE[0] + 25, SIZE[1]), True, False)
        self.image = self.anim.image
        self.rect = self.anim.rect
        self.hp = 10 + random.randint(-7, 10)
        self.vel_x = 3
        self.path = level1
        self.vel_y = 3
        self.reward = 2 + random.randint(-1, 3)
        self.dmg = 3 + random.randint(1, 3)
        self.hp_fix = self.hp
        self.radius = SIZE[0] // 3

        #   как фичу можно придумать что мы играем за монстров

    def update(self, ms):
        self.anim.update(ms)
        self.image = self.anim.image
        self.health_bar()
        # print(self.rect.x, " ", self.rect.y)

    def moving(self):  # переписать этот метод, а то это полное говно

        if self.rect.y <= 0:
            self.rect.y = 0

        if self.rect.y == 0 and self.rect.right < WIN_SIZE[0]:
            self.rect.x += self.vel_x

        if self.rect.right >= WIN_SIZE[0]:
            self.rect.right = WIN_SIZE[0]

        if self.rect.y <= WIN_SIZE[1] and self.rect.right == WIN_SIZE[0]:
            self.rect.top += self.vel_y

        if self.rect.bottom >= WIN_SIZE[1]:
            return 1, self.kill()

    def dead(self):
        if self.hp <= 0 or self.rect.bottom >= WIN_SIZE[1]:
            return 1, self.kill()

    def health_bar(self):
        height = 10
        width = (self.hp * self.rect.width) / self.hp_fix
        pygame.draw.line(self.image, (200, 0, 0), (0, 0), (self.rect.width, 0), height)
        pygame.draw.line(self.image, (0, 200, 0), (0, 0), (width, 0), height)

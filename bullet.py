import pygame
from config import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, spawn, enemy):
        super(Bullet, self).__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, SIZE)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = spawn[0], spawn[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5
        self.enemy = enemy
        self.spawn = spawn

    def aim(self):  # функиця расчета полета пули
        x = self.enemy.rect.centerx - 18 - self.rect.x
        y = self.enemy.rect.centery - 18 - self.rect.y
        if x == 0 and y == 0:
            self.kill()
        k = pow((x * x + y * y), 0.5) / self.speed
        self.nx = x / k
        self.ny = y / k

    def update(self):
        self.aim()
        self.rect.x += self.nx
        self.rect.y += self.ny
        self.hitting()

    def hitting(self):
        if pygame.sprite.spritecollide(self, [self.enemy], False, pygame.sprite.collide_mask):
            self.enemy.hp -= 4
            self.kill()


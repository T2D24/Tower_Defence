import pygame
from config import *
import math
from tower import *
from animation import Animation



class Shop(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super(Shop, self).__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, SHOP_SIZE)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def draw_shop(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def buy_tower(self, gold, towers):
        gold -= 100
        towers.add(Tower(self.rect.x + 45, self.rect.y + 43, TOWER))
        return gold



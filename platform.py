import pygame
from config import *
import math
from shop import *

class Platform(Shop):
    def __init__(self, pos, image):
        super(Platform, self).__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, SHOP_SIZE)
        self.image.convert_alpha()
        self.img_shop = pygame.image.load(SHOP)
        self.img_shop = pygame.transform.scale(self.img_shop, SHOP_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.able_click = True
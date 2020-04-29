import pygame
from config import *
import math
from shop import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super(Platform, self).__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (WIN_SIZE[0] // 16, WIN_SIZE[1] // 9))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.able_click = True
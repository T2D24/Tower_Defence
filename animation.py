import pygame
import os
from config import *

class Animation(pygame.sprite.Sprite):
    def __init__(self, images, x, y):
        super(Animation, self).__init__()
        self.clock = pygame.time.Clock()
        self.tiles = []
        self.time = 0
        self.loadFromFiles(images)
        self.image = pygame.Surface(SIZE, 
                            pygame.SRCALPHA | pygame.HWSURFACE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.update()

    def loadFromFiles(self, images):
        for image in images:
            self.pic = pygame.image.load(image)
            self.pic = pygame.transform.scale(self.pic, SIZE)
            self.pic.convert_alpha()
            self.tiles.append(self.pic)

    def update(self):
        ms = self.clock.tick(FPS)
        self.time += ms
        if self.time // FPS >= 20:
            self.time = 0
        self.image.fill(pygame.SRCALPHA | pygame.HWSURFACE)
        self.image.blit(self.tiles[self.time // FPS], (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.image.convert_alpha()
        
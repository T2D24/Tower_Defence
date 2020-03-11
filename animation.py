import pygame
import os
from config import *
# анимация смерти и урона у врага 
class Animation(pygame.sprite.Sprite):
    def __init__(self, images, x, y, size, loop, paused):
        super(Animation, self).__init__()
        self.loop = loop
        self.clock = pygame.time.Clock()
        self.tiles = []
        self.time = 0
        self.loadFromFiles(images, size)
        self.image = pygame.Surface(SIZE, 
                            pygame.SRCALPHA | pygame.HWSURFACE)
        self.image.fill(pygame.SRCALPHA | pygame.HWSURFACE)
        self.image.blit(self.tiles[0], (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.convert_alpha()                    
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.image.blit(self.tiles[0], (0, 0))
        self.finished = False
        self.paused = paused

    def loadFromFiles(self, images, size):
        for image in images:
            self.pic = pygame.image.load(image)
            self.pic = pygame.transform.scale(self.pic, size)
            self.pic.convert_alpha()
            self.tiles.append(self.pic)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)

    def update(self, ms):
        if not self.paused:
            self.time += ms
            if self.time // FPS >= len(self.tiles) and self.loop:
                self.time = 0
            if self.time // FPS >= len(self.tiles) and not self.loop:
                self.time = 0
                self.finished = True
            self.image.fill(pygame.SRCALPHA | pygame.HWSURFACE)
            self.image.blit(self.tiles[self.time // FPS], (0, 0))
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            self.image.convert_alpha()
            
            

    
        
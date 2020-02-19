import pygame
from config import *


class Button(pygame.sprite.Sprite):
    def __init__(self, tower):
        super(Button, self).__init__()
        self.image = pygame.image.load(upgrade)
        self.image = pygame.transform.scale(self.image, BUTTON_SIZE).convert_alpha()
        self.rect = self.image.get_rect()
        self.tower = tower
        self.rect.x = self.tower.rect.left
        self.rect.y = self.tower.rect.bottom

    def clicked(self):
        self.tower.dmg += 2
        self.tower.upgrade_cost += 5











import pygame
from config import *


class Button(pygame.sprite.Sprite):
    def __init__(self, tower):
        super(Button, self).__init__()
        self.image = pygame.image.load(UPGRADE)
        self.image = pygame.transform.scale(self.image, BUTTON_SIZE).convert_alpha()
        self.rect = self.image.get_rect()
        self.tower = tower
        self.rect.x = self.tower.rect.left
        self.rect.y = self.tower.rect.bottom
        self.myfont = pygame.font.SysFont('arial', 18)

    def clicked(self):
        if self.tower.fire_rate > 100:
            self.tower.fire_rate -= 100
        self.tower.dmg += 2
        self.tower.upgrade_cost += 5
        self.tower.level += 1

    def get_cost(self):
        return self.tower.upgrade_cost

    def draw_cost(self, display):
        cost = self.myfont.render(str(self.tower.upgrade_cost), False, (0, 0, 0))
        display.blit(cost, self.rect.bottomleft)

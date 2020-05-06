import pygame
from config import *
from bullet import *
from button import *
from animation import Animation


# новые типы башен и анимация башен 
class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, images, type):
        super(Tower, self).__init__()
        self.anim = Animation(TOWER_1, x, y, \
                                  SIZE, True, False)
        self.type = type
        self.image = self.anim.image
        self.rect = self.anim.rect
        self.rect.x, self.rect.y = x, y
        self.level = 1
        self.upgrade_cost = 12
        self.radius = 250
        self.ms = 0
        self.fire_rate = 2000
        self.dmg = 3
        self.button = Button(self)
        self.cost_to_buy = 200
        self.clicked = False

    def update(self, enemies, bullets, ms, display):
        enemies = pygame.sprite.spritecollide(self, enemies, False,
                                              collided=pygame.sprite.collide_circle_ratio(1))
        self.ms += ms
        if enemies and self.ms > self.fire_rate:
            newBullet = Bullet(BULLET_IMG, self.rect.topleft, enemies[0], self.dmg, 'arch')
            newBullet.add(bullets)
            self.ms = 0

        self.check_radius()
        self.anim.update(ms - 20)
        self.image = self.anim.image

    def check_radius(self):
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if self.rect.left <= pos[0] <= self.rect.right and self.rect.top <= pos[1] <= self.rect.bottom:
                self.clicked = True
            else:
                self.clicked = False

    def draw_circle(self, display):
        if self.clicked:
            pygame.draw.circle(display, (0, 255, 0), (self.rect.centerx, self.rect.centery), self.radius, 5)

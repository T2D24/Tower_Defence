import pygame 
from config import *
from bullet import *
from button import *

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Tower, self).__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, SIZE)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.level = 1
        self.upgrade_cost = 4
        self.radius = 150
        self.ms = 0
        self.fire_rate = 2000
        self.dmg = 4
        self.button = Button(self)

    def update(self, enemies, bullets, ms):
        enemies = pygame.sprite.spritecollide(self, enemies, False,
                        collided = pygame.sprite.collide_circle_ratio(1))
        self.ms += ms
        if enemies and self.ms > self.fire_rate:                                            # 2000 нужно будет в отдельную переменную которая отвечает за скорострельность
            newBullet = Bullet(bulletImg, self.rect.topleft, enemies[0], self.dmg)             # картинки нужно будет разные выдавать
            newBullet.add(bullets)                                                # нужно передавать topleft а не self
            self.ms = 0






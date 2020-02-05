import pygame 
from config import *
from bullet import *

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Tower, self).__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, SIZE)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = 150
        self.ms = 0

    def update(self, enemies, bullets, ms):
        enemies = pygame.sprite.spritecollide(self, enemies, False,
                        collided = pygame.sprite.collide_circle_ratio(1))

        self.ms += ms
        if enemies and self.ms > 2000: 
            newBullet = Bullet(bulletImg, self, enemies[0])
            newBullet.add(bullets)
            self.ms = 0

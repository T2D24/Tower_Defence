import pygame
from config import *
import math
from animation import Animation

# целится не в маску а в центр surface, исправить на маску

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, spawn, enemy, dmg):
        super(Bullet, self).__init__()
        self.anim = Animation(FIREBALL_BLOWUP, spawn[0], spawn[1], \
                             (SIZE[0] - 30, SIZE[1]), False, True)
        self.image = self.anim.image
        self.rect = self.anim.rect
        self.rect.x, self.rect.y = spawn[0], spawn[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 8
        self.enemy = enemy
        self.spawn = spawn
        self.dmg = dmg
        self.local_ms = 0
        self.bulletRotate()

    def aim(self, ms):  # функиця расчета полета пули
        x = self.enemy.rect.x - self.rect.x
        y = self.enemy.rect.y - self.rect.y
        if x == 0 and y == 0:
            self.kill()
        k = pow((x * x + y * y), 0.5) // self.speed
        if not k:
            k = 1
        self.nx = x / k  # локальные nx и ny
        self.ny = y / k
        self.local_ms += ms
    #перестало работать после анимации
    def bulletRotate(self):
        x1 = 0
        y1 = self.enemy.rect.y - self.rect.y
        x2 = self.enemy.rect.x - self.rect.x
        y2 = self.enemy.rect.y - self.rect.y
        cosa = (x1 * x2 + y1 * y2) / (math.sqrt(x1 * x1 + y1 * y1) * math.sqrt(x2 * x2 + y2 * y2))
        angle = math.acos(cosa) * 57.2958
        if self.rect.x < self.enemy.rect.x:
            angle *= -1
        if self.rect.y < self.enemy.rect.y:
            if angle > 0:
                angle += 90
            if angle < 0:
                angle -= 90
        self.anim.rotate(angle + 180)
        self.local_ms = 0

    def update(self, ms):
        self.anim.update(ms)
        self.image = self.anim.image
        self.aim(ms)
        self.rect.x += self.nx
        self.rect.y += self.ny
        self.hitting()

    def hitting(self):
        if pygame.sprite.spritecollide(self, [self.enemy], False, pygame.sprite.collide_mask) and self.anim.paused:
            self.enemy.hp -= self.dmg
            self.anim.paused = False
        if self.anim.finished:
            self.kill()


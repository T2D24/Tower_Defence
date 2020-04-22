import pygame
from config import *
import math
import random
from animation import Animation


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, spawn, pos, dmg, type):
        super(Bullet, self).__init__()
        if random.randint(0, 1) == 1:
            # сделать выбор спрайта при создании
            self.anim = Animation(STONE_BLOWUP, spawn[0], spawn[1], (SIZE[0] - 30, SIZE[1] - 30), False, True)
        else:
            self.anim = Animation(FIREBALL_BLOWUP, spawn[0], spawn[1], (SIZE[0] - 40, SIZE[1] - 10), False, True)
        self.image = self.anim.image
        self.rect = self.anim.rect
        self.rect.x, self.rect.y = spawn[0], spawn[1]
        self.speed = 8
        self.pos = pos
        self.type = type
        self.spawn = spawn
        self.dmg = dmg
        self.local_ms = 0
        self.radius = SIZE[0] // 3
        self.enemies = enemies
        self.bulletRotate()
        self.aoe = 200

    def aim(self, ms):  # функиця расчета полета пули
        x = self.pos[0] - self.rect.x
        y = self.pos[1] - self.rect.y
        if x == 0 and y == 0:
            self.kill()
        k = pow((x * x + y * y), 0.5) // self.speed
        if not k:
            k = 1
        self.nx = x / k  # локальные nx и ny
        self.ny = y / k
        self.local_ms += ms

    # перестало работать после анимации
    def bulletRotate(self):
        x1 = 0
        y1 = self.pos[1] - self.rect.y
        x2 = self.pos[0] - self.rect.x
        y2 = self.pos[1] - self.rect.y
        cosa = (x1 * x2 + y1 * y2)  / ((math.sqrt(x1 * x1 + y1 * y1) * math.sqrt(x2 * x2 + y2 * y2)))
        angle = math.acos(cosa) * 57.2958
        if self.rect.x < self.pos[0]:
            angle *= -1
        if self.rect.y < self.pos[1]:
            angle = 180 - angle
        self.anim.rotate(angle + 180)
        self.local_ms = 0

    def update(self, ms, enemies):
        self.anim.update(ms)
        self.image = self.anim.image
        self.aim(ms)
        self.rect.x += self.nx
        self.rect.y += self.ny
        self.hitting(enemies)

    def hitting(self, enemies):
        for enemy in enemies:
            if pygame.sprite.collide_circle(enemy, self):   
                if self.type == 'splash':
                    for block in enemies:
                        if math.sqrt((block.rect.center[0] - enemy.rect.center[0]) ** 2 + (block.rect.center[1] - enemy.rect.center[1]) ** 2) < self.aoe:
                            block.hp -= self.dmg // 2
                    enemy.hp -= self.dmg
                    self.anim.paused = False
                if self.type == 'arch':
                    enemy.hp -= self.dmg
                    self.anim.paused = False


        if self.anim.finished:
            self.kill()

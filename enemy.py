import pygame
from config import *
from levels import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Enemy, self).__init__()
        self.pic = pygame.image.load(image)
        self.pic = pygame.transform.scale(self.pic, (SIZE[0], SIZE[1]))
        self.pic.convert_alpha()
        self.image = pygame.Surface((SIZE[0], SIZE[1] + 18), 
                            pygame.SRCALPHA | pygame.HWSURFACE)
        self.image.blit(self.pic, (0, 18))
        self.image.convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.pic.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.hp = 30
        self.hp_fix = self.hp
        self.vel_x = 3
        self.path = level1
        self.vel_y = 3

    def update(self):
        self.dead()
        self.moving()
        self.health_bar()
        # print(self.rect.x, " ", self.rect.y)
        
    def moving(self):       # переписать этот метод, а то это полное говно
        '''for dot in self.path:
            while True:
                if self.rect.x < dot[0]:
                    self.rect.x += self.vel_x
                elif self.rect.x > dot[0]:
                    self.rect.x -= self.vel_x
                if self.rect.y > dot[1]:
                    self.rect.y -= self.vel_y
                elif self.rect.y < dot[1]:
                    self.rect.y += self.vel_y
                    '''
        if self.rect.y > 0:
            self.rect.y -= self.vel_y

        if self.rect.y <= 0:
            self.rect.y = 0

        if self.rect.y == 0 and self.rect.x < 800:
            self.rect.x += self.vel_x

        if self.rect.right >= 800:
            self.rect.right = 800

        if self.rect.y <= 600 and self.rect.right == 800:
            self.rect.top += 2 * self.vel_y
            print(1)

        if self.rect.bottom >= 600:
            exit()

    def dead(self):
        if self.hp <= 0:
            self.kill()

    def health_bar(self):
        height = 10 
        width = (self.hp * self.rect.width) / self.hp_fix
        pygame.draw.line(self.image, (200, 0, 0), (0, 0), (self.rect.width, 0), height)
        pygame.draw.line(self.image, (0, 200, 0), (0,0), (width, 0), height)



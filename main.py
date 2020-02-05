import pygame
from pygame.locals import *
from config import *
from enemy import *
from tower import *


class Game(object):
    def __init__(self):
        super(Game, self).__init__()
        pygame.init()
        self.display = pygame.display.set_mode(WIN_SIZE)
        self.display.fill((255, 255, 255))
        self.clock = pygame.time.Clock()
        self.running = True
        self.background = pygame.image.load(BG)
        self.background = pygame.transform.scale(self.background, WIN_SIZE)
        self.ms = 0
        self.towers = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        newEnemy = Enemy(0, 500, enemy)
        newEnemy.add(self.enemys)
        self.bullets = pygame.sprite.Group()
        self.hp = 20

    def creating_towers(self):  # должен в будущем принимать координаты при нажатии
        x = 100
        y = 100
        for i in range(2):
            newTower = Tower(x, y, tower)
            self.towers.add(newTower)
            x += 500

    def render(self):
        self.display.blit(self.background, (0, 0))
        self.towers.draw(self.display)
        self.enemys.draw(self.display)
        self.bullets.draw(self.display)
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

    def update(self):
        ms = self.clock.tick(FPS)
        self.enemys.update()
        self.towers.update(self.enemys, self.bullets, ms)
        self.bullets.update()

    def run(self):
        self.creating_towers()
        while self.running:
            self.events()
            self.update()
            self.render()


if __name__ == '__main__':
    Game().run()

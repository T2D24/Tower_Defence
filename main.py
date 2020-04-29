import pygame
from time import time
from pygame.locals import *
from config import *
from enemy import *
from tower import *
from shop import *
from platform import  *


# уровни и шоп
class Game(object):
    def __init__(self):
        super(Game, self).__init__()
        pygame.init()
        self.display = pygame.display.set_mode(WIN_SIZE)
        self.display.fill((255, 255, 255))
        self.clock = pygame.time.Clock()
        self.running = True
        self.platforms = pygame.sprite.Group()
        self.background = pygame.image.load(BG)
        self.background = pygame.transform.scale(self.background, WIN_SIZE)
        self.ms = 0
        self.towers = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        newEnemy = Enemy(0, 500)
        newEnemy.add(self.enemies)
        self.bullets = pygame.sprite.Group()
        self.coins = 2300
        self.buttons = pygame.sprite.Group()
        self.lives = 20
        self.show_shop = False
        self.spawn_time = 0
        self.new_shop = 0
        self.myfont = pygame.font.SysFont('arial', 33)
        self.load_map()
        
    def load_map(self):
        file = open('level.txt')
        A = pygame.image.load('assets/map-tiles/1.png')
        A = pygame.transform.scale(A, (WIN_SIZE[0] // 16, WIN_SIZE[1] // 9))
        B = pygame.image.load('assets/map-tiles/9.png')
        B = pygame.transform.scale(B, (WIN_SIZE[0] // 16, WIN_SIZE[1] // 9))
        V = pygame.image.load('assets/map-tiles/3.png')
        V = pygame.transform.scale(V, (WIN_SIZE[0] // 16, WIN_SIZE[1] // 9))
        C = pygame.image.load('assets/map-tiles/4.png')
        C = pygame.transform.scale(C, (WIN_SIZE[0] // 16, WIN_SIZE[1] // 9))
        for y1, line in enumerate(file):
            for x1, letter in enumerate(line.strip()):
                if letter == 'A':
                    self.display.blit(A, (x1 * (WIN_SIZE[0] // 16), y1 * (WIN_SIZE[1] // 9)))
                if letter == 'B':
                    self.display.blit(B, (x1 * (WIN_SIZE[0] // 16), y1 * (WIN_SIZE[1] // 9)))
                if letter == 'C':
                    self.display.blit(C, (x1 * (WIN_SIZE[0] // 16), y1 * (WIN_SIZE[1] // 9)))
                if letter == 'V':
                    self.display.blit(V, (x1 * (WIN_SIZE[0] // 16), y1 * (WIN_SIZE[1] // 9)))

    def creating_towers(self):  # должен в будущем принимать координаты при нажатии
        file = open('level.txt')
        for y1, line in enumerate(file):
            for x1, letter in enumerate(line.strip()):
                if letter == 'T':
                    self.platforms.add(Platform((x1 * WIN_SIZE[0] // 16, y1 * (WIN_SIZE[1] // 9)), PLATFORM))

        for block in self.towers:
            self.buttons.add(block.button)
    # КООООРДИНАТЫ НЕ РАБОТАЮ ГАД ДАМН ИТ БОЙ
    def create_mobs(self, ms):
        self.spawn_time += ms
        if self.spawn_time > SPAWN_RATE:
            self.enemies.add(Enemy(0, 0))
            self.spawn_time = 0

    def render_cost(self):
        for button in self.buttons:
            button.draw_cost(self.display)

    #def start_shop(self):
     #   pos = pygame.mouse.get_pos()
      #  self.new_shop = Shop(pos, SHOP)
       # self.new_shop.draw_shop(self.display)

    def render(self):
        #self.display.blit(self.background, (0, 0))
        pygame.display.set_caption(str(self.clock.get_fps()))
        self.load_map()
        self.towers.draw(self.display)
        self.enemies.draw(self.display)
        self.buttons.draw(self.display)
        self.bullets.draw(self.display)
        lives = self.myfont.render("Lives: " + str(self.lives), False, (0, 0, 0))
        coins = self.myfont.render("Coins: " + str(self.coins), False, (0, 0, 0))
        self.display.blit(lives, (WIN_SIZE[0] // 2.5, WIN_SIZE[1] * 0.8))
        self.display.blit(coins, (WIN_SIZE[0] // 2.5, WIN_SIZE[1] * 0.85))
        self.render_cost()
        self.draw_t_radius()
        if self.show_shop:
            self.new_shop.draw_shop(self.display)
        if self.lives <= 0:
            self.draw_death_screen()
        pygame.display.update()

    def events(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_b:
                        x = pos[0] - 50
                        y = pos[1] - 50
                        self.new_shop = Shop((x, y), SHOP)
                        self.show_shop = not self.show_shop
                        if not self.show_shop:
                            self.new_shop.kill()

            if event.type == QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN and self.new_shop != 0:
                if self.new_shop.rect.right // 4 < pos[0] > self.new_shop.rect.left and self.coins >= 100 and self.show_shop:
                    self.coins = self.new_shop.buy_tower(self.coins, self.towers)
                    for block in self.towers:
                        self.buttons.add(block.button)
                    self.new_shop.kill()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.rect.left <= pos[0] <= button.rect.right and button.rect.top <= pos[1] <= button.rect.bottom\
                            and self.coins >= button.tower.upgrade_cost:
                        self.coins -= button.tower.upgrade_cost
                        button.clicked()



    # def menu_get_events(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             self.menu_running = False
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_ESCAPE:
    #                 self.menu_running = False
    #         if event.type == pygame.KEYUP:
    #             if event.key == pygame.K_p:
    #                 self.running = True
    #                 self.run()

    def draw_death_screen(self):
        self.display.fill((0, 0, 0))
        myfont = pygame.font.SysFont('arial', 55)
        dead_text = myfont.render('YOU LOSE', False, (255, 0, 0))
        self.display.blit(dead_text, (WIN_SIZE[0] // 2.5, WIN_SIZE[1] // 2.5))

    def menu_draw(self):
        self.display.blit(self.background, (0, 0))
        play_text = self.myfont.render('Press P to play', False, (0, 0, 0))
        exit_text = self.myfont.render('Press ESC to exit', False, (0, 0, 0))
        self.display.blit(play_text, (WIN_SIZE[0] // 25, WIN_SIZE[1] // 10))
        self.display.blit(exit_text, (WIN_SIZE[0] // 25, WIN_SIZE[1] // 6))
        pygame.display.update()

    def menu(self):
        self.menu_running = True
        while self.menu_running:
            self.menu_get_events()
            self.menu_draw()

    def draw_t_radius(self):
        for tower in self.towers:
            tower.draw_circle(self.display)

    def update(self):
        ms = self.clock.tick(FPS)
        for block in self.enemies:
            block.health_bar()
            if block.dead() == (1, None):
                self.coins += block.reward
            if block.moving() == (1, None):
                self.lives -= block.dmg
        for button in self.buttons:
            if self.coins < button.tower.upgrade_cost:
                button.image = pygame.image.load(CUPGRADE)
                button.image = pygame.transform.scale(button.image, BUTTON_SIZE).convert_alpha()
            else:
                button.image = pygame.image.load(UPGRADE)
                button.image = pygame.transform.scale(button.image, BUTTON_SIZE).convert_alpha()
        

        self.enemies.update(ms)
        self.towers.update( self.bullets, ms, self.display)
        self.bullets.update(ms, self.enemies)
        self.create_mobs(ms)

        # print(self.coins)

    def run(self):
        self.creating_towers()
        while self.running:
            self.events()
            self.update()
            self.render()


if __name__ == '__main__':
    Game().run()

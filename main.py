import pygame
from time import time
from pygame.locals import *
from config import *
from enemy import *
from tower import *

# уровни и шоп
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
        self.enemies = pygame.sprite.Group()
        newEnemy = Enemy(0, 500)
        newEnemy.add(self.enemies)
        self.bullets = pygame.sprite.Group()
        self.coins = 2300
        self.buttons = pygame.sprite.Group()
        self.lives = 20
        self.show_shop = False
        self.spawn_time = 0
        self.myfont = pygame.font.SysFont('arial', 33)

    def creating_towers(self):  # должен в будущем принимать координаты при нажатии
        x = 300
        y = 100
        for _ in range(2):
            self.towers.add(Tower(x, y, tower))
            x += 300

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

    def draw_shop(self):
        pass

    def render(self):
        self.display.blit(self.background, (0, 0))
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
            pygame.draw.polygon(self.display, (255, 255, 255),
                                [(0, 3 * WIN_SIZE[1] // 4), (0, WIN_SIZE[1]), (WIN_SIZE[0], WIN_SIZE[1]),
                                 (WIN_SIZE[0], 3 * WIN_SIZE[1] // 4)
                                 ])
        if self.lives <= 0:
            self.draw_death_screen()
        pygame.display.update()

    def events(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_b:
                    self.show_shop = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.rect.left <= pos[0] <= button.rect.right and button.rect.top <= pos[1] <= button.rect.bottom\
                            and self.coins >= button.tower.upgrade_cost:
                        self.coins -= button.tower.upgrade_cost
                        button.clicked()
                        print(button.tower.upgrade_cost)
        if pygame.key.get_pressed()[pygame.K_b] and self.show_shop:
            self.show_shop = False

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
                button.image = pygame.image.load(cupgrade)
                button.image = pygame.transform.scale(button.image, BUTTON_SIZE).convert_alpha()
            else:
                button.image = pygame.image.load(upgrade)
                button.image = pygame.transform.scale(button.image, BUTTON_SIZE).convert_alpha()
        

        self.enemies.update(ms)
        self.towers.update(self.enemies, self.bullets, ms, self.display)
        self.bullets.update(ms)
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

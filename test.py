import pygame
import os

WIN_SIZE = (480, 480)
FPS = 30

currentDir = os.path.dirname(__file__)
assets = os.path.join(currentDir, 'assets')
enemies = os.path.join(assets, 'enemies_walk')
enemy_1 = os.path.join(enemies, 'enemy_1')

images = [enemy_1 + '\9_enemies_1_walk_000.png', 
          enemy_1 + '\9_enemies_1_walk_001.png', 
          enemy_1 + '\9_enemies_1_walk_002.png', 
          enemy_1 + '\9_enemies_1_walk_003.png', 
          enemy_1 + '\9_enemies_1_walk_004.png', 
          enemy_1 + '\9_enemies_1_walk_005.png', 
          enemy_1 + '\9_enemies_1_walk_006.png', 
          enemy_1 + '\9_enemies_1_walk_007.png', 
          enemy_1 + '\9_enemies_1_walk_008.png', 
          enemy_1 + '\9_enemies_1_walk_009.png', 
          enemy_1 + '\9_enemies_1_walk_010.png', 
          enemy_1 + '\9_enemies_1_walk_011.png', 
          enemy_1 + '\9_enemies_1_walk_012.png', 
          enemy_1 + '\9_enemies_1_walk_013.png', 
          enemy_1 + '\9_enemies_1_walk_014.png', 
          enemy_1 + '\9_enemies_1_walk_015.png', 
          enemy_1 + '\9_enemies_1_walk_016.png',
          enemy_1 + '\9_enemies_1_walk_017.png',
          enemy_1 + '\9_enemies_1_walk_018.png',
          enemy_1 + '\9_enemies_1_walk_019.png',]

class Game(object):
    def __init__(self):
        super(Game, self).__init__()
        self.display = pygame.display.set_mode(WIN_SIZE)
        self.display.fill((255, 255, 255))
        self.clock = pygame.time.Clock()
        self.tiles = []
        self.time = 0
        self.loadFromFiles(images)

    def loadFromFiles(self, images):
        for image in images:
            self.pic = pygame.image.load(image)
            self.pic = pygame.transform.scale(self.pic, (100, 100))
            self.pic.convert_alpha()
            self.tiles.append(self.pic)

    def anim(self, picIter):
        self.image = pygame.Surface((100, 100), 
                            pygame.SRCALPHA | pygame.HWSURFACE)
        self.image.fill((255, 255, 255))
        self.image.blit(self.tiles[picIter], (0, 0))
        self.image.convert_alpha()

    def update(self):
        ms = self.clock.tick(FPS)
        self.time += ms
        if self.time // FPS >= 20:
            self.time = 0
        self.anim(self.time // FPS)

    def render(self):
        self.display.fill((255, 255, 255))
        self.display.blit(self.image, (100, 100))
        pygame.display.update()


    def run(self):
        while True:
            self.update()
            self.render()

if __name__ == '__main__':
    Game().run()



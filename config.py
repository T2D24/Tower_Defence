import os

WIN_SIZE = (1200, 900)
SIZE = (64, 64)
FPS = 30
BUTTON_SIZE = (26, 25)

currentDir = os.path.dirname(__file__)
assets = os.path.join(currentDir, 'assets')
SPAWN_RATE = 4000
tower = os.path.join(assets, 'tower.png')
enemy = os.path.join(assets, 'enemy.png')
BG = os.path.join(assets, 'bg.png')
upgrade = os.path.join(assets, 'upgrade.png')
cupgrade = os.path.join(assets, 'cupgrade.png')
bulletImg = os.path.join(assets, 'enemy.png')

enemies = os.path.join(assets, 'enemies_walk')
enemy_1 = os.path.join(enemies, 'enemy_1')

bullets = os.path.join(assets, 'bullets')
fireball = os.path.join(bullets, 'fireball')


ENEMY_1_WALK = [enemy_1 + '/9_enemies_1_walk_000.png', 
                enemy_1 + '/9_enemies_1_walk_001.png', 
                enemy_1 + '/9_enemies_1_walk_002.png', 
                enemy_1 + '/9_enemies_1_walk_003.png', 
                enemy_1 + '/9_enemies_1_walk_004.png', 
                enemy_1 + '/9_enemies_1_walk_005.png', 
                enemy_1 + '/9_enemies_1_walk_006.png', 
                enemy_1 + '/9_enemies_1_walk_007.png', 
                enemy_1 + '/9_enemies_1_walk_008.png', 
                enemy_1 + '/9_enemies_1_walk_009.png', 
                enemy_1 + '/9_enemies_1_walk_010.png', 
                enemy_1 + '/9_enemies_1_walk_011.png', 
                enemy_1 + '/9_enemies_1_walk_012.png', 
                enemy_1 + '/9_enemies_1_walk_013.png', 
                enemy_1 + '/9_enemies_1_walk_014.png', 
                enemy_1 + '/9_enemies_1_walk_015.png', 
                enemy_1 + '/9_enemies_1_walk_016.png',
                enemy_1 + '/9_enemies_1_walk_017.png',
                enemy_1 + '/9_enemies_1_walk_018.png',
                enemy_1 + '/9_enemies_1_walk_019.png',]

FIREBALL_BLOWUP = [fireball + '/1.png',
                   fireball + '/2.png',
                   fireball + '/3.png',
                   fireball + '/4.png',
                   fireball + '/5.png']

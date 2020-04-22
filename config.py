import os

WIN_SIZE = (1600, 900)
SIZE = (64, 64)
FPS = 40
BUTTON_SIZE = (26, 25)
SHOP_SIZE = (128, 128)
currentDir = os.path.dirname(__file__)
assets = os.path.join(currentDir, 'assets')
SPAWN_RATE = 2000
TOWER = os.path.join(assets, 'tower.png')
SHOP = os.path.join(assets, 'shop.png')
ENEMY = os.path.join(assets, 'enemy.png')
BG = os.path.join(assets, 'bg.png')
UPGRADE = os.path.join(assets, 'upgrade.png')
CUPGRADE = os.path.join(assets, 'cupgrade.png')
BULLET_IMG = os.path.join(assets, 'enemy.png')

enemies = os.path.join(assets, 'enemies_walk')
enemy_1 = os.path.join(enemies, 'enemy_1')
enemy_2 = os.path.join(enemies, 'enemy_2')

bullets = os.path.join(assets, 'bullets')
fireball = os.path.join(bullets, 'fireball')
stone = os.path.join(bullets, 'stone')

towers = os.path.join(assets, 'towers')
tower_1 = os.path.join(towers, 'tower_1')


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

ENEMY_2_WALK = [enemy_2 + '/1_enemies_1_walk_001.png',
                enemy_2 + '/1_enemies_1_walk_002.png',
                enemy_2 + '/1_enemies_1_walk_003.png',
                enemy_2 + '/1_enemies_1_walk_004.png',
                enemy_2 + '/1_enemies_1_walk_005.png',
                enemy_2 + '/1_enemies_1_walk_006.png',
                enemy_2 + '/1_enemies_1_walk_007.png',
                enemy_2 + '/1_enemies_1_walk_008.png',
                enemy_2 + '/1_enemies_1_walk_009.png',
                enemy_2 + '/1_enemies_1_walk_010.png',
                enemy_2 + '/1_enemies_1_walk_011.png',
                enemy_2 + '/1_enemies_1_walk_012.png',
                enemy_2 + '/1_enemies_1_walk_013.png',
                enemy_2 + '/1_enemies_1_walk_014.png',
                enemy_2 + '/1_enemies_1_walk_015.png',
                enemy_2 + '/1_enemies_1_walk_016.png',
                enemy_2 + '/1_enemies_1_walk_017.png',
                enemy_2 + '/1_enemies_1_walk_018.png',
                enemy_2 + '/1_enemies_1_walk_019.png',]

FIREBALL_BLOWUP = [fireball + '/1.png',
                   fireball + '/2.png',
                   fireball + '/3.png',
                   fireball + '/4.png',
                   fireball + '/5.png']

STONE_BLOWUP = [stone + '/29.png',
                stone + '/30.png',
                stone + '/31.png',
                stone + '/32.png',
                stone + '/33.png',
                stone + '/34.png',]

TOWER_1 = [tower_1 + '/2.png',
           tower_1 + '/3.png',
           tower_1 + '/4.png',
           tower_1 + '/5.png',
           tower_1 + '/6.png',
           tower_1 + '/7.png',
           tower_1 + '/8.png',
           tower_1 + '/9.png',
           tower_1 + '/10.png',
           tower_1 + '/11.png',
           tower_1 + '/12.png',
           tower_1 + '/13.png',
           tower_1 + '/14.png',
           tower_1 + '/15.png',
           tower_1 + '/16.png',
           tower_1 + '/17.png',
           tower_1 + '/18.png',
           tower_1 + '/19.png',
           tower_1 + '/20.png',
           tower_1 + '/21.png',
           tower_1 + '/22.png',]

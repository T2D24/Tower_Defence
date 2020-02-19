import os

WIN_SIZE = (800, 600)
SIZE = (32, 32)
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

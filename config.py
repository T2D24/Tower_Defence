import os

WIN_SIZE = (800, 600)
SIZE = (32, 32)
FPS = 30

currentDir = os.path.dirname(__file__)
assets = os.path.join(currentDir, 'assets')

tower = os.path.join(assets, 'tower.png')
enemy = os.path.join(assets, 'enemy.png')
BG = os.path.join(assets, 'bg.png')
bulletImg = os.path.join(assets, 'enemy.png')

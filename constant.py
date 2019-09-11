import pygame

GAME_DISPLAY = pygame.display.set_mode((425, 475))
# seringe_img = pygame.image.load(os.path.join('ressource', 'seringue.png'))
# needle_img = pygame.image.load(os.path.join('ressource', 'aiguille.png'))
# plastic_tube_img = pygame.image.load(os.path.join('ressource', 'tube_plastique.png'))
# ether_img = pygame.image.load(os.path.join('ressource', 'ether.png'))
# mc_gyver_img = pygame.image.load(os.path.join('ressource', 'MacGyver.png'))
# floor_img = pygame.image.load(os.path.join('ressource', 'floor.png'))
# background_color = pygame.Color(0, 0, 0)
MAZE = []
grid = open("labyrinth.txt", "r")
for line in grid:
    a = line.replace("/n", "")
    raw = a.split()
    for case in raw:
        col = case.split(",")
    MAZE.append(col)
grid.close()

YELLOW = pygame.Color(255, 255, 0)
GREEN = pygame.Color(75, 181, 67)
RED = pygame.Color(255, 0, 0)
SCREENABLE = 25

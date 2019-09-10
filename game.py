"""Here is the Labyrinth :
first i created a 2d list first list is the raw and second the col.
Then i choose letter and numbers to set the labyrinth.
"""
import os
import random
import pygame
import time

seringe_img = pygame.image.load(os.path.join('ressource', 'seringue.png'))
needle_img = pygame.image.load(os.path.join('ressource', 'aiguille.png'))
plastic_tube_img = pygame.image.load(os.path.join('ressource', 'tube_plastique.png'))
ether_img = pygame.image.load(os.path.join('ressource', 'ether.png'))
mc_gyver_img = pygame.image.load(os.path.join('ressource', 'MacGyver.png'))
guard_img = pygame.image.load(os.path.join('ressource', 'Gardien.png'))

yellow = pygame.Color(255, 255, 0)
green = pygame.Color(75, 181, 67)
red = pygame.Color(255, 0, 0)

class Objet:
    TAKEN = False

    def __init__(self, pos_x = 0, pos_y = 0):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw_objet(self, image):
        sprite(image, self.pos_x * 25, self.pos_y * 25)
    

class Heros:

    OBJECTCOUNT = 0

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 2
    
    def draw_hero(self, image):
        sprite(image, self.pos_x * 25, self.pos_y * 25)
    
    def take_object(self, objet):
        self.OBJECTCOUNT += 1
        print("Objet collécté :" + str(self.OBJECTCOUNT))
           
class Badguy:

    def __init__(self):
        self.pos_x = 16
        self.pos_y = 10

    def draw_bad_guy(self, image):
        sprite(image, self.pos_x * 25, self.pos_y * 25)


GRID = []

maze = open("labyrinth.txt", "r")
for line in maze:
  a = line.replace("/n", "")
  raw = a.split()

  for case in raw:
    col = case.split(",")
  GRID.append(col)
maze.close()
print(GRID)

GAME_DISPLAY = pygame.display.set_mode((425, 475))
pygame.display.set_caption(("MacGyver ce héros"))

def random_position(grid):
    possible_position = []
    for INDEX_RAW, RAW in enumerate(grid):
        for INDEX_COL, COL in enumerate(grid[INDEX_RAW]):
            CASE_VALUE = grid[INDEX_RAW][INDEX_COL]
            if CASE_VALUE == '0':
                possible_position.append([INDEX_RAW, INDEX_COL])
    return possible_position

macGyver = Heros()
guard = Badguy()
seringe = Objet()
needle = Objet()
ether = Objet()
plastic = Objet()

position_object_1 = random.choice(random_position(GRID))

seringe.pos_x = position_object_1[1]
seringe.pos_y = position_object_1[0]
# GRID[POSITION_SERINGE_Y][POSITION_SERINGE_X] = "N"

position_object_2 = random.choice(random_position(GRID))
needle.pos_x = position_object_2[1]
needle.pos_y = position_object_2[0]
# GRID[POSITION_NEEDLE_Y][POSITION_NEEDLE_X] = "N"

position_object_3 = random.choice(random_position(GRID))
ether.pos_x = position_object_3[1]
ether.pos_y = position_object_3[0]
# GRID[POSITION_ETHER_Y][POSITION_ETHER_X] = "N"

position_object_4 = random.choice(random_position(GRID))
plastic.pos_x = position_object_4[1]
plastic.pos_y = position_object_4[0]
# GRID[POSITION_PLASTIC_Y][POSITION_PLASTIC_X] = "N"

def sprite(wall_image, pos_x, pos_y):
    """display the right sprite in the right position
    """
    GAME_DISPLAY.blit(wall_image, (pos_x, pos_y))

def text(msg,color):
    screen_text = pygame.font.SysFont('Arial', 25).render(msg, True, color)
    GAME_DISPLAY.blit(screen_text, (1 * 25, 17 * 25))

def end_game(msg, color):
    GAME_DISPLAY.fill((0, 0, 0))
    screen_text = pygame.font.SysFont('Arial', 25).render(msg, True, color)
    GAME_DISPLAY.blit(screen_text, (425/2, 425/2))
    pygame.display.update()

def draw():

    TOP_LEFT_CORNER = pygame.image.load(os.path.join('ressource', 'TopLeftCorner.png'))
    TOP_RIGHT_CORNER = pygame.image.load(os.path.join('ressource', 'TopRightCorner.png'))
    TOP_MIDDLE = pygame.image.load(os.path.join('ressource', 'MiddleTop.png'))
    BOTTOM_RIGHT_CORNER = pygame.image.load(os.path.join('ressource', 'BottomRigthCorner.png'))
    BOTTOM_LEFT_CORNER = pygame.image.load(os.path.join('ressource', 'BottomLeftCorner.png'))
    BOTTOM_MIDDLE = pygame.image.load(os.path.join('ressource', 'MiddleBot.png'))
    LEFT_MIDDLE = pygame.image.load(os.path.join('ressource', 'MiddleLeft.png'))
    RIGHT_MIDDLE = pygame.image.load(os.path.join('ressource', 'MiddleRight.png'))
    MAZE_WALL = pygame.image.load(os.path.join('ressource', 'wall.png'))

    # seringe_img = pygame.image.load(os.path.join('ressource', 'seringue.png'))
    # needle_img = pygame.image.load(os.path.join('ressource', 'aiguille.png'))
    # plastic_tube_img = pygame.image.load(os.path.join('ressource', 'tube_plastique.png'))
    # ether_img = pygame.image.load(os.path.join('ressource', 'ether.png'))
    # mc_gyver_img = pygame.image.load(os.path.join('ressource', 'MacGyver.png'))
    
    
    GAME_DISPLAY.fill((0, 0, 0))
    for INDEX_RAW, RAW in enumerate(GRID):
        for INDEX_COL, COL in enumerate(GRID[INDEX_RAW]):
            CASE_VALUE = GRID[INDEX_RAW][INDEX_COL]
            SCREEN_RAW = INDEX_COL * 25
            SCREEN_COL = INDEX_RAW * 25
            if CASE_VALUE == '1':
                sprite(TOP_MIDDLE, SCREEN_RAW, SCREEN_COL)
              
            elif CASE_VALUE == '2':
                sprite(TOP_LEFT_CORNER, SCREEN_RAW, SCREEN_COL)
          
            elif CASE_VALUE == '3':
                sprite(BOTTOM_LEFT_CORNER, SCREEN_RAW, SCREEN_COL)
     
            elif CASE_VALUE == '4':
                sprite(BOTTOM_RIGHT_CORNER, SCREEN_RAW, SCREEN_COL)
                
            elif CASE_VALUE == '5':
                sprite(TOP_RIGHT_CORNER, SCREEN_RAW, SCREEN_COL)
          
            elif CASE_VALUE == '6':
                sprite(LEFT_MIDDLE, SCREEN_RAW, SCREEN_COL)
                
            elif CASE_VALUE == '7':
                sprite(RIGHT_MIDDLE, SCREEN_RAW, SCREEN_COL)

                # elif CASE_VALUE == 8:
                #     sprite(RightMiddle, SCREEN_RAW, SCREEN_COL)
            elif CASE_VALUE == 'X':
                sprite(BOTTOM_MIDDLE, SCREEN_RAW, SCREEN_COL)
               
            elif CASE_VALUE == 'M':
                sprite(MAZE_WALL, SCREEN_RAW, SCREEN_COL)
             
    seringe.draw_objet(seringe_img)
    needle.draw_objet(needle_img)
    plastic.draw_objet(plastic_tube_img)
    ether.draw_objet(ether_img)

    macGyver.draw_hero(mc_gyver_img)
    guard.draw_bad_guy(guard_img)
    
    text("ITEM:", yellow)
    pygame.display.update()

gameOn = True
while gameOn:
    pygame.init()
    draw()

   
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        control = pygame.key.get_pressed()

        if control[pygame.K_LEFT] and GRID[macGyver.pos_y][macGyver.pos_x - 1] == '0' :
            macGyver.pos_x -= 1
        if control[pygame.K_RIGHT] and GRID[macGyver.pos_y][macGyver.pos_x + 1] == '0':
            macGyver.pos_x += 1
        if control[pygame.K_UP] and GRID[macGyver.pos_y - 1][macGyver.pos_x] == '0':
            macGyver.pos_y -= 1
        if control[pygame.K_DOWN] and GRID[macGyver.pos_y + 1][macGyver.pos_x] == '0':
            macGyver.pos_y += 1

        if macGyver.pos_x == plastic.pos_x and macGyver.pos_y == plastic.pos_y and plastic.TAKEN == False:
            macGyver.take_object(plastic)
            plastic.pos_x = 4 * 25
            plastic.pos_y = 17 * 25
            plastic.TAKEN = True
            plastic.draw_objet(plastic_tube_img)

        if macGyver.pos_x == seringe.pos_x and macGyver.pos_y == seringe.pos_y and seringe.TAKEN == False:
            macGyver.take_object(seringe)
            seringe.pos_x = 6 * 25
            seringe.pos_y = 17 * 25
            seringe.TAKEN = True
        
        if macGyver.pos_x == ether.pos_x and macGyver.pos_y == ether.pos_y and ether.TAKEN == False:
            macGyver.take_object(ether)
            ether.pos_x = 8 * 25
            ether.pos_y = 17 * 25
            ether.TAKEN = True
            
        if macGyver.pos_x == needle.pos_x and macGyver.pos_y == needle.pos_y and needle.TAKEN == False:
            macGyver.take_object(needle)
            needle.pos_x = 10 * 25
            needle.pos_y = 17 * 25
            needle.TAKEN = True
        
        if macGyver.pos_x == guard.pos_x and guard.pos_y == guard.pos_y and macGyver.OBJECTCOUNT >= 3:
            gameOn = False
            end_game("GAGNÉ", green)
            time.sleep(4)

        elif macGyver.pos_x == guard.pos_x and guard.pos_y == guard.pos_y and macGyver.OBJECTCOUNT < 3:
            gameOn = False
            end_game("PERDU", red)
            time.sleep(4)

        
        
pygame.display.update()
    
            
            


"""Here is the Labyrinth :
first i created a 2d list first list is the raw and second the col.
Then i choose letter and numbers to set the labyrinth.
"""
import constant
import os
import random
import pygame
import time

class Objet:
    TAKEN = False

    def __init__(self, pos_x=0, pos_y=0):
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

def random_position(grid):
    possible_position = []
    for index_raw, raw in enumerate(grid):
        for index_col, col in enumerate(grid[index_raw]):
            case_value = grid[index_raw][index_col]
            if case_value == '0':
                possible_position.append([index_raw, index_col])
    return possible_position

def sprite(wall_image, pos_x, pos_y):
    """display the right sprite in the right position
    """
    constant.GAME_DISPLAY.blit(wall_image, (pos_x, pos_y))

def text(msg, color):
    screen_text = pygame.font.SysFont('Arial', 25).render(msg, True, color)
    constant.GAME_DISPLAY.blit(screen_text, (1 * 25, 17 * 25))

def end_game(msg, color):
    constant.GAME_DISPLAY.fill((0, 0, 0))
    screen_text = pygame.font.SysFont('Arial', 25).render(msg, True, color)
    constant.GAME_DISPLAY.blit(screen_text, (425/2, 425/2))
    pygame.display.update()

macGyver = Heros()
guard = Badguy()
seringe = Objet()
needle = Objet()
ether = Objet()
plastic = Objet()
position_object_1 = random.choice(random_position(constant.MAZE))
seringe.pos_x = position_object_1[1]
seringe.pos_y = position_object_1[0]

position_object_2 = random.choice(random_position(constant.MAZE))
needle.pos_x = position_object_2[1]
needle.pos_y = position_object_2[0]

position_object_3 = random.choice(random_position(constant.MAZE))
ether.pos_x = position_object_3[1]
ether.pos_y = position_object_3[0]

position_object_4 = random.choice(random_position(constant.MAZE))
plastic.pos_x = position_object_4[1]
plastic.pos_y = position_object_4[0]
def labyrinth():

    seringe_img = pygame.image.load(os.path.join('ressource', 'seringue.png'))
    needle_img = pygame.image.load(os.path.join('ressource', 'aiguille.png'))
    plastic_tube_img = pygame.image.load(os.path.join('ressource', 'tube_plastique.png'))
    ether_img = pygame.image.load(os.path.join('ressource', 'ether.png'))
    mc_gyver_img = pygame.image.load(os.path.join('ressource', 'MacGyver.png'))
    guard_img = pygame.image.load(os.path.join('ressource', 'Gardien.png'))

    top_left_corner = pygame.image.load(os.path.join('ressource', 'TopLeftCorner.png'))
    top_right_corner = pygame.image.load(os.path.join('ressource', 'TopRightCorner.png'))
    top_middle = pygame.image.load(os.path.join('ressource', 'MiddleTop.png'))
    bot_right_corner = pygame.image.load(os.path.join('ressource', 'BottomRigthCorner.png'))
    bot_left_corner = pygame.image.load(os.path.join('ressource', 'BottomLeftCorner.png'))
    bot_middle = pygame.image.load(os.path.join('ressource', 'MiddleBot.png'))
    left_middle = pygame.image.load(os.path.join('ressource', 'MiddleLeft.png'))
    right_middle = pygame.image.load(os.path.join('ressource', 'MiddleRight.png'))
    maze_wall = pygame.image.load(os.path.join('ressource', 'wall.png'))

    constant.GAME_DISPLAY.fill((0, 0, 0))
    for index_raw, raw in enumerate(constant.MAZE):
        for index_col, col in enumerate(constant.MAZE[index_raw]):
            case_value = constant.MAZE[index_raw][index_col]
            screen_raw = index_col * 25
            screen_col = index_raw * 25
            if case_value == '1':
                sprite(top_middle, screen_raw, screen_col)

            elif case_value == '2':
                sprite(top_left_corner, screen_raw, screen_col)

            elif case_value == '3':
                sprite(bot_left_corner, screen_raw, screen_col)
     
            elif case_value == '4':
                sprite(bot_right_corner, screen_raw, screen_col)

            elif case_value == '6':
                sprite(left_middle, screen_raw, screen_col)

            elif case_value == '5':
                sprite(top_right_corner, screen_raw, screen_col)

            elif case_value == '7':
                sprite(right_middle, screen_raw, screen_col)

            elif case_value == 'X':
                sprite(bot_middle, screen_raw, screen_col)

            elif case_value == 'M':
                sprite(maze_wall, screen_raw, screen_col)

    seringe.draw_objet(seringe_img)
    needle.draw_objet(needle_img)
    plastic.draw_objet(plastic_tube_img)
    ether.draw_objet(ether_img)

    macGyver.draw_hero(mc_gyver_img)
    guard.draw_bad_guy(guard_img)

    text("ITEM:", constant.YELLOW)
    # pygame.display.update()

gameOn = True
while gameOn:
    pygame.init()
    labyrinth()

   
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        control = pygame.key.get_pressed()

        if control[pygame.K_LEFT] and constant.MAZE[macGyver.pos_y][macGyver.pos_x - 1] == '0' :
            macGyver.pos_x -= 1
        if control[pygame.K_RIGHT] and constant.MAZE[macGyver.pos_y][macGyver.pos_x + 1] == '0':
            macGyver.pos_x += 1
        if control[pygame.K_UP] and constant.MAZE[macGyver.pos_y - 1][macGyver.pos_x] == '0':
            macGyver.pos_y -= 1
        if control[pygame.K_DOWN] and constant.MAZE[macGyver.pos_y + 1][macGyver.pos_x] == '0':
            macGyver.pos_y += 1

        if macGyver.pos_x == plastic.pos_x and macGyver.pos_y == plastic.pos_y and plastic.TAKEN == False:
            macGyver.take_object(plastic)
            plastic.pos_x = 4 * 25
            plastic.pos_y = 17 * 25
            plastic.TAKEN = True

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
            end_game("GAGNÉ", constant.GREEN)
            time.sleep(4)

        elif macGyver.pos_x == guard.pos_x and guard.pos_y == guard.pos_y and macGyver.OBJECTCOUNT < 3:
            gameOn = False
            end_game("PERDU", RED)
            time.sleep(4)

        
        
pygame.display.update()
    
            
            


"""Here is the Labyrinth :
first i created a 2d list first list is the raw and second the col.
Then i choose letter and numbers to set the labyrinth.
"""
import os
import random
import time
import pygame
import constant

class Item:
    """set of Items and method"""
    taken = False

    def __init__(self, pos_x=0, pos_y=0):
        """Create the item set his position to 0 by default"""
        self.pos_x = pos_x
        self.pos_y = pos_y

    def random_position(self, grid):
        """Set a random position to the item inside the grid"""
        possible_position = []
        for index_raw, _ in enumerate(grid):
            for index_col, _ in enumerate(grid[index_raw]):
                case_value = grid[index_raw][index_col]
                if case_value == '0':
                    possible_position.append([index_raw, index_col])

        position_object = random.choice(possible_position)
        self.pos_x = position_object[1]
        self.pos_y = position_object[0]

    def draw_objet(self, image):
        """draw the image in the screen"""
        sprite(image, self.pos_x * 25, self.pos_y * 25)

class Heros:
    """The hero class with all his function"""
    object_count = 0

    def __init__(self):
        """ we create the hero with the position of his start"""
        self.pos_x = 0
        self.pos_y = 2

    def draw_hero(self, image):
        """will dislay the hero on the screen "* 25"
        allow us to display the image at the right position """
        sprite(image, self.pos_x * 25, self.pos_y * 25)

    def take_object(self, item):
        """ Hero can take an item and it will change his position on the screen"""
        if self.pos_x == item.pos_x and self.pos_y == item.pos_y \
        and item.taken is False:
            item.pos_x = 1000 * 25
            item.pos_y = 1000 * 25
            item.taken = True
            self.object_count += 1
# class Badguy:

#     def __init__(self):
#         self.pos_x = 16
#         self.pos_y = 10

#     def draw_bad_guy(self, image):
#         sprite(image, self.pos_x * 25, self.pos_y * 25)


def sprite(wall_image, pos_x, pos_y):
    """display the right sprite in the right position
    """
    constant.GAME_DISPLAY.blit(wall_image, (pos_x, pos_y))

def text(msg, color):
    """display the Item section at the bottom of the screen"""

    screen_text = pygame.font.SysFont('Arial', 25).render(msg, True, color)
    constant.GAME_DISPLAY.blit(screen_text, (1 * 25, 17 * 25))

def end_game(msg, color):
    """Will display the right message wether the player won or lose"""
    constant.GAME_DISPLAY.fill((0, 0, 0))
    screen_text = pygame.font.SysFont('Arial', 25).render(msg, True, color)
    constant.GAME_DISPLAY.blit(screen_text, (425/2, 425/2))
    pygame.display.update()

guard_pos_x = 16
guard_pos_y = 10
MacGyver = Heros()
# Guard = Badguy()
Seringe = Item()
Needle = Item()
Ether = Item()
Plastic = Item()

Seringe.random_position(constant.MAZE)
Needle.random_position(constant.MAZE)
Ether.random_position(constant.MAZE)
Plastic.random_position(constant.MAZE)

def labyrinth():
    """Set the structure of the labyrinth from the grid in the constant file,
    each character will match a structure '0' is the path the player can move """

    structure = {
        'seringe_img': pygame.image.load(os.path.join('ressource', 'seringue.png')),
        'needle_img': pygame.image.load(os.path.join('ressource', 'aiguille.png')),
        'plastic_tube_img': pygame.image.load(os.path.join('ressource', 'tube_plastique.png')),
        'ether_img': pygame.image.load(os.path.join('ressource', 'ether.png')),
        'mc_gyver_img': pygame.image.load(os.path.join('ressource', 'MacGyver.png')),
        'guard_img': pygame.image.load(os.path.join('ressource', 'Gardien.png')),
        'top_left_corner': pygame.image.load(os.path.join('ressource', 'TopLeftCorner.png')),
        'top_right_corner': pygame.image.load(os.path.join('ressource', 'TopRightCorner.png')),
        'top_middle': pygame.image.load(os.path.join('ressource', 'MiddleTop.png')),
        'bot_right_corner': pygame.image.load(os.path.join('ressource', 'BottomRigthCorner.png')),
        'bot_left_corner': pygame.image.load(os.path.join('ressource', 'BottomLeftCorner.png')),
        'bot_middle': pygame.image.load(os.path.join('ressource', 'MiddleBot.png')),
        'left_middle': pygame.image.load(os.path.join('ressource', 'MiddleLeft.png')),
        'right_middle': pygame.image.load(os.path.join('ressource', 'MiddleRight.png')),
        'maze_wall': pygame.image.load(os.path.join('ressource', 'wall.png'))}

    constant.GAME_DISPLAY.fill((0, 0, 0))
    for index_raw, _ in enumerate(constant.MAZE):
        for index_col, _ in enumerate(constant.MAZE[index_raw]):
            case_value = constant.MAZE[index_raw][index_col]
            screen_raw = index_col * 25
            screen_col = index_raw * 25
            if case_value == '1':
                sprite(structure['top_middle'], screen_raw, screen_col)

            elif case_value == '2':
                sprite(structure['top_left_corner'], screen_raw, screen_col)

            elif case_value == '3':
                sprite(structure['bot_left_corner'], screen_raw, screen_col)

            elif case_value == '4':
                sprite(structure['bot_right_corner'], screen_raw, screen_col)

            elif case_value == '6':
                sprite(structure['left_middle'], screen_raw, screen_col)

            elif case_value == '5':
                sprite(structure['top_right_corner'], screen_raw, screen_col)

            elif case_value == '7':
                sprite(structure['right_middle'], screen_raw, screen_col)

            elif case_value == 'X':
                sprite(structure['bot_middle'], screen_raw, screen_col)

            elif case_value == 'M':
                sprite(structure['maze_wall'], screen_raw, screen_col)

    Seringe.draw_objet(structure['seringe_img'])
    Needle.draw_objet(structure['needle_img'])
    Plastic.draw_objet(structure['plastic_tube_img'])
    Ether.draw_objet(structure['ether_img'])

    MacGyver.draw_hero(structure['mc_gyver_img'])
    sprite(structure['guard_img'], guard_pos_x * 25, guard_pos_y * 25)

    text("ITEM: {}".format(MacGyver.object_count), constant.YELLOW)
    # pygame.display.update()

def game():
    """Here is the game function, it regroups the labyrinth,
    the Hero class method and set the player's move"""
    game_on = True
    while game_on:
        pygame.init()
        labyrinth()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
            control = pygame.key.get_pressed()

            if control[pygame.K_LEFT] and constant.MAZE[MacGyver.pos_y][MacGyver.pos_x - 1] == '0':
                MacGyver.pos_x -= 1
            if control[pygame.K_RIGHT] and constant.MAZE[MacGyver.pos_y][MacGyver.pos_x + 1] == '0':
                MacGyver.pos_x += 1
            if control[pygame.K_UP] and constant.MAZE[MacGyver.pos_y - 1][MacGyver.pos_x] == '0':
                MacGyver.pos_y -= 1
            if control[pygame.K_DOWN] and constant.MAZE[MacGyver.pos_y + 1][MacGyver.pos_x] == '0':
                MacGyver.pos_y += 1

            MacGyver.take_object(Plastic)
            MacGyver.take_object(Ether)
            MacGyver.take_object(Needle)
            MacGyver.take_object(Seringe)

            if MacGyver.pos_x == guard_pos_x and MacGyver.pos_y == guard_pos_y \
            and MacGyver.object_count >= 3:
                game_on = False
                end_game("GAGNÉ", constant.GREEN)
                time.sleep(4)

            elif MacGyver.pos_x == guard_pos_x and MacGyver.pos_y == guard_pos_y \
            and MacGyver.object_count < 3:
                game_on = False
                end_game("PERDU", constant.RED)
                time.sleep(4)

    pygame.display.update()

game()

"""This is the module where i set all the classes for the main file.
it has the item, heros and labyrinth(level) classes
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
        constant.GAME_DISPLAY.blit(image, (self.pos_x * 25, self.pos_y * 25))


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
        constant.GAME_DISPLAY.blit(image, (self.pos_x * 25, self.pos_y * 25))

    def take_object(self, item):
        """ Hero can take an item and it will change his position on the screen"""
        if self.pos_x == item.pos_x and self.pos_y == item.pos_y \
                and item.taken is False:
            item.pos_x = 1000 * 25
            item.pos_y = 1000 * 25
            item.taken = True
            self.object_count += 1


class Labyrinth:
    """Set the structure of the labyrinth from the grid in the constant file,
    each character will match a structure '0' is the path the player can move """
    maze = []
    grid = open("labyrinth.txt", "r")
    for line in grid:
        a = line.replace("/n", "")
        raw = a.split()
        for case in raw:
            value = case.split(",")
        maze.append(value)
    grid.close()
    guard_pos_x = 16
    guard_pos_y = 10
    MacGyver = Heros()
    Needle = Item()
    Ether = Item()
    Plastic = Item()
    game_on = False
    Needle.random_position(maze)
    Ether.random_position(maze)
    Plastic.random_position(maze)
    structure = {
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

    @classmethod
    def sprite(cls, wall_image, pos_x, pos_y):
        """display the right sprite in the right position
        """
        constant.GAME_DISPLAY.blit(wall_image, (pos_x, pos_y))

    @classmethod
    def text(cls, msg, color):
        """display the Item section at the bottom of the screen"""
        screen_text = pygame.font.SysFont('Arial', 25).render(msg, True, color)
        constant.GAME_DISPLAY.blit(screen_text, (1 * 25, 17 * 25))

    @classmethod
    def end_game(cls, msg, color):
        """Will display the right message wether the player won or lose"""
        constant.GAME_DISPLAY.fill((0, 0, 0))
        screen_text = pygame.font.SysFont('Arial', 25).render(msg, True, color)
        constant.GAME_DISPLAY.blit(screen_text, (425 / 2, 425 / 2))
        pygame.display.update()

    @classmethod
    def menu(cls):
        """ Landing screen to launch the game it will explain
         the rules and commands of the game"""
        constant.GAME_DISPLAY.fill((255, 255, 255))
        screen_title = pygame.font.SysFont('Arial', 50).render('AIDEZ MCGYVER',
                                                               True, constant.BLACK)
        screen_paragraph1 = pygame.font.SysFont('Arial', 25).render("Pour gagné,",
                                                                    True, constant.BLACK)
        screen_paragraph2 = pygame.font.SysFont('Arial', 25).render(
            "il suffit de ramasser les trois objets", True, constant.BLACK)
        screen_paragraph3 = pygame.font.SysFont('Arial', 25).render(
            "et de vous preséter devant le garde.", True, constant.BLACK)
        screen_controle1 = pygame.font.SysFont('Arial', 25).render(
            "Utilisez les touches directionelles",
            True, constant.BLACK)
        screen_controle2 = pygame.font.SysFont('Arial', 25).render(
            "du clavier pour vous déplacer",
            True, constant.BLACK)
        quit_menu = pygame.font.SysFont('Arial', 30).render(
            "Appuyez sur 'space' pour jouer",
            True, constant.BLACK)
        constant.GAME_DISPLAY.blit(screen_title, (0, 0))
        constant.GAME_DISPLAY.blit(screen_paragraph1, (150, 90))
        constant.GAME_DISPLAY.blit(screen_paragraph2, (15, 120))
        constant.GAME_DISPLAY.blit(screen_paragraph3, (15, 150))
        constant.GAME_DISPLAY.blit(screen_controle1, (15, 180))
        constant.GAME_DISPLAY.blit(screen_controle2, (15, 210))
        constant.GAME_DISPLAY.blit(quit_menu, (10, 350))
        pygame.display.update()

    def __init__(self):
        constant.GAME_DISPLAY.fill((0, 0, 0))
        for index_raw, _ in enumerate(self.maze):
            for index_col, _ in enumerate(self.maze[index_raw]):
                case_value = self.maze[index_raw][index_col]
                screen_raw = index_col * 25
                screen_col = index_raw * 25
                if case_value == '1':
                    self.sprite(self.structure['top_middle'], screen_raw, screen_col)

                elif case_value == '2':
                    self.sprite(self.structure['top_left_corner'], screen_raw, screen_col)

                elif case_value == '3':
                    self.sprite(self.structure['bot_left_corner'], screen_raw, screen_col)

                elif case_value == '4':
                    self.sprite(self.structure['bot_right_corner'], screen_raw, screen_col)

                elif case_value == '6':
                    self.sprite(self.structure['left_middle'], screen_raw, screen_col)

                elif case_value == '5':
                    self.sprite(self.structure['top_right_corner'], screen_raw, screen_col)

                elif case_value == '7':
                    self.sprite(self.structure['right_middle'], screen_raw, screen_col)

                elif case_value == 'X':
                    self.sprite(self.structure['bot_middle'], screen_raw, screen_col)

                elif case_value == 'M':
                    self.sprite(self.structure['maze_wall'], screen_raw, screen_col)

        self.Needle.draw_objet(self.structure['needle_img'])
        self.Plastic.draw_objet(self.structure['plastic_tube_img'])
        self.Ether.draw_objet(self.structure['ether_img'])

        self.MacGyver.draw_hero(self.structure['mc_gyver_img'])
        self.sprite(self.structure['guard_img'], self.guard_pos_x * 25, self.guard_pos_y * 25)

        self.text("ITEM: {}".format(self.MacGyver.object_count), constant.YELLOW)

    def win_or_lose(self):
        """This function check if the player won the game or lose it and display the right text"""
        if self.MacGyver.pos_x == self.guard_pos_x and self.MacGyver.pos_y == self.guard_pos_y \
                and self.MacGyver.object_count >= 3:
            self.end_game("GAGNÉ", constant.GREEN)
            time.sleep(4)
            Labyrinth.game_on = False
            self.reset_labyrinth()

        elif self.MacGyver.pos_x == self.guard_pos_x and self.MacGyver.pos_y == self.guard_pos_y \
                and self.MacGyver.object_count < 3:
            self.end_game("PERDU", constant.RED)
            time.sleep(4)
            Labyrinth.game_on = False
            self.reset_labyrinth()


    def reset_labyrinth(self):
        """reset the game at his origin"""
        self.Needle.random_position(self.maze)
        self.Ether.random_position(self.maze)
        self.Plastic.random_position(self.maze)
        self.MacGyver.pos_x = 0
        self.MacGyver.pos_y = 2
        self.MacGyver.object_count = 0
        self.Needle.taken = False
        self.Ether.taken = False
        self.Plastic.taken = False

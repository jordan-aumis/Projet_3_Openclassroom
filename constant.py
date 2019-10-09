"""This file regroups constants using for the game like colors or window display"""
import os
import pygame

GAME_DISPLAY = pygame.display.set_mode((425, 475))
YELLOW = pygame.Color(255, 255, 0)
GREEN = pygame.Color(75, 181, 67)
RED = pygame.Color(255, 0, 0)
BLACK = pygame.Color(0, 0, 0)
STRUCTURE = {
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
        
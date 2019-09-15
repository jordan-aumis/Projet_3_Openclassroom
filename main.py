import game
import pygame
import time
import constant


def main():
    """Here is the game function, it regroups the labyrinth,
    the Hero class method and set the player's move"""
    pygame.init()
    play = True
    game_on = False

    while play:
        if game_on is False:
            menu = game.Menu()
            press = pygame.key.get_pressed()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or press[pygame.K_ESCAPE]:
                    pygame.quit()
                    play = False
                if press[pygame.K_SPACE]:
                    game_on = True

        if game_on:
            level_1 = game.Labyrinth()
            pygame.display.update()
            control = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    play = False

                if control[pygame.K_LEFT] and constant.MAZE[level_1.MacGyver.pos_y][level_1.MacGyver.pos_x - 1] == '0':
                    level_1.MacGyver.pos_x -= 1
                if control[pygame.K_RIGHT] and constant.MAZE[level_1.MacGyver.pos_y][level_1.MacGyver.pos_x + 1] == '0':
                    level_1.MacGyver.pos_x += 1
                if control[pygame.K_UP] and constant.MAZE[level_1.MacGyver.pos_y - 1][level_1.MacGyver.pos_x] == '0':
                    level_1.MacGyver.pos_y -= 1
                if control[pygame.K_DOWN] and constant.MAZE[level_1.MacGyver.pos_y + 1][level_1.MacGyver.pos_x] == '0':
                    level_1.MacGyver.pos_y += 1

                level_1.MacGyver.take_object(level_1.Plastic)
                level_1.MacGyver.take_object(level_1.Ether)
                level_1.MacGyver.take_object(level_1.Needle)
                level_1.MacGyver.take_object(level_1.Seringe)

                if level_1.MacGyver.pos_x == level_1.guard_pos_x and level_1.MacGyver.pos_y == level_1.guard_pos_y \
                        and level_1.MacGyver.object_count >= 3:
                    level_1.end_game("GAGNÉ", constant.GREEN)
                    time.sleep(4)
                    game_on = False
                    level_1.reset_labyrinth()

                elif level_1.MacGyver.pos_x == level_1.guard_pos_x and level_1.MacGyver.pos_y == level_1.guard_pos_y \
                        and level_1.MacGyver.object_count < 3:
                    level_1.end_game("PERDU", constant.RED)
                    time.sleep(4)
                    game_on = False
                    level_1.reset_labyrinth()


main()

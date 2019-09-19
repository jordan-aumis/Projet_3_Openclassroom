"""This is the main file from which the game is launched"""
import pygame
import game


def main():
    """Here is the game function, it regroups the labyrinth,
    the Hero class method and set the player's move with the main loop"""
    pygame.init()
    play = True

    while play:
        if game.Labyrinth.game_on is False:
            press = pygame.key.get_pressed()
            game.Labyrinth.menu()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or press[pygame.K_ESCAPE]:
                    pygame.quit()
                    play = False
                if press[pygame.K_SPACE]:
                    game.Labyrinth.game_on = True

        if game.Labyrinth.game_on is True:
            level_1 = game.Labyrinth()
            pygame.display.update()
            control = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    play = False

                if control[pygame.K_LEFT] and \
                        game.Labyrinth.maze[level_1.MacGyver.pos_y][level_1.MacGyver.pos_x - 1] \
                            == '0':
                    level_1.MacGyver.pos_x -= 1
                if control[pygame.K_RIGHT] and \
                        game.Labyrinth.maze[level_1.MacGyver.pos_y][level_1.MacGyver.pos_x + 1] \
                            == '0':
                    level_1.MacGyver.pos_x += 1
                if control[pygame.K_UP] and \
                        game.Labyrinth.maze[level_1.MacGyver.pos_y - 1][level_1.MacGyver.pos_x] \
                            == '0':
                    level_1.MacGyver.pos_y -= 1
                if control[pygame.K_DOWN] and \
                        game.Labyrinth.maze[level_1.MacGyver.pos_y + 1][level_1.MacGyver.pos_x] \
                            == '0':
                    level_1.MacGyver.pos_y += 1

                level_1.MacGyver.take_object(level_1.Plastic)
                level_1.MacGyver.take_object(level_1.Ether)
                level_1.MacGyver.take_object(level_1.Needle)
                level_1.win_or_lose()


main()

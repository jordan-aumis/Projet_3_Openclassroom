import pygame 

"""Here is the Labyrinth :
first i created a 2d list first list is the raw and second the col
 """ 
grid = [
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
    [8, 0, 'M', 0, 0, 0, 'M',  0, 0, 0, 'M', 0, 0, 0, 0, 0, 7],
    [6, 0, 0, 0, 'M', 0, 'M', 0, 'M', 0, 'M', 0, 'M', 0, 'M', 0, 7],
    [6, 'M', 'M', 'M', 0, 0, 'M', 0, 'M', 0, 0, 0, 'M', 0, 'M', 0, 7],
    [6, 0, 0, 'M', 0, 'M', 'M', 0, 'M', 'M', 'M', 0, 'M', 'M', 0, 0, 7],
    [6, 'M', 0, 0, 0, 0, 'M', 0, 0, 0, 0, 'M', 'M', 0, 0, 'M', 7],
    [6, 0, 0, 'M', 'M', 0, 0, 0, 'M', 'M', 0, 0, 'M', 'M', 0, 0, 7],
    [6, 0, 'M', 0, 'M', 0, 'M', 0, 'M', 0, 'M', 0, 0, 'M', 'M', 0, 9],
    [6, 0, 0, 0, 'M', 0, 'M', 0, 0, 0, 'M', 'M', 0, 0, 0, 'M', 7],
    [3, 'X', 'X','X','X','X','X','X','X','X','X','X','X','X','X','X', 4]]

TopLeftCorner = pygame.image.load('TopLeftCorner.png')
TopRightCorner = pygame.image.load('TopRightCorner.png')
TopMiddle = pygame.image.load('MiddleTop.png')
BottomRightCorner = pygame.image.load('BottomRigthCorner.png')
BottomLeftCorner = pygame.image.load('BottomLeftCorner.png')
BottomMiddle = pygame.image.load('MiddleBot.png')
LeftMiddle = pygame.image.load('MiddleLeft.png')
RightMiddle = pygame.image.load('MiddleRight.png')
maze_wall = pygame.image.load('wall.png')

pygame.init()

gameDisplay = pygame.display.set_mode((425,250))

pygame.display.set_caption(("MacGyver ce héros"))

i = 25
def wall(wallImage, x, y):
    gameDisplay.blit(wallImage, (x,y))

gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

    gameDisplay.fill((0,0,0))
    for raw in range(len(grid)):
        for col in range(len(grid[raw])):
            case_value = grid[raw][col]

            screen_raw = 0 + (col * 25)
            screen_col = 225 - (raw * 25)
            if case_value == 1:
                wall(BottomMiddle, screen_raw, screen_col)
            elif case_value == 2:
                wall(BottomLeftCorner, screen_raw, screen_col)
            elif case_value == 3:
                wall(TopLeftCorner, screen_raw, screen_col)
            elif case_value == 4:
                wall(TopRightCorner, screen_raw, screen_col)
            elif case_value == 5:
                wall(BottomRightCorner, screen_raw, screen_col)
            elif case_value == 6:
                wall(LeftMiddle, screen_raw, screen_col)
            elif case_value == 7:
                wall(RightMiddle, screen_raw, screen_col)
            # elif case_value == 8:
            #     wall(RightMiddle, screen_raw, screen_col)
            elif case_value == 'X':
                wall(TopMiddle, screen_raw, screen_col)
            elif case_value == 'M':
                wall(maze_wall, screen_raw, screen_col)

                
    
    pygame.display.update()
    
  
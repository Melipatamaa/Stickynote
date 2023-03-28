from scripts.grid import *
import pygame

font = pygame.font.SysFont(None, 24)
text_speed = font.render('Speed : ', True, ORANGE)


def draw_grid_on_canvas(canvas,grid:Grid):
    """
    It draws a grid on the canvas on the center of the screen.
    
    :param canvas: the surface to draw on
    :param grid: the grid object
    :type grid: Grid
    """
    #pygame.draw.rect(canvas,WHITE,(BORDERS_ROWS,BORDERS_COLS,CANVAS_WIDTH,CANVAS_HEIGHT))
    for i, row in enumerate(grid.grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(canvas,pixel,(j*PX_SIZE,i*PX_SIZE,PX_SIZE,PX_SIZE)) #original and final coordinates
    if GRID:
        #+1 so the grid won't be cropped by the window 
        for i in range(ROWS + 1):
            pygame.draw.line(canvas,LGREY,(0,i*PX_SIZE),(WIDTH,i*PX_SIZE))
        for j in range(COLS + 1):
            pygame.draw.line(canvas,LGREY,(j*PX_SIZE,0),(j*PX_SIZE,HEIGHT-TOOLBAR))
    if CANVAS_GRID:
        for i in range(ROWS):
            #+2 pour bien fermer la grille
            pygame.draw.line(canvas,LGREY,(BORDERS_ROWS,BORDERS_COLS+i*PX_SIZE),(WIDTH - BORDERS_ROWS+2,BORDERS_COLS+i*PX_SIZE))
        #pour faire une belle grille propre (ne dépasse pas, 85 et 100 valeurs random pour ROWS = 200)
        for k in range(85,100):
            pygame.draw.line(canvas,WHITE,(BORDERS_ROWS,BORDERS_COLS+k*PX_SIZE),(WIDTH - BORDERS_ROWS+2,BORDERS_COLS+k*PX_SIZE))
        for j in range(COLS):
            pygame.draw.line(canvas,LGREY,(BORDERS_ROWS+j*PX_SIZE,BORDERS_COLS),(BORDERS_ROWS+j*PX_SIZE,HEIGHT-BORDERS_COLS+3))
        #pour faire une belle grille propre
        for l in range(148,180):
            pygame.draw.line(canvas,WHITE,(BORDERS_ROWS+l*PX_SIZE,BORDERS_COLS),(BORDERS_ROWS+l*PX_SIZE,HEIGHT-BORDERS_COLS+3))


def get_coord_position(pos):
    """
    It takes a position (x, y) and returns the row and column of the corresponding pixel in the image.
    
    :param pos: the position of the mouse click
    :return: The row and column of the pixel that was clicked.
    """
    x, y = pos
    row = y // PX_SIZE
    col = x // PX_SIZE
    #modification des valeurs rentrées en focntion des paramètres : pour + tard
    if (col <= 26 or col >= 174 or row <= 16 or row >= 101):
        raise IndexError
    return row, col

def draw_on_grid(grid:Grid,drawing_col,row,col,size):
    """
    It draws a shape depending on the size of the brush on the canvas.
    
    :param grid: the grid object
    :type grid: Grid
    :param drawing_col: The color of the drawing
    :param row: the row of the grid you want to draw on
    :param col: the column of the grid you want to draw on
    :param size: the size of the square you want to draw
    """
    if (size > 1 and size <5):
        grid.grid[row+1][col] = drawing_col
        grid.grid[row-1][col] = drawing_col
        grid.grid[row][col+1] = drawing_col
        grid.grid[row][col-1] = drawing_col
        if size > 2:
            grid.grid[row+1][col+1] = drawing_col
            grid.grid[row-1][col-1] = drawing_col
            grid.grid[row-1][col+1] = drawing_col
            grid.grid[row+1][col-1] = drawing_col
            grid.grid[row+2][col-1] = drawing_col
            grid.grid[row+2][col] = drawing_col
            grid.grid[row+2][col+1] = drawing_col
            grid.grid[row-2][col-1] = drawing_col
            grid.grid[row-2][col] = drawing_col
            grid.grid[row-2][col+1] = drawing_col
            grid.grid[row-1][col+2] = drawing_col
            grid.grid[row][col+2] = drawing_col
            grid.grid[row+1][col+2] = drawing_col
            grid.grid[row-1][col-2] = drawing_col
            grid.grid[row][col-2] = drawing_col
            grid.grid[row+1][col-2] = drawing_col
            if size > 3:
                grid.grid[row+2][col+2] = drawing_col
                grid.grid[row-2][col-2] = drawing_col
                grid.grid[row-2][col+2] = drawing_col
                grid.grid[row+2][col-2] = drawing_col
                grid.grid[row+3][col-1] = drawing_col
                grid.grid[row+3][col] = drawing_col
                grid.grid[row+3][col+1] = drawing_col
                grid.grid[row-3][col-1] = drawing_col
                grid.grid[row-3][col] = drawing_col
                grid.grid[row-3][col+1] = drawing_col
                grid.grid[row-1][col+3] = drawing_col
                grid.grid[row][col+3] = drawing_col
                grid.grid[row+1][col+3] = drawing_col
                grid.grid[row-1][col-3] = drawing_col
                grid.grid[row][col-3] = drawing_col
                grid.grid[row+1][col-3] = drawing_col
    if (size > 4 and size < 6):
        grid.grid[row+3][col] = drawing_col
        grid.grid[row+2][col] = drawing_col
        grid.grid[row+1][col] = drawing_col
        grid.grid[row-1][col] = drawing_col
        grid.grid[row-2][col] = drawing_col
        grid.grid[row-3][col] = drawing_col
    if size > 5:
        grid.grid[row][col+3] = drawing_col
        grid.grid[row][col+2] = drawing_col
        grid.grid[row][col+1] = drawing_col
        grid.grid[row][col-1] = drawing_col
        grid.grid[row][col-2] = drawing_col
        grid.grid[row][col-3] = drawing_col

def display_interface(WINDOW,sticky):
    a = 20

    # White background of the interface
    pygame.draw.rect(WINDOW,WHITE,(0,0,WIDTH,BORDERS_COLS))
    pygame.draw.rect(WINDOW,WHITE,(0,0,BORDERS_ROWS,HEIGHT))
    pygame.draw.rect(WINDOW,WHITE,(0,HEIGHT-BORDERS_COLS,WIDTH,BORDERS_COLS))
    pygame.draw.rect(WINDOW,WHITE,(WIDTH-BORDERS_ROWS,0,BORDERS_ROWS,HEIGHT))

    # Orange border
    pygame.draw.rect(WINDOW,ORANGE,(0,0,WIDTH,HEIGHT), 20)

    # Some *fancy* details to top left corner...
    pygame.draw.rect(WINDOW,ORANGE,(a,a,a,a))
    pygame.draw.rect(WINDOW,ORANGE,(a+a,a,a,a))
    pygame.draw.rect(WINDOW,ORANGE,(a,a+a,a,a))

    # ...to the bottom left corner...
    pygame.draw.rect(WINDOW,ORANGE,(a,HEIGHT-2*a,a,a))
    pygame.draw.rect(WINDOW,ORANGE,(a+a,HEIGHT-2*a,a,a))
    pygame.draw.rect(WINDOW,ORANGE,(a,HEIGHT-3*a,a,a))

    # ...to the top right corner...
    pygame.draw.rect(WINDOW,ORANGE,(WIDTH-2*a,a,a,a))
    pygame.draw.rect(WINDOW,ORANGE,(WIDTH-2*a,a+a,a,a))
    pygame.draw.rect(WINDOW,ORANGE,(WIDTH-3*a,a,a,a))

    # ...and to the bottom right corner !
    pygame.draw.rect(WINDOW,ORANGE,(WIDTH-2*a,HEIGHT-2*a,a,a))
    pygame.draw.rect(WINDOW,ORANGE,(WIDTH-2*a,HEIGHT-3*a,a,a))
    pygame.draw.rect(WINDOW,ORANGE,(WIDTH-3*a,HEIGHT-2*a,a,a))

    # Drawing a border around the grid
    pygame.draw.rect(WINDOW,ORANGE,(BORDERS_ROWS - 5,BORDERS_COLS - 5,CANVAS_WIDTH + 5,CANVAS_HEIGHT + 5), 10)

    # Displaying the logo of Stickynote Studio
    WINDOW.blit(sticky,(460,25))

    WINDOW.blit(text_speed, (BORDERS_ROWS - 8, HEIGHT - 72))

def get_frame_number(WINDOW,current_frame_index):
    pygame.draw.rect(WINDOW,ORANGE,(1050,600,50,50))
    cfi = font.render(str(current_frame_index),True, WHITE)
    WINDOW.blit(cfi, (1060,610))
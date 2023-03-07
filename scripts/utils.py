from scripts.grid import *
import pygame

def draw_grid_on_canvas(canvas,grid:Grid):
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
    x, y = pos
    row = y // PX_SIZE
    col = x // PX_SIZE
    #modification des valeurs rentrées en focntion des paramètres : pour + tard
    if (col <= 26 or col >= 174 or row <= 16 or row >= 101):
        raise IndexError
    return row, col

def draw_on_grid(grid:Grid,drawing_col,row,col,size):
    if size > 1:
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

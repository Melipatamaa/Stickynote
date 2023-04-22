from scripts.grid import *
import os
import pygame
import cv2
import numpy as np
import glob
import time

font = pygame.font.SysFont(None, 24)
text_speed = font.render('Speed : ', True, ORANGE)


def draw_grid_on_canvas(canvas,grid:Grid,grid_pattern):
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
    if grid_pattern:
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
    """
    This function displays an interface with various graphical elements such as borders, rectangles, and
    a logo.
    
    :param WINDOW: The Pygame window surface on which the interface will be displayed
    :param sticky: The "sticky" parameter is an image representing the logo of
    Stickynote Studio, which is displayed on the interface using the `WINDOW.blit()` method
    """
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

def get_frame_number(WINDOW,current_frame_index,animation_list):
    """
    This function displays the current frame number and total number of frames in an animation on a
    Pygame window.
    
    :param WINDOW: The Pygame window surface on which the frame number will be displayed
    :param current_frame_index: The index of the current frame in the animation_list
    :param animation_list: A list of frames in an animation. Each frame is a separate image that is
    displayed in sequence to create the illusion of motion
    """
    pygame.draw.rect(WINDOW,ORANGE,(1053,610,62,50))
    font = pygame.font.SysFont("calibri", 18)
    cfi = font.render(str(current_frame_index+1) + "/" + str(len(animation_list)),True, WHITE)
    WINDOW.blit(cfi, (1060,620))

def save_frame(screen,current_frame_index,unique_id):
    """
    It takes a screenshot of the canvas and saves it as a jpg file.
    
    :param screen: the screen that you want to save
    """
    folder = f"{os.getcwd()}\\frames_{unique_id}"
    rect = pygame.Rect(BORDERS_ROWS, BORDERS_COLS, CANVAS_WIDTH-5, CANVAS_HEIGHT-5)
    sub = screen.subsurface(rect)
    screenshot = pygame.Surface((CANVAS_WIDTH-5, CANVAS_HEIGHT-5))
    screenshot.blit(sub, (0,0))
    if not os.path.exists(folder):
        os.makedirs(folder)
    pygame.image.save(screenshot, f"{folder}\\frame{current_frame_index+1}.jpg")

def delete_frame(current_frame_index,unique_id):
    """
    This function deletes a specific frame from a directory based on its index and a unique identifier.
    
    :param current_frame_index: The index of the frame that needs to be deleted
    :param unique_id: The unique_id parameter is a string that represents a unique identifier for a set
    of frames. It is used to create a folder where the frames are stored and retrieved from
    """
    folder = f"{os.getcwd()}\\frames_{unique_id}"
    os.remove(f"{folder}\\frame{current_frame_index+1}.jpg")

def clean_for_save(unique_id):
    folder = f"{os.getcwd()}\\frames_{unique_id}"
    for frame in os.listdir(folder):
        os.remove(os.path.join(folder,frame))

def change_type_rate(frame_speed):
    new_frame_speed = 0
    print(frame_speed)
    if (frame_speed == 1000):
        new_frame_speed = 1
    elif (frame_speed == 800):
        new_frame_speed = 1.5
    elif (frame_speed == 600):
        new_frame_speed = 2
    elif (frame_speed == 400):
        new_frame_speed = 2.5
    elif (frame_speed == 200):
        new_frame_speed = 3
    elif (frame_speed == 100):
        new_frame_speed = 3.5
    elif (frame_speed == 50):
        new_frame_speed = 4
    elif (frame_speed == 25):
        new_frame_speed = 4.5
    return new_frame_speed

def save_video(unique_id,frame_speed):
    frames = []
    folder_files = f"{os.getcwd()}\\frames_{unique_id}\\*.jpg"
    for frame in glob.glob(folder_files):
        img = cv2.imread(frame)
        height, width, layer = img.shape
        size = (width,height)
        frames.append(img)
    new_frame_speed = change_type_rate(frame_speed)
    out = cv2.VideoWriter(f"{os.getcwd()}\\frames_{unique_id}\\my_animation.avi",cv2.VideoWriter_fourcc(*'XVID'), new_frame_speed, size)
    for i in range(len(frames)):
        out.write(frames[i])
    out.release()
    return
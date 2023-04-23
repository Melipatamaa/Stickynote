import pygame
pygame.init()
pygame.font.init()

# Defining the colors for the brushes.
WHITE = (255,255,255)
LGREY = (200,200,200)
GREY = (125, 125, 125)
BLACK = (0,0,0)
BLUE = (67,94,255)
GREEN = (47,198,54)
YELLOW = (246,221,52)
ORANGE = (255,117,15)
RED = (241,50,50)
PINK = (244,72,153)
PURPLE = (179, 46, 228)

# Setting the frame rate of Stickynote.
FPS = 60

# Defining the dimensions of the window.
WIDTH = 1200
HEIGHT = 700

# Defining the size of the pixels.
ROWS = 200
COLS = 200
PX_SIZE = WIDTH // ROWS

# Defining the dimensions of the canvas.
CANVAS_WIDTH = 883
CANVAS_HEIGHT = 505

# Limits of the drawing grid
GRID_ROW_MIN = 17
GRID_COL_MIN = 27
GRID_ROW_MAX = 110
GRID_COL_MAX = 175

# Defining the width of the toolbar containing the different buttons.
TOOLBAR = WIDTH - 1140

# Setting the background color of the canvas to white.
BACKGROUND_COLOR = WHITE

# Defining the dimensions of the borders of the screen.
BORDERS_ROWS = 160
BORDERS_COLS = 100

def get_font(size):
    """
    It returns a font object with the font "calibri" and the size "size"
    
    :param size: The size of the font
    :return: A font object.
    """
    return pygame.font.SysFont("calibri",size)
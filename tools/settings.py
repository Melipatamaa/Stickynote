import pygame
pygame.init()
pygame.font.init()

#colors for brushes
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

#to look for
FPS = 300

#dimensions of the window
WIDTH = 1200
HEIGHT = 700

#size of the pixels
ROWS = 100
COLS = 100
PX_SIZE = WIDTH // ROWS
#print(PX_SIZE)

#dimensions of the canvas
CANVAS_WIDTH = 700
CANVAS_HEIGHT = 500

#toolbar containing colors, eraser..
TOOLBAR = WIDTH - 1140

#color of the background
BACKGROUND_COLOR = WHITE

#help to represent pixels
GRID = False

CANVAS_GRID = True

BORDERS_ROWS = 120
BORDERS_COLS = 60

#create a font
def get_font(size):
    return pygame.font.SysFont("calibri",size)
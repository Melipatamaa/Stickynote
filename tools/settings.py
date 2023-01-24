import pygame
pygame.init()
pygame.font.init()

#colors for brushes
WHITE = (255,255,255)
LGREY = (200,200,200)
BLACK = (0,0,0)
ORANGE = (255,117,15)

#to look for
FPS = 60

#dimensions of the window
WIDTH = 500
HEIGHT = 600

#size of the pixels
PX_W = 20
PX_H = 20
PX_SIZE = WIDTH // PX_W

#toolbar containing colors, eraser..
TOOLBAR_H = HEIGHT - WIDTH

#color of the background
BACKGROUND_COLOR = WHITE

#help to represent pixels in the canvas
GRID = True

#create a font
def get_font(size):
    return pygame.font.SysFont("calibri",size)
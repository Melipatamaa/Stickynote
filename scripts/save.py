from .settings import *
from .button import *

class Save(Button) :
    def __init__(self,x,y,width,height,screen,color,text=None,text_color=BLACK,icon = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.icon = icon
        self.screen = screen

    def save(self,screen):
        rect = pygame.Rect(BORDERS_ROWS, BORDERS_COLS, CANVAS_WIDTH, CANVAS_HEIGHT)
        sub = screen.subsurface(rect)
        screenshot = pygame.Surface((CANVAS_WIDTH, CANVAS_HEIGHT))
        screenshot.blit(sub, (0,0))
        pygame.image.save(screenshot, "screenshot1.jpg")
            
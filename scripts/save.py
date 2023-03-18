from .settings import *
from .button import *

class Save(Button) :
    def __init__(self,x,y,width,height,screen,color,border_color=LGREY,text=None,text_color=BLACK,icon = None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.screen = screen

    def save(self,screen):
        rect = pygame.Rect(BORDERS_ROWS, BORDERS_COLS, CANVAS_WIDTH, CANVAS_HEIGHT)
        sub = screen.subsurface(rect)
        screenshot = pygame.Surface((CANVAS_WIDTH, CANVAS_HEIGHT))
        screenshot.blit(sub, (0,0))
        pygame.image.save(screenshot, "screenshot1.jpg")
            
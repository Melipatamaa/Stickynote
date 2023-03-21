from .settings import *
from .button import *

# The Save class is a subclass of the Button class. It has the same attributes as the Button class,
# but it also has a screen attribute so as to get the drawing that has to be saved.
class Save(Button) :
    def __init__(self,x,y,width,height,screen,color,border_color=LGREY,text=None,text_color=BLACK,icon = None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.screen = screen

    def save(self,screen):
        """
        It takes a screenshot of the canvas and saves it as a jpg file.
        
        :param screen: the screen that you want to save
        """
        rect = pygame.Rect(BORDERS_ROWS, BORDERS_COLS, CANVAS_WIDTH-5, CANVAS_HEIGHT-5)
        sub = screen.subsurface(rect)
        screenshot = pygame.Surface((CANVAS_WIDTH-5, CANVAS_HEIGHT-5))
        screenshot.blit(sub, (0,0))
        pygame.image.save(screenshot, "screenshot1.jpg")
            
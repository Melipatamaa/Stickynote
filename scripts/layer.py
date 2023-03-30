from .settings import *
from .button import *
from .save import *

# The Layer class is a subclass of the Button class. It creates a reference image that the user can display on 
# his current drawing to get a better and smoother animation.

class Layer(Button) :
    def __init__(self,x,y,width,height,screen,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.screen = screen

    def stick_layer(self,screen,visible,current_frame_index):
        if current_frame_index > 0:
            layer = pygame.image.load(f"screenshot{current_frame_index}.jpg")
            if visible:
                pygame.Surface.set_alpha(layer,50)
                screen.blit(layer,(BORDERS_ROWS,BORDERS_COLS))
            #else:
            #    pygame.Surface.set_alpha(layer,0)
            #    screen.blit(layer,(BORDERS_ROWS,BORDERS_COLS))
            #màj de l'écran
            #pygame.display.update()
            
        
        
from .settings import *
from .button import *

class Layer(Button) :
    def __init__(self,x,y,width,height,screen,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)

    def stick_layer(self,screen,visible):
        layer = pygame.image.load('screenshot1.jpg')
        if visible:
            pygame.Surface.set_alpha(layer,100)
            screen.blit(layer,(BORDERS_ROWS,BORDERS_COLS))
        else:
            pygame.Surface.set_alpha(layer,0)
            screen.blit(layer,(BORDERS_ROWS,BORDERS_COLS))
        #màj de l'écran
        pygame.display.update()
            
        
        
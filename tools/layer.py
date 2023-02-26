from .settings import *
from .button import *

class Layer(Button) :
    def __init__(self,x,y,width,height,screen,color,text=None,text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.color = color
        self.text = text
        self.text_color = text_color

    def stick_layer(self,screen,visible):
        layer = pygame.image.load('screenshot1.jpg')
        if visible:
            layer.set_alpha(50)
            screen.blit(layer,(BORDERS_ROWS,BORDERS_COLS))
        else:
            layer.set_alpha(0)
            screen.blit(layer,(BORDERS_ROWS,BORDERS_COLS))
            
        
        
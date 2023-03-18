from .settings import *
from .button import *

class Cancel(Button) :
    def __init__(self,x,y,width,height,screen,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.screen = screen
    
    def cancel_drawing(self,prev,screen):
        screen = prev

    
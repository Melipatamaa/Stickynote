from .settings import *
from .button import *

class Cancel(Button) :
    def __init__(self,x,y,width,height,screen,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.color = color
        self.border_color = border_color
        self.text = text
        self.text_color = text_color
        self.icon = icon
    
    def cancel_drawing(self,prev,screen):
        screen = prev

    
from .settings import *
from .button import *

class Cancel(Button) :
    def __init__(self,x,y,width,height,screen,color,text=None,text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.color = color  
        self.text = text
        self.text_color = text_color
    
    def cancel_drawing(self,prev,screen):
        screen = prev

    
from .settings import *
from .button import *

class ChooseFrame(Button) :
    def __init__(self,x,y,width,height,color,text=None,text_color=BLACK,icon=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.icon = icon
        self.choose = False
from .settings import *
from .button import *

class Brush(Button) :
    def __init__(self,x,y,width,height,size,color,text=None,text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.size = size
        self.color = color
        self.text = text
        self.text_color = text_color
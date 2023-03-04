from .settings import *
from .button import *

class Pipette(Button) :
    def __init__(self,x,y,width,height,row,col,color,text=None,text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.row = row
        self.col = col
        self.color = color  
        self.text = text
        self.text_color = text_color
        self.activated = False
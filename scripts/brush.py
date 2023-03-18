from .settings import *
from .button import *

class Brush(Button) :
    def __init__(self,x,y,width,height,size,row,col,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.size = size
        self.row = row
        self.col = col

 

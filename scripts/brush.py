from .settings import *
from .button import *

# Brush is a subclass of Button. It has the same attributes as Button, plus size, row, and col.
# size is giving the size of the pencil/brush, used on draw_on_grid(). row and col are needed 
# to draw around these coordinates.

class Brush(Button) :
    def __init__(self,x,y,width,height,size,row,col,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.size = size
        self.row = row
        self.col = col

 

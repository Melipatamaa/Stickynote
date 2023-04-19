from ..settings import *
from .button import *

# The class Pipette is a subclass of the class Button. It gets the color of the pixel with (row,col) coordinates
# that is clicked by the user.

class Pipette(Button) :
    def __init__(self,x,y,width,height,row,col,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.row = row
        self.col = col
        self.activated = False
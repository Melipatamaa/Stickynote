from ..settings import *
from .button import *

# The GridPattern class is a subclass of the Button class with additional parameters for creating a
# grid pattern. It allows the user to choose if they want to display a grid on their canvas for reference or not.

class GridPattern(Button) :
    def __init__(self,x,y,width,height,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
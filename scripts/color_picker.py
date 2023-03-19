from .settings import *
from .button import *

# The ColorPicker class inherits from the Button class, and adds a method to change the color of the
# button with Pygame_GUI in main.py.
class ColorPicker(Button) :
    def __init__(self,x,y,width,height,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
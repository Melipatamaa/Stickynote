from .settings import *
from .button import *

# The Color class is a subclass of the Button class. It manages buttons of colors.
class Color(Button) :
    def __init__(self,x,y,width,height,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
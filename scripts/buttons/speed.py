from ..settings import *
from .button import *

# The Speed class is a subclass of the Button class that initializes with a frame speed attribute. 8 speeds are available 
# and the user choose it on the screen. Thus, it will modifity the frame speed on the animation preview.

class Speed(Button) :
    def __init__(self,x,y,width,height,frame_speed,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.frame_speed = frame_speed
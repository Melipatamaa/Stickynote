from .settings import *
from .button import *

class Speed(Button) :
    def __init__(self,x,y,width,height,frame_speed,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.frame_speed = frame_speed
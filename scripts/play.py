from .settings import *
from .button import *

class Play(Button) :
    def __init__(self,x,y,width,height,animation_list,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.animation_list = animation_list

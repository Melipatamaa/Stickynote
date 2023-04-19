from ..settings import *
from .button import *

# The Play class is a subclass of the Button class that adds an animation list attribute. By clicking on Play, the user can 
# have a preview of its final animation.

class Play(Button) :
    def __init__(self,x,y,width,height,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)

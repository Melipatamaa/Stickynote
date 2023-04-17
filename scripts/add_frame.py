from .settings import *
from .button import *

# The AddFrame class is a subclass of the Button class with an additional attribute "add" initialized
# to False. By clicking on this button, the user adds a new frame to their animation.

class AddFrame(Button) :
    def __init__(self,x,y,width,height,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.add = False
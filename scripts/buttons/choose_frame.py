from ..settings import *
from .button import *

# The ChooseFrame class is a subclass of the Button class with an added attribute "choose" initialized
# to False. 2 types of choosing frames are possible : go back to the previous frame or move forward to the next one.

class ChooseFrame(Button) :
    def __init__(self,x,y,width,height,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.choose = False
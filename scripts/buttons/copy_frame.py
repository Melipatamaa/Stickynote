from ..settings import *
from .add_frame import *

# The CopyFrame class inherits from the AddFrame class and adds a boolean attribute "copy". Instead of creating a new
# blank frame, the user just copies their current frame.

class CopyFrame(AddFrame) :
    def __init__(self,x,y,width,height,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.copy = False
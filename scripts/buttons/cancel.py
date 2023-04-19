from ..settings import *
from .button import *

# The Cancel class is a subclass of the Button class with additional parameters for screen and icon. If the user wants
# to cancel a last drawing, they have to click on this button and it will reload the previous versions of the caanvas.

class Cancel(Button) :
    def __init__(self,x,y,width,height,screen,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.screen = screen
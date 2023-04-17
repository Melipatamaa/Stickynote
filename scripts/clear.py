from .settings import *
from .button import *

# The Clear class inherits from the Button class. When this button is clicked, the grid is entierely cleared.

class Clear(Button) :
    def __init__(self,x,y,width,height,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
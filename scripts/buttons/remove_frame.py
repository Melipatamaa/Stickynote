from ..settings import *
from .button import *

# The RemoveFrame class is a subclass of Button that initializes with a delete attribute set to False, so as the user can 
# delete the whole frame if they are not satisfied with it. This class is linked to the function delete_frame in utils.

class RemoveFrame(Button) :
    def __init__(self,x,y,width,height,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.delete = False
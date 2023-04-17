from .settings import *
from .button import *
import os

# The Save class is a subclass of the Button class. It has the same attributes as the Button class,
# but it also has a screen attribute so as to get the drawing that has to be saved.

class Save(Button) :
    def __init__(self,x,y,width,height,screen,color,unique_id,border_color=LGREY,text=None,text_color=BLACK,icon = None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.screen = screen
        self.unique_id = unique_id
        self.dossier = f"{os.getcwd()}\\frames_{unique_id}"

    def save(self,frame_speed):
        #essayer avec la librairie opencv ?????????
        return
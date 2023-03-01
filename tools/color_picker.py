from .settings import *
from .button import *
from pygame_gui.elements import UIButton
from pygame_gui.windows import UIColourPickerDialog

import pygame_gui
from skimage.color import hsv2rgb

class ColorPicker(Button) :
    def __init__(self,x,y,width,height,color,text=None,text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color  
        self.text = text
        self.text_color = text_color

    def set_color(self):
        ui_manager = pygame_gui.UIManager((800,600))
        color_picker = UIColourPickerDialog(pygame.Rect(160,50,420,400),ui_manager,window_title="Choose color !")
        self.color = color_picker.changed_hsv_update_rgb()
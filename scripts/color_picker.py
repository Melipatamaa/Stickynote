from .settings import *
from .button import *
from pygame_gui.elements import UIButton
from pygame_gui.windows import UIColourPickerDialog

import pygame
import pygame_gui
import colorsys

class ColorPicker(Button) :
    def __init__(self,x,y,width,height,color,text=None,text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color  
        self.text = text
        self.text_color = text_color

    def hsv2rgb(h,s,v):
        return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
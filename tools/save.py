from .settings import *
from .button import *
from tkinter import filedialog, messagebox, colorchooser

class Save(Button) :
    def __init__(self,x,y,width,height,WINDOW,color,text=None,text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.WINDOW = WINDOW

    def save(self):
        filename = filedialog.asksaveasfilename(initialfile="untitled.png",defaultextension="png",filetypes=[("PNG","JPG"),(".png","jpg")])
        print("coucou")
        if filename != "":
            self.image.save(filename)

    def coucou(self):
        print("coucou")
            
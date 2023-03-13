import sys
sys.setrecursionlimit(10**9)

from .settings import *
from .button import *

class Filler(Button) :
    def __init__(self,x,y,width,height,row,col,color,text=None,text_color=BLACK,icon=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.row = row
        self.col = col
        self.color = color  
        self.text = text
        self.text_color = text_color
        self.icon = icon
        self.filling = False

    def fillRec(self,screen, row, col, prev_color, new_color):
        print(row)

        if (row < 0 or row >= (CANVAS_HEIGHT) or col < 0 or col >= (CANVAS_WIDTH) or screen[row][col] != prev_color or screen[row][col] == new_color):
            return
        screen[row][col] = new_color
        self.fillRec(screen, row + 1, col, prev_color, new_color)
        self.fillRec(screen, row - 1, col, prev_color, new_color)
        self.fillRec(screen, row, col + 1, prev_color, new_color)
        self.fillRec(screen, row, col - 1, prev_color, new_color)
 
    def fill(self,screen, row, col, new_color):
        prev_color = screen[row][col]
        if(prev_color==new_color):
            return
        self.fillRec(screen, row, col, prev_color, new_color)
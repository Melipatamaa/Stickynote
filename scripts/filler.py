import sys
sys.setrecursionlimit(100000)

from .settings import *
from .button import *

class Filler(Button) :
    def __init__(self,x,y,width,height,row,col,color,text=None,text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.row = row
        self.col = col
        self.color = color  
        self.text = text
        self.text_color = text_color
        self.filling = False

    def fillRec(self,screen, row, col, prevC, newC):
        if (row < 0 or row >= HEIGHT or col < 0 or col >= WIDTH or screen[row][col] != prevC or screen[row][col] == newC):
            return
        screen[row][col] = newC
        self.fillRec(screen, row + 1, col, prevC, newC)
        self.fillRec(screen, row - 1, col, prevC, newC)
        self.fillRec(screen, row, col + 1, prevC, newC)
        self.fillRec(screen, row, col - 1, prevC, newC)
 
    def fill(self,screen, row, col, newC):
        prevC = screen[row][col]
        if(prevC==newC):
            return
        self.fillRec(screen, row, col, prevC, newC)
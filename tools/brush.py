from .settings import *
from .button import *

class Brush(Button) :
    def __init__(self,x,y,width,height,size,row,col,color,text=None,text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.size = size
        self.row = row
        self.col = col
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw_on_grid(self,grid,drawing_col,row,col,size):
        if size > 1:
            grid[row+1][col] = drawing_col
            grid[row-1][col] = drawing_col
            grid[row][col+1] = drawing_col
            grid[row][col-1] = drawing_col
            if size > 2:
                grid[row+1][col+1] = drawing_col
                grid[row-1][col-1] = drawing_col
                grid[row-1][col+1] = drawing_col
                grid[row+1][col-1] = drawing_col
                grid[row+2][col-1] = drawing_col
                grid[row+2][col] = drawing_col
                grid[row+2][col+1] = drawing_col
                grid[row-2][col-1] = drawing_col
                grid[row-2][col] = drawing_col
                grid[row-2][col+1] = drawing_col
                grid[row-1][col+2] = drawing_col
                grid[row][col+2] = drawing_col
                grid[row+1][col+2] = drawing_col
                grid[row-1][col-2] = drawing_col
                grid[row][col-2] = drawing_col
                grid[row+1][col-2] = drawing_col
                if size > 3:
                    grid[row+2][col+2] = drawing_col
                    grid[row-2][col-2] = drawing_col
                    grid[row-2][col+2] = drawing_col
                    grid[row+2][col-2] = drawing_col
                    grid[row+3][col-1] = drawing_col
                    grid[row+3][col] = drawing_col
                    grid[row+3][col+1] = drawing_col
                    grid[row-3][col-1] = drawing_col
                    grid[row-3][col] = drawing_col
                    grid[row-3][col+1] = drawing_col
                    grid[row-1][col+3] = drawing_col
                    grid[row][col+3] = drawing_col
                    grid[row+1][col+3] = drawing_col
                    grid[row-1][col-3] = drawing_col
                    grid[row][col-3] = drawing_col
                    grid[row+1][col-3] = drawing_col
from ..settings import *
from .button import *

# It's a button that can be clicked to fill a cell in a grid. It inherits from Button.
class Filler(Button) :
    def __init__(self,x,y,width,height,row,col,color,border_color=LGREY,text=None,text_color=BLACK,icon=None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.row = row
        self.col = col
        self.filling = False
        self.recursive_call_cpt = 0

    def fillRec(self,screen, row, col, prev_color, new_color):
        """
        If the current pixel is the same color as the previous pixel, then fill the current pixel with
        the new color and recursively call the function on the pixel to the right, left, top, and bottom
        of the current pixel.
        
        :param screen: 2D array of colors, which represents the pixel colors of the screen,
        :param row: The row of the pixel to be filled,
        :param col: The column of the pixel to be filled,
        :param prev_color: the color of the pixel that you're currently on,
        :param new_color: the color you want to fill the area with,
        :return: the screen with the new color.
        """

        if(self.recursive_call_cpt>2500):
            return
        
        grid_row_min = 17
        grid_col_min = 27
        grid_row_max = 110
        grid_col_max = 175
        self.recursive_call_cpt+=1
        if (row < grid_row_min or row >= grid_row_max or col < grid_col_min or col >= grid_col_max or screen[row][col] != prev_color or screen[row][col] == new_color):
            return
        screen[row][col] = new_color
        self.fillRec(screen, row, col + 1, prev_color, new_color)
        self.fillRec(screen, row, col - 1, prev_color, new_color)
        self.fillRec(screen, row + 1, col, prev_color, new_color)
        self.fillRec(screen, row - 1, col, prev_color, new_color)

 
    def fill(self,screen, row, col, new_color):
        """
        It fills the screen with the new color thanks to fillRec.
        
        :param screen: 2D array of colors, which represents the pixel colors of the screen,
        :param row: The row of the pixel that is clicked,
        :param col: the column of the pixel that is clicked,
        :param new_color: the color you want to change the pixel to,
        :return: the screen with the new cell color.
        """
        prev_color = screen[row][col]
        if(prev_color==new_color):
            return
        self.recursive_call_cpt=0
        self.fillRec(screen, row, col, prev_color, new_color)

    def desactivate_filler(self):
        """
        It sets the filling and button_activated attributes to False so that the feddback can be withdrawn in main.py.
        """
        self.filling = False
        self.button_activated = False
import pygame
from scripts.settings import *
#from copy import deepcopy

# The Grid class is used to create a grid object that can be used to store the state of the drawing.

class Grid:
    def __init__(self,grid=None,rows=ROWS,cols=COLS,color=BACKGROUND_COLOR):
        self.rows = rows
        self.cols = cols
        self.color = color
        if(grid==None):
            self.grid = self.initial_grid()
        else:
            self.grid = grid

    def initial_grid(self):
        """
        It creates a grid of the size of the rows and columns of the canvas and fills it with the color
        of the canvas
        :return: A list of lists.
        """
        grid = []
        for i in range(self.rows):
            grid.append([])
            for j in range(self.cols):
                grid[i].append(self.color)
        return grid
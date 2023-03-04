import pygame
from scripts.settings import *
from copy import deepcopy

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
        grid = []
        for i in range(self.rows):
            grid.append([])
            for j in range(self.cols):
                grid[i].append(self.color)
        return grid
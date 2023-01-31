from tools import *

#display opens the window
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

#name of our window
pygame.display.set_caption("Stickynote Studio")

## ► Grid ◄

def initial_grid(rows,cols,color):
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(color)
    return grid

## ► Drawing ◄

#grid = initial_grid(PX_H,PX_W,BACKGROUND_COLOR)
#for pixel in enumerate(grid):
#    print(pixel)

def draw_grid(win,grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            #print(pixel)
            pygame.draw.rect(win,pixel,(j*PX_SIZE,i*PX_SIZE,PX_SIZE,PX_SIZE)) #original and final coordinates

    if GRID:
        #+1 so the grid won't be cropped by the window 
        for i in range(PX_W + 1):
            pygame.draw.line(win,LGREY,(0,i*PX_SIZE),(WIDTH,i*PX_SIZE))
        for j in range(PX_H + 1):
            pygame.draw.line(win,LGREY,(j*PX_SIZE,0),(j*PX_SIZE,HEIGHT-TOOLBAR_H))

def draw(win, grid, buttons):
    win.fill(BACKGROUND_COLOR)
    draw_grid(win,grid)
    for button in buttons:
        button.draw(win)
    pygame.display.update()

def get_coord_position(pos):
    x, y = pos
    row = y // PX_SIZE
    col = x // PX_SIZE
    if row >= PX_H:
        raise IndexError
    return row, col
    

## ► Program ◄

#variables
using =  True
clock = pygame.time.Clock()
grid = initial_grid(PX_H,PX_W,BACKGROUND_COLOR)
drawing_col = BLACK

button_y = HEIGHT - TOOLBAR_H/2 - 25
buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, ORANGE),
    Button(130, button_y, 50, 50, WHITE, "erase", LGREY)
    ]

while using: #run while the user does not close the window

    #can't be faster than the intial FPS
    clock.tick(FPS) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            using = False

        if pygame.mouse.get_pressed()[0]: #0 for left mouse button
            position = pygame.mouse.get_pos()
            try :
                row, col = get_coord_position(position)
                grid[row][col] = drawing_col
            except IndexError:
                for button in buttons:
                    if not button.clicked(position):
                        continue
                    drawing_col = button.color

    draw(WINDOW, grid, buttons)

pygame.quit()
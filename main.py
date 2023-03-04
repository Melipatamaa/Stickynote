from tools import *

from tools.brush import Brush
from tools.save import Save
from tools.layer import Layer
from tools.pipette import Pipette
from tools.cancel import Cancel
from tools.color_picker import ColorPicker
from tools.grid import *
from copy import deepcopy

#display opens the window
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

#name of our window
pygame.display.set_caption("Stickynote Studio")

## ► Drawing ◄

def create_grid(canvas,grid:Grid):
    for i, row in enumerate(grid.grid):
        for j, pixel in enumerate(row):
            #print(pixel)
            pygame.draw.rect(canvas,pixel,(j*PX_SIZE,i*PX_SIZE,PX_SIZE,PX_SIZE)) #original and final coordinates
    if GRID:
        #+1 so the grid won't be cropped by the window 
        for i in range(ROWS + 1):
            pygame.draw.line(canvas,LGREY,(0,i*PX_SIZE),(WIDTH,i*PX_SIZE))
        for j in range(COLS + 1):
            pygame.draw.line(canvas,LGREY,(j*PX_SIZE,0),(j*PX_SIZE,HEIGHT-TOOLBAR))
    if CANVAS_GRID:
        for i in range(ROWS):
            #+2 pour bien fermer la grille
            pygame.draw.line(canvas,LGREY,(BORDERS_ROWS,BORDERS_COLS+i*PX_SIZE),(WIDTH - BORDERS_ROWS+2,BORDERS_COLS+i*PX_SIZE))
        #pour faire une belle grille propre (ne dépasse pas, 85 et 100 valeurs random pour ROWS = 200)
        for k in range(85,100):
            pygame.draw.line(canvas,WHITE,(BORDERS_ROWS,BORDERS_COLS+k*PX_SIZE),(WIDTH - BORDERS_ROWS+2,BORDERS_COLS+k*PX_SIZE))
        for j in range(COLS):
            pygame.draw.line(canvas,LGREY,(BORDERS_ROWS+j*PX_SIZE,BORDERS_COLS),(BORDERS_ROWS+j*PX_SIZE,HEIGHT-BORDERS_COLS+3))
        #pour faire une belle grille propre
        for l in range(148,180):
            pygame.draw.line(canvas,WHITE,(BORDERS_ROWS+l*PX_SIZE,BORDERS_COLS),(BORDERS_ROWS+l*PX_SIZE,HEIGHT-BORDERS_COLS+3))

def create_all(canvas, grid:Grid, buttons):
    canvas.fill(BACKGROUND_COLOR)
    create_grid(canvas,grid)
    for button in buttons:
        button.draw(canvas)
    for brush in brushes:
        brush.draw(canvas)
    for save in saves:
        save.draw(canvas)
    layer.draw(canvas)
    pipette.draw(canvas)
    cancel.draw(canvas)
    color_picker.draw(canvas)
    pygame.display.update()

def get_coord_position(pos):
    x, y = pos
    row = y // PX_SIZE
    col = x // PX_SIZE
    #modification des valeurs rentrées en focntion des paramètres : pour + tard
    if (col <= 26 or col >= 174 or row <= 16 or row >= 101):
        raise IndexError
    return row, col

def draw_on_grid(grid:Grid,drawing_col,row,col,size):
    if size > 1:
        grid.grid[row+1][col] = drawing_col
        grid.grid[row-1][col] = drawing_col
        grid.grid[row][col+1] = drawing_col
        grid.grid[row][col-1] = drawing_col
        if size > 2:
            grid.grid[row+1][col+1] = drawing_col
            grid.grid[row-1][col-1] = drawing_col
            grid.grid[row-1][col+1] = drawing_col
            grid.grid[row+1][col-1] = drawing_col
            grid.grid[row+2][col-1] = drawing_col
            grid.grid[row+2][col] = drawing_col
            grid.grid[row+2][col+1] = drawing_col
            grid.grid[row-2][col-1] = drawing_col
            grid.grid[row-2][col] = drawing_col
            grid.grid[row-2][col+1] = drawing_col
            grid.grid[row-1][col+2] = drawing_col
            grid.grid[row][col+2] = drawing_col
            grid.grid[row+1][col+2] = drawing_col
            grid.grid[row-1][col-2] = drawing_col
            grid.grid[row][col-2] = drawing_col
            grid.grid[row+1][col-2] = drawing_col
            if size > 3:
                grid.grid[row+2][col+2] = drawing_col
                grid.grid[row-2][col-2] = drawing_col
                grid.grid[row-2][col+2] = drawing_col
                grid.grid[row+2][col-2] = drawing_col
                grid.grid[row+3][col-1] = drawing_col
                grid.grid[row+3][col] = drawing_col
                grid.grid[row+3][col+1] = drawing_col
                grid.grid[row-3][col-1] = drawing_col
                grid.grid[row-3][col] = drawing_col
                grid.grid[row-3][col+1] = drawing_col
                grid.grid[row-1][col+3] = drawing_col
                grid.grid[row][col+3] = drawing_col
                grid.grid[row+1][col+3] = drawing_col
                grid.grid[row-1][col-3] = drawing_col
                grid.grid[row][col-3] = drawing_col
                grid.grid[row+1][col-3] = drawing_col

#def get_size(grid,row,col,size):
    if size > 1:
        grid.grid[row+1][col] = drawing_col
        grid.grid[row-1][col] = drawing_col
        grid.grid[row][col+1] = drawing_col
        grid.grid[row][col-1] = drawing_col
        if size > 2:
            grid.grid[row+1][col+1] = drawing_col
            grid.grid[row-1][col-1] = drawing_col
            grid.grid[row-1][col+1] = drawing_col
            grid.grid[row+1][col-1] = drawing_col
            grid.grid[row+2][col-1] = drawing_col
            grid.grid[row+2][col] = drawing_col
            grid.grid[row+2][col+1] = drawing_col
            grid.grid[row-2][col-1] = drawing_col
            grid.grid[row-2][col] = drawing_col
            grid.grid[row-2][col+1] = drawing_col
            grid.grid[row-1][col+2] = drawing_col
            grid.grid[row][col+2] = drawing_col
            grid.grid[row+1][col+2] = drawing_col
            grid.grid[row-1][col-2] = drawing_col
            grid.grid[row][col-2] = drawing_col
            grid.grid[row+1][col-2] = drawing_col
            if size > 3:
                grid.grid[row+2][col+2] = drawing_col
                grid.grid[row-2][col-2] = drawing_col
                grid.grid[row-2][col+2] = drawing_col
                grid.grid[row+2][col-2] = drawing_col
                grid.grid[row+3][col-1] = drawing_col
                grid.grid[row+3][col] = drawing_col
                grid.grid[row+3][col+1] = drawing_col
                grid.grid[row-3][col-1] = drawing_col
                grid.grid[row-3][col] = drawing_col
                grid.grid[row-3][col+1] = drawing_col
                grid.grid[row-1][col+3] = drawing_col
                grid.grid[row][col+3] = drawing_col
                grid.grid[row+1][col+3] = drawing_col
                grid.grid[row-1][col-3] = drawing_col
                grid.grid[row][col-3] = drawing_col
                grid.grid[row+1][col-3] = drawing_col
    return 

## ► Program ◄

#variables
using =  True
clock = pygame.time.Clock()
grid = Grid()
drawing_col = BLACK
size = 1

#list for x coordinates of buttons
X = []
for i in range(11):
    X.append(30 + i*45)
button_x = 30
button_w_h = 30
buttons = [
    Button(button_x, X[0], button_w_h, button_w_h, BLACK),
    Button(button_x, X[1], button_w_h, button_w_h, GREY),
    Button(button_x, X[2], button_w_h, button_w_h, PURPLE),
    Button(button_x, X[3], button_w_h, button_w_h, BLUE),
    Button(button_x, X[4], button_w_h, button_w_h, GREEN),
    Button(button_x, X[5], button_w_h, button_w_h, YELLOW),
    Button(button_x, X[6], button_w_h, button_w_h, ORANGE),
    Button(button_x, X[7], button_w_h, button_w_h, RED),
    Button(button_x, X[8], button_w_h, button_w_h, PINK),
    Button(button_x, X[9], button_w_h, button_w_h, WHITE, "erase", LGREY),
    Button(button_x, X[10], button_w_h, button_w_h, WHITE, "clear", LGREY)
    ]

brushes = [ 
    Brush(button_x*2 + 10, X[0], button_w_h, button_w_h, 1, 1, 1, WHITE, "1", LGREY),
    Brush(button_x*2 + 10, X[1], button_w_h, button_w_h, 2, 1, 1, WHITE, "2", LGREY),
    Brush(button_x*2 + 10, X[2], button_w_h, button_w_h, 3, 1, 1, WHITE, "3", LGREY),
    Brush(button_x*2 + 10, X[3], button_w_h, button_w_h, 4, 1, 1, WHITE, "4", LGREY)
    ]

saves = [
    Save(button_x*2 + 10, X[4], button_w_h, button_w_h, WINDOW, WHITE, "save", LGREY)
]

layer = Layer(1075, X[2], button_w_h + 60, button_w_h + 20, WINDOW, WHITE, "Layer", LGREY)

pipette = Pipette(button_x*2 + 10, X[5], button_w_h, button_w_h, 1, 1, WHITE, "pip", LGREY)

cancel = Cancel(1075, X[4], button_w_h + 60, button_w_h + 20, WINDOW, WHITE, "◄◄", LGREY)

color_picker = ColorPicker(button_x*2 + 10, X[5], button_w_h, button_w_h, WHITE, "colorpic", LGREY)

visible = False
cancelled = False

states_of_drawing = [deepcopy(grid)]
nb_actions = 0
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
                if pipette.activated:
                    drawing_col = grid.grid[row][col]
                    pipette.color = drawing_col
                    pipette.activated = False
                else:
                    grid.grid[row][col] = drawing_col
                    draw_on_grid(grid,drawing_col,row,col,size)
                    #print(states_of_drawing[0][0])
                    if(len(states_of_drawing)<=100):
                        newgrid = Grid([[i for i in row] for row in grid.grid])
                        states_of_drawing.append(newgrid)
                    else:
                        del states_of_drawing[0]
                        newgrid = Grid([[i for i in row] for row in grid.grid])
                        # for row in grid.grid:
                        #     for i in row:
                        #         newgrid[row][i] = i
                        states_of_drawing.append(newgrid)
            except IndexError:
                for button in buttons:
                    if not button.clicked(position):
                        continue
                    if button.text == "clear":
                        grid = Grid()
                    drawing_col = button.color
                for brush in brushes:
                    if not brush.clicked(position):
                        continue
                    size = brush.size
                if color_picker.clicked(position):
                    color_picker.set_color(WINDOW)
                    print("pouet")
                for save in saves:
                    if not save.clicked(position):
                        continue
                    save.save(WINDOW)
                if pipette.clicked(position):
                    pipette.activated = True
                if layer.clicked(position):
                    visible = True
                if cancel.clicked(position):
                    cancelled = True
    if cancelled:
        #matches = [match for match in grid if (0,0,0) in match]
        if(len(states_of_drawing)>0):
            grid = states_of_drawing[-1]
            del states_of_drawing[-1]

        create_all(WINDOW, grid, buttons)
    else :
        create_all(WINDOW, grid, buttons)
    layer.stick_layer(WINDOW,visible)
    cancelled = False
pygame.quit()
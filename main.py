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

def draw_grid(canvas,grid):
    for i, row in enumerate(grid):
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
        for i in range(ROWS + 1):
            pygame.draw.line(canvas,BLACK,(BORDERS_ROWS,i*PX_SIZE),(WIDTH - BORDERS_ROWS,i*PX_SIZE))
        for j in range(COLS + 1):
            pygame.draw.line(canvas,RED,(j*PX_SIZE,BORDERS_COLS),(j*PX_SIZE,HEIGHT-BORDERS_COLS))


def draw(canvas, grid, buttons):
    canvas.fill(BACKGROUND_COLOR)
    draw_grid(canvas,grid)
    for button in buttons:
        button.draw(canvas)
    pygame.display.update()

def get_coord_position(pos):
    x, y = pos
    row = y // PX_SIZE
    col = x // PX_SIZE
    if (row >= COLS or col >= ROWS):
        raise IndexError
    return row, col
    

## ► Program ◄

#variables
using =  True
clock = pygame.time.Clock()
grid = initial_grid(COLS,ROWS,BACKGROUND_COLOR)
drawing_col = BLACK

#list for x coordinates of buttons
X = []
for i in range(10):
    X.append(30 + i*60)
button_x = 30
buttons = [
    Button(button_x, X[0], 50, 50, BLACK),
    Button(button_x, X[1], 50, 50, GREY),
    Button(button_x, X[2], 50, 50, PURPLE),
    Button(button_x, X[3], 50, 50, BLUE),
    Button(button_x, X[4], 50, 50, GREEN),
    Button(button_x, X[5], 50, 50, YELLOW),
    Button(button_x, X[6], 50, 50, ORANGE),
    Button(button_x, X[7], 50, 50, RED),
    Button(button_x, X[8], 50, 50, PINK),
    Button(button_x, X[9], 50, 50, WHITE, "erase", LGREY)
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
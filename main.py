import pygame
import pygame_gui

from pygame_gui.windows import UIColourPickerDialog

from scripts.settings import *
from scripts import Button
from scripts.brush import Brush
from scripts.save import Save
from scripts.layer import Layer
from scripts.pipette import Pipette
from scripts.cancel import Cancel
from scripts.color_picker import ColorPicker
from scripts.filler import Filler
from scripts.add_frame import AddFrame
from scripts.choose_frame import ChooseFrame

from scripts.grid import *
from scripts.utils import *

import colorsys
from copy import deepcopy

#display opens the window
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

#name of our window
pygame.display.set_caption("Stickynote Studio")

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
    Button(button_x, X[9], button_w_h, button_w_h, WHITE, icon=pygame.image.load('scripts\icons\\gomme.png')),
    Button(button_x, X[10], button_w_h, button_w_h, WHITE, icon=pygame.image.load('scripts\icons\\clear.png'))
    ]

brushes = [ 
    Brush(button_x*2 + 10, X[0], button_w_h, button_w_h, 1, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\size_one.png')),
    Brush(button_x*2 + 10, X[1], button_w_h, button_w_h, 2, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\size_two.png')),
    Brush(button_x*2 + 10, X[2], button_w_h, button_w_h, 3, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\size_three.png')),
    Brush(button_x*2 + 10, X[3], button_w_h, button_w_h, 4, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\size_four.png'))
    ]

saves = [
    Save(button_x*2 + 10, X[4], button_w_h, button_w_h, WINDOW, WHITE, icon=pygame.image.load('scripts\icons\\save.png'))
]

layer = Layer(1075, X[2], button_w_h + 60, button_w_h + 20, WINDOW, WHITE, LGREY, "Layer", LGREY)

pipette = Pipette(button_x*2 + 10, X[5], button_w_h, button_w_h, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\pipette.png'))

cancel = Cancel(1075, X[4], button_w_h + 60, button_w_h + 20, WINDOW, WHITE, LGREY, "◄◄", LGREY)

color_picker = ColorPicker(button_x*2 + 10, X[6], button_w_h, button_w_h, WHITE, icon=pygame.image.load('scripts\icons\\colorpick.png'))

filler = Filler(button_x*2 + 10, X[7], button_w_h, button_w_h, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\fill.png'))

add_frame = AddFrame(1075, X[6], button_w_h + 60, button_w_h + 20, WHITE, LGREY, "Add frame", LGREY)
previous_frame = ChooseFrame(1075, X[8], button_w_h + 60, button_w_h + 20, WHITE, LGREY, "prev frame", LGREY)
next_frame = ChooseFrame(1075, X[10], button_w_h + 60, button_w_h + 20, WHITE, LGREY, "next frame", LGREY)

# utilise les variables globales
def create_all(canvas, grid:Grid,open_picker):
    canvas.fill(BACKGROUND_COLOR)
    if(open_picker):
        ui_manager.update(time_delta)
        ui_manager.draw_ui(WINDOW)
    else:
        draw_grid_on_canvas(canvas,grid)
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
        filler.draw(canvas)
        add_frame.draw(canvas)
        previous_frame.draw(canvas)
        next_frame.draw(canvas)

    pygame.display.update()
    
visible = False
cancelled = False
ui_manager = pygame_gui.UIManager((800, 600))
is_picker_opened = False
states_of_drawing = [deepcopy(grid)]
nb_actions = 0

animation_list = [deepcopy(grid)]

while using: #run while the user does not close the window

    #can't be faster than the intial FPS
    time_delta = clock.tick(FPS)/1000

    for event in pygame.event.get():
        ui_manager.process_events(event)
        if event.type == pygame.QUIT:
            using = False
        if(is_picker_opened==False):
            if pygame.mouse.get_pressed()[0]: #0 for left mouse button
                position = pygame.mouse.get_pos()
                try :
                    row, col = get_coord_position(position)
                    if pipette.activated:
                        drawing_col = grid.grid[row][col]
                        pipette.color = drawing_col
                        pipette.activated = False
                    if filler.filling:
                        filler.fill(grid.grid,row,col,drawing_col)
                    else:
                        grid.grid[row][col] = drawing_col
                        draw_on_grid(grid,drawing_col,row,col,size)
                        if(len(states_of_drawing)<=100):
                            newgrid = Grid([[i for i in row] for row in grid.grid])
                            states_of_drawing.append(newgrid)
                        else:
                            del states_of_drawing[0]
                            newgrid = Grid([[i for i in row] for row in grid.grid])
                            states_of_drawing.append(newgrid)
                except IndexError:
                    filler.filling = False
                    for button in buttons:
                        if not button.clicked(position):
                            continue
                        if button.text == "clear":
                            grid = Grid()
                        drawing_col = button.color
                        button.give_feedback()
                    for brush in brushes:
                        if not brush.clicked(position):
                            continue
                        size = brush.size
                        brush.give_feedback()
                    if color_picker.clicked(position):
                        colour_picker = UIColourPickerDialog(pygame.Rect(160,50,420,400), ui_manager, window_title="change colour",initial_colour=pygame.Color(drawing_col))
                        is_picker_opened=True
                        color_picker.give_feedback()
                    for save in saves:
                        if not save.clicked(position):
                            continue
                        save.save(WINDOW)
                        save.give_feedback()
                    if pipette.clicked(position):
                        pipette.activated = True
                        pipette.give_feedback()
                    if layer.clicked(position):
                        visible = True
                        layer.give_feedback()
                    if cancel.clicked(position):
                        cancelled = True
                        cancel.give_feedback()
                    if filler.clicked(position):
                        filler.filling = True
                        filler.give_feedback()
                    if add_frame.clicked(position):
                        add_frame.add = True
                        new_frame = Grid()
                        animation_list.append(new_frame)
                    if previous_frame.clicked(position):
                        #previous_frame.choose = True
                        grid = animation_list[-1]
                    if next_frame.clicked(position):
                        #next_frame.choose = True
                        grid = animation_list[-1]      
        else:
            if event.type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED:
                is_picker_opened=False
                drawing_col = event.colour
                color_picker.color = event.colour
            if event.type ==pygame_gui.UI_WINDOW_CLOSE:
                is_picker_opened = False
    if cancelled:
        if(len(states_of_drawing)>0):
            grid = states_of_drawing[-1]
            del states_of_drawing[-1]
        create_all(WINDOW, grid,is_picker_opened)
    if add_frame.add:
        create_all(WINDOW, new_frame,is_picker_opened)
        grid = new_frame
        add_frame.add = False
    else :
        create_all(WINDOW, grid,is_picker_opened)
    layer.stick_layer(WINDOW,visible)
    cancelled = False
pygame.quit()
import pygame
import pygame_gui

# Importing the modules from the scripts folder.
from pygame_gui.windows import UIColourPickerDialog

from scripts.settings import *
from scripts.color import Color
from scripts.brush import Brush
from scripts.clear import Clear
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

from copy import deepcopy

# Creating a window with the dimensions of WIDTH and HEIGHT.
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

# Setting the title of the window : Stickynote Studio
pygame.display.set_caption("Stickynote Studio")

# Initializing the variables.
using =  True
clock = pygame.time.Clock()
grid = Grid()
drawing_col = BLACK
size = 1

# list for x coordinates of some buttons
X = []
for i in range(11):
    X.append(105 + i*45)
button_x = 50
button_w_h = 30

# Creating a list of colors
colors = [
    Color(button_x, X[0], button_w_h, button_w_h, BLACK),
    Color(button_x, X[1], button_w_h, button_w_h, GREY),
    Color(button_x, X[2], button_w_h, button_w_h, PURPLE),
    Color(button_x, X[3], button_w_h, button_w_h, BLUE),
    Color(button_x, X[4], button_w_h, button_w_h, GREEN),
    Color(button_x, X[5], button_w_h, button_w_h, YELLOW),
    Color(button_x, X[6], button_w_h, button_w_h, ORANGE),
    Color(button_x, X[7], button_w_h, button_w_h, RED),
    Color(button_x, X[8], button_w_h, button_w_h, PINK),
    Color(button_x + 45, X[10], button_w_h, button_w_h, WHITE, icon=pygame.image.load('scripts\icons\\gomme.png')),
    ]

# Creating a list of brushes
brushes = [ 
    Brush(button_x + 45, X[0], button_w_h, button_w_h, 1, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\size_one.png')),
    Brush(button_x + 45, X[1], button_w_h, button_w_h, 2, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\size_two.png')),
    Brush(button_x + 45, X[2], button_w_h, button_w_h, 3, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\size_three.png')),
    Brush(button_x + 45, X[3], button_w_h, button_w_h, 4, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\size_four.png')),
    Brush(button_x + 45, X[4], button_w_h, button_w_h, 5, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\verti.png')),
    Brush(button_x + 45, X[5], button_w_h, button_w_h, 6, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\horiz.png'))
    ]

# Creating the other buttons needed

# Clearing the canvas, erasing everything
clear = Clear(button_x, X[10], button_w_h, button_w_h, WHITE, icon=pygame.image.load('scripts\icons\\clear.png'))
# Saving the drawing
save = Save(button_x + 45, X[10] + 30, button_w_h, button_w_h, WINDOW, WHITE, icon=pygame.image.load('scripts\icons\\save.png'))
# Adding a reference layer
layer = Layer(1075, X[1] + 20, button_w_h + 60, button_w_h + 20, WINDOW, WHITE, LGREY, "Layer", LGREY)
# Getting the color of any pixel on the drawing
pipette = Pipette(button_x + 45, X[6], button_w_h, button_w_h, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\pipette.png'))
# Cancelling the previous drawings
cancel = Cancel(1075, X[0], button_w_h + 60, button_w_h + 20, WINDOW, WHITE, LGREY, "◄◄", LGREY)
# Choosing any color from the RGB/TSL codes
color_picker = ColorPicker(button_x + 45, X[7], button_w_h, button_w_h, WHITE, icon=pygame.image.load('scripts\icons\\colorpick.png'))
# Filling a cell with the drawing color
filler = Filler(button_x + 45, X[8], button_w_h, button_w_h, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\fill.png'))
# Adding a new frame to the animation
add_frame = AddFrame(1075, X[4], button_w_h + 60, button_w_h + 20, WHITE, LGREY, "Add frame", LGREY)
# Getting back to a previous frame already created
previous_frame = ChooseFrame(1075, X[5] + 20, button_w_h + 60, button_w_h + 20, WHITE, LGREY, "prev frame", LGREY)
# Getting forward to the next frame already created
next_frame = ChooseFrame(1075, X[6] + 40, button_w_h + 60, button_w_h + 20, WHITE, LGREY, "next frame", LGREY)

# Loading the image of Stikynote Studio and rescaling it.
sticky = pygame.image.load('scripts\icons\\sticky.png')
sticky = pygame.transform.scale(sticky, (250, 72))

def create_all(canvas, grid:Grid,open_picker):
    """
    This method creates the interface of Stickynote Studio. It draws the grid, the colors, the brushes, 
    the clear button, the save button, the layer button, the pipette button, the cancel button, 
    the color picker button, the filler button, the add frame button, the previous frame button,
    and the next frame button.
    If the color picker is clicked, the interface is entirely redrawn and just displays the color wheel,
    and not the background of the drawing not to interact with it.
    
    :param canvas: The canvas that the grid is drawn on,
    :param grid: the grid object,
    :param open_picker: boolean, if true, the color picker is opened
    """
    #canvas.fill(BACKGROUND_COLOR)
    if(open_picker):
        ui_manager.update(time_delta)
        ui_manager.draw_ui(WINDOW)
    else:
        draw_grid_on_canvas(canvas,grid)
        display_interface(WINDOW,sticky)
        for color in colors:
            color.draw(canvas)
        for brush in brushes:
            brush.draw(canvas)
        clear.draw(canvas)
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
    
# Initializing other variables that will be used in the program.
visible = False
cancelled = False
ui_manager = pygame_gui.UIManager((800, 600))
is_picker_opened = False
states_of_drawing = [deepcopy(grid)]
animation_list = [deepcopy(grid)]

while using: # Running while the user does not close the window
    clear.button_activated = False
    cancel.button_activated = False
    save.button_activated = False
    # Setting the FPS
    time_delta = clock.tick(FPS)/1000
    for event in pygame.event.get():
        ui_manager.process_events(event)
        # Checking if the user has clicked on the red cross to close the window. If so, the program
        # stops.
        if event.type == pygame.QUIT:
            using = False
        if(is_picker_opened==False):
            if pygame.mouse.get_pressed()[0]: #0 for left mouse button
                position = pygame.mouse.get_pos()
                try :
                    row, col = get_coord_position(position)
                    # Checking if the pipette is activated. If it is, it sets the drawing color to the
                    # color of the grid square that the mouse is hovering over. It then deactivates
                    # the pipette and the pipette button.
                    if pipette.activated:
                        drawing_col = grid.grid[row][col]
                        pipette.color = drawing_col
                        pipette.activated = False
                        pipette.button_activated = False
                    # Filling the grid with the color of the drawing_col.
                    if filler.filling:
                        filler.fill(grid.grid,row,col,drawing_col)
                    # Drawing on the grid and saving every state of drawing so it can be cancelled later
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
                # If a button is clicked
                except IndexError:
                    # Checking if the mouse is clicked on the color button. If it is, it sets the
                    # drawing color to the color of the button. It also deselects all other color
                    # buttons and the color picker and pipette.
                    for color in colors:
                        if not color.clicked(position):
                            continue
                        drawing_col = color.color
                        color.button_activated = True
                        # desactive tous les autres boutons colors
                        for c in colors:
                            if(c!=color):
                                c.button_activated=False
                        color_picker.button_activated=False
                        pipette.button_activated=False
                    # Checking if the brush is clicked and if it is, it sets the size of the brush to
                    # the size of the brush that was clicked. It also sets the button_activated
                    # variable to True.
                    for brush in brushes:
                        if not brush.clicked(position):
                            continue
                        size = brush.size
                        brush.button_activated = True   
                        for b in brushes:
                            if(b!=brush):
                                b.button_activated=False
                        filler.desactivate_filler()
                    # Opening a color picker dialog box.
                    if color_picker.clicked(position):
                        colour_picker = UIColourPickerDialog(pygame.Rect(160,50,420,400), ui_manager, window_title="change colour",initial_colour=pygame.Color(drawing_col))
                        is_picker_opened = True
                        color_picker.button_activated = True
                        for c in colors:
                            c.button_activated = False
                    # Checking if the clear button is clicked.
                    if clear.clicked(position):
                        grid = Grid()
                        clear.button_activated = True
                    # Saving the drawing
                    if save.clicked(position):
                        if not save.clicked(position):
                            continue
                        save.save(WINDOW)
                        save.button_activated = True
                    # Checking if the pipette button is clicked. If it is, it sets the pipette button
                    # to activated. If the pipette button is activated, it sets the pipette button to
                    # not activated. If the pipette button is not activated, it sets the pipette
                    # button to activated. It then sets all the other color buttons to not activated
                    # and the color picker button to not activated. It then desactivates the filler.
                    if pipette.clicked(position):
                        pipette.activated = True
                        if(pipette.button_activated):
                            pipette.button_activated = False
                        else:
                            pipette.button_activated = True
                        for c in colors:
                            c.button_activated=False
                        color_picker.button_activated=False
                        filler.desactivate_filler()
                    # Checking if the button is clicked and if it is, it sets the visibility to true.
                    # If the button is activated, it sets the button to false. If the button is not
                    # activated, it sets the button to true.
                    if layer.clicked(position):
                        visible = True
                        if(layer.button_activated):
                            layer.button_activated = False
                        else:
                            layer.button_activated = True
                    # Checking if the cancel button is clicked and setting it to activated.
                    if cancel.clicked(position):
                        cancelled = True
                        cancel.button_activated = True
                    # Checking if the mouse is clicked on the filler button. If it is, it checks if
                    # the filler is activated. If it is, it deactivates it. If it isn't, it activates
                    # it. It desactivates all the brushes and the pipette.
                    if filler.clicked(position):
                        if(filler.button_activated):
                            filler.desactivate_filler()
                        else:
                            filler.filling = True
                            filler.button_activated = True
                            for b in brushes:
                                b.button_activated=False
                            pipette.button_activated = False
                    # Adding a new frame to the animation list if the button is clicked.
                    if add_frame.clicked(position):
                        add_frame.add = True
                        new_frame = Grid()
                        animation_list.append(new_frame)
                    # Checking if the previous frame button is clicked. If it is, it sets the grid to the
                    # last frame in the animation list.
                    if previous_frame.clicked(position):
                        #previous_frame.choose = True
                        grid = animation_list[-1]
                    if next_frame.clicked(position):
                        #next_frame.choose = True
                        grid = animation_list[-1]      
        else:
            # Setting the color of the color picker to the color that was picked and closing it when it is done.
            if event.type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED:
                is_picker_opened=False
                drawing_col = event.colour
                color_picker.color = event.colour
            if event.type ==pygame_gui.UI_WINDOW_CLOSE:
                is_picker_opened = False
    # Checking if the user has cancelled the drawing. If so, it will remove the last drawing from the
    # list of drawings and update the grid with the previous drawing.
    if cancelled:
        if(len(states_of_drawing)>0):
            grid = states_of_drawing[-1]
            del states_of_drawing[-1]
        create_all(WINDOW, grid,is_picker_opened)
    elif add_frame.add:
        create_all(WINDOW, new_frame,is_picker_opened)
        grid = new_frame
        add_frame.add = False
    # Creating a window and then creating a grid : continuously updated.
    else :
        create_all(WINDOW, grid,is_picker_opened)
    layer.stick_layer(WINDOW,visible)
    cancelled = False
pygame.quit()
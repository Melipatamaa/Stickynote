import pygame
import pygame_gui
import time

from pygame_gui.windows import UIColourPickerDialog

# Importing the modules from the scripts folder.
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
from scripts.remove_frame import RemoveFrame
from scripts.speed import Speed
from scripts.play import Play
from scripts.copy_frame import CopyFrame
from scripts.grid_pattern import GridPattern

from scripts.grid import *
from scripts.utils import *

from copy import deepcopy

# Creating a window with the dimensions of WIDTH and HEIGHT.
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

# Setting the title of the window : Stickynote Studio
pygame.display.set_caption("Stickynote Studio")

# Initializing the variables.
is_grid_pattern_on = False
using =  True
clock = pygame.time.Clock()
grid = Grid()
drawing_col = BLACK
size = 1
current_frame_index = 0
visible = False
was_visible = False
frame_speed = 1000
animation_list = [grid] 
unique_id = str(time.time())
cancelled = False
ui_manager = pygame_gui.UIManager((800, 600))
is_picker_opened = False
states_of_drawing = [deepcopy(grid)]

# list for x coordinates of some buttons
X = []
for i in range(11):
    X.append(105 + i*45)
button_x = 50
button_w_h = 30

# Displaying a grid on the canvas so it can be used as a reference
grid_pattern = GridPattern(1068, X[3] + 20, button_w_h + 60, button_w_h + 20, WHITE, icon=pygame.image.load('scripts\icons\\gridpattern.png'))

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
clear = Clear(button_x, X[10], button_w_h, button_w_h, WHITE, icon=pygame.image.load(f'{os.getcwd()}\\scripts\icons\\clear.png'))
# Saving the drawing
save = Save(1085, X[1] + 30, button_w_h + 20, button_w_h + 20, WINDOW, WHITE, unique_id=unique_id, icon=pygame.image.load('scripts\icons\\save.png'))
# Adding a reference layer
layer = Layer(1068, X[5] + 10, button_w_h + 60, button_w_h + 20, WINDOW, WHITE,unique_id=unique_id, icon=pygame.image.load('scripts\icons\\layer.png'))
# Getting the color of any pixel on the drawing
pipette = Pipette(button_x + 45, X[6], button_w_h, button_w_h, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\pipette.png'))
# Cancelling the previous drawings
cancel = Cancel(1085, X[0], button_w_h + 20, button_w_h + 20, WINDOW, WHITE, icon=pygame.image.load('scripts\icons\\undo.png'))
# Choosing any color from the RGB/TSL codes
color_picker = ColorPicker(button_x + 45, X[7], button_w_h, button_w_h, WHITE, icon=pygame.image.load('scripts\icons\\colorpick.png'))
# Filling a cell with the drawing color
filler = Filler(button_x + 45, X[8], button_w_h, button_w_h, 1, 1, WHITE, icon=pygame.image.load('scripts\icons\\fill.png'))
# Adding a new frame to the animation
add_frame = AddFrame(1068, X[6] + 30, button_w_h + 60, button_w_h + 20, WHITE, icon=pygame.image.load('scripts\icons\\add.png'))
# Copying the current frame for the next one
copy_frame = CopyFrame(1068, X[7] + 50, button_w_h + 60, button_w_h + 20, WHITE, icon=pygame.image.load('scripts\icons\\copy.png'))
# Getting back to a previous frame already created
previous_frame = ChooseFrame(730, HEIGHT - 85, button_w_h + 20, button_w_h + 20, WHITE, icon=pygame.image.load('scripts\icons\\prev.png'))
# Getting forward to the next frame already created
next_frame = ChooseFrame(730 + 160, HEIGHT - 85, button_w_h + 20, button_w_h + 20, WHITE, icon=pygame.image.load('scripts\icons\\next.png'))
# Removing a whole frame from the animation
remove_frame = RemoveFrame(1068, X[8] + 70, button_w_h + 60, button_w_h + 20, WHITE, icon=pygame.image.load('scripts\icons\\copy.png'))
# Setting the frame rate of the animation with 8 differents speeds
speeds = [
    Speed(120 + X[0], HEIGHT - 80, button_w_h, button_w_h, 1000, WHITE,LGREY, "1", ORANGE),
    Speed(120 + X[1], HEIGHT - 80, button_w_h, button_w_h, 800, WHITE, LGREY, "2", ORANGE),
    Speed(120 + X[2], HEIGHT - 80, button_w_h, button_w_h, 600, WHITE, LGREY, "3", ORANGE),
    Speed(120 + X[3], HEIGHT - 80, button_w_h, button_w_h, 400, WHITE, LGREY, "4", ORANGE),
    Speed(120 + X[4], HEIGHT - 80, button_w_h, button_w_h, 200, WHITE, LGREY, "5", ORANGE),
    Speed(120 + X[5], HEIGHT - 80, button_w_h, button_w_h, 100, WHITE, LGREY, "6", ORANGE),
    Speed(120 + X[6], HEIGHT - 80, button_w_h, button_w_h, 50, WHITE, LGREY, "7", ORANGE),
    Speed(120 + X[7], HEIGHT - 80, button_w_h, button_w_h, 25, WHITE, LGREY, "8", ORANGE)
    ]
# Playing a preview of the animation
play = Play(730 + 80, HEIGHT - 85, button_w_h + 20, button_w_h + 20, animation_list, WHITE,icon=pygame.image.load('scripts\icons\\play.png'))

# Loading the image of Stikynote Studio and rescaling it.
sticky = pygame.image.load('scripts\icons\\sticky.png')
sticky = pygame.transform.scale(sticky, (250, 72))

def create_all(canvas, grid:Grid,open_picker,visible):
    """
    This function creates all the necessary elements on the canvas for a drawing program, including the
    grid, interface, color and brush options, and buttons for various actions.
    
    :param canvas: The canvas on which the drawing will be displayed
    :param grid: A Grid object that represents the grid on which the user can draw
    :type grid: Grid
    :param open_picker: A boolean value that indicates whether the color picker UI should be open or
    not. If it is True, the color picker UI will be updated and drawn on the canvas. If it is False, the
    regular drawing tools and buttons will be displayed on the canvas
    :param visible: A boolean value indicating whether or not a layer is currently visible. If it is
    True, the layer will be displayed on the canvas. If it is False, the layer will not be displayed
    """
    draw_grid_on_canvas(canvas,grid,is_grid_pattern_on)
    display_interface(WINDOW,sticky)
    get_frame_number(WINDOW,current_frame_index,animation_list)
    if(open_picker):
        ui_manager.update(time_delta)
        ui_manager.draw_ui(WINDOW)
    else:
        if(visible):
            layer.stick_layer(WINDOW,visible,current_frame_index)
        for color in colors:
            color.draw(canvas)
        for brush in brushes:
            brush.draw(canvas)
        grid_pattern.draw(canvas)
        clear.draw(canvas)
        save.draw(canvas)
        layer.draw(canvas)
        pipette.draw(canvas)
        cancel.draw(canvas)
        color_picker.draw(canvas)
        filler.draw(canvas)
        add_frame.draw(canvas)
        copy_frame.draw(canvas)
        previous_frame.draw(canvas)
        next_frame.draw(canvas)
        remove_frame.draw(canvas)
        for speed in speeds:
            speed.draw(canvas)
        play.draw(canvas)
    pygame.display.update()

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
                        # Dealing with cancel related actions. A save of the canvas is made in the states_of_drawing,
                        # which is a FIFO, and it can save a maximum of 100 canvas.
                        if(len(states_of_drawing)<=100):
                            # Recreating the whole drawing by hand instead of calling deepcopy for speed purposes
                            newgrid = Grid([[i for i in row] for row in grid.grid])
                            states_of_drawing.append(newgrid)
                        else:
                            # According to the FIFO method, the first drawing saved is deleted to make place for 
                            # the new canvas.
                            del states_of_drawing[0]
                            newgrid = Grid([[i for i in row] for row in grid.grid])
                            states_of_drawing.append(newgrid)
                # If a button is clicked
                except IndexError:
                    # Checking if the mouse is clicked on the grid_pattern button. If so, it displays a grid reference
                    # if it was not already on screen by setting the parameters to True. To desactivate this tool, the user
                    # clicks on the button again and the parameters are updated and set up to False.
                    if grid_pattern.clicked(position):
                        if(grid_pattern.button_activated):
                            grid_pattern.button_activated = False
                            is_grid_pattern_on = False
                        else:
                            grid_pattern.button_activated = True
                            is_grid_pattern_on = True
                    # Checking if the mouse is clicked on the color button. If it is, it sets the
                    # drawing color to the color of the button. It also deselects all other color
                    # buttons and the color picker and pipette.
                    for color in colors:
                        if not color.clicked(position):
                            continue
                        drawing_col = color.color
                        color.button_activated = True
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
                    # Saving the drawing as an animation
                    if save.clicked(position):
                        if not save.clicked(position):
                            continue
                        save.save(frame_speed)
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
                            visible = False
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
                        save_frame(WINDOW,current_frame_index,unique_id)
                        add_frame.add = True
                        current_frame_index+=1
                        new_frame = Grid()
                        animation_list.insert(current_frame_index,new_frame)
                        add_frame.button_activated = True
                    # Adding a new frame by copying the current one. It is added to the animation list.
                    if copy_frame.clicked(position):
                        save_frame(WINDOW,current_frame_index,unique_id)
                        copy_frame.copy = True
                        current_frame_index+=1
                        new_frame = grid
                        animation_list.insert(current_frame_index,new_frame)
                        copy_frame.button_activated = True
                    # Checking if the previous frame button is clicked. If it is, it sets the grid to the
                    # last frame in the animation list.
                    if previous_frame.clicked(position):
                        if(current_frame_index>=1):
                            save_frame(WINDOW,current_frame_index,unique_id)
                            current_frame_index-=1
                            grid = animation_list[current_frame_index]
                            previous_frame.button_activated = True
                    # Same thing, but it sets the grid to the next frame in the animation list.
                    if next_frame.clicked(position):
                        if(current_frame_index < len(animation_list)-1):
                            save_frame(WINDOW,current_frame_index,unique_id)
                            current_frame_index+=1
                            grid = animation_list[current_frame_index]
                            delete_frame.delete = True
                            next_frame.button_activated = True
                    # Removing a whole frame from the animation list.
                    if remove_frame.clicked(position):
                        if(current_frame_index>=1):
                            # Calling delete_frame in utils
                            delete_frame(current_frame_index,unique_id)
                            frame_to_delete = grid
                            animation_list.remove(frame_to_delete)
                            current_frame_index-=1
                            grid = animation_list[current_frame_index]
                            remove_frame.button_activated = True
                    # Setting the frame rate of the animation preview. It also desactivates the other 
                    # speeds on the screen when one is clicked.
                    for speed in speeds:
                        if not speed.clicked(position):
                            continue
                        frame_speed = speed.frame_speed
                        speed.button_activated = True
                        for s in speeds:
                            if(s!=speed):
                                s.button_activated=False
                    # Playing the animation preview by setting the boolean to True
                    if play.clicked(position):
                        play.button_activated = True
        else:
            # Setting the color of the color picker to the color that was picked and closing it when it is done.
            if event.type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED:
                is_picker_opened = False
                drawing_col = event.colour
                color_picker.color = event.colour
            if event.type == pygame_gui.UI_WINDOW_CLOSE:
                is_picker_opened = False
    # Checking if the user has cancelled the drawing. If so, it will remove the last drawing from the
    # list of drawings and update the grid with the previous drawing.
    if cancelled:
        if(len(states_of_drawing)>0):
            save_frame(WINDOW,current_frame_index,unique_id)
            grid = states_of_drawing[-1]
            animation_list[current_frame_index] = grid
            del states_of_drawing[-1]
        create_all(WINDOW,grid,is_picker_opened,visible)
    # Checking if the user has added a new frame. If so, the screen is updated and booleans back to False.
    elif add_frame.add:
        create_all(WINDOW,new_frame,is_picker_opened,visible)
        grid = new_frame
        add_frame.add = False
        add_frame.button_activated = False
    # Checking if the user has copied a frame. If so, the screen is updated and booleans back to False.
    elif copy_frame.copy:
        create_all(WINDOW,new_frame,is_picker_opened,visible)
        grid = new_frame
        copy_frame.copy = False
        copy_frame.button_activated = False
    # Checking if the user has removed a frame. 
    elif remove_frame.delete :
        create_all(WINDOW,grid,is_picker_opened,visible)
        remove_frame.button_activated = False
    # Checking if the "play" button has been activated. If it has been activated, it is iterating through
    # the drawings of animation list and does not display the layer (visible) during the preview if it was activated. 
    # It waits for a certain amount of time which is equal to the frame speed before moving on to the
    # next frame. During this event, the user can't interact with the interface. Once all frames have been saved, 
    # it sets the visibility of the animation to True if was previously activated and allows mouse button events again.
    elif play.button_activated:
        for drawing in animation_list:
            frame_number = 1
            if visible:
                was_visible = True
                visible = False
                layer.button_activated = False
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
            grid = drawing
            create_all(WINDOW,grid,is_picker_opened,visible)
            save_frame(WINDOW,frame_number,unique_id)
            pygame.time.wait(frame_speed)
            frame_number += 1
        grid = animation_list[current_frame_index]
        play.button_activated = False
        pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
        if was_visible:
            visible = True
            layer.button_activated = True

    # Creating a window and then creating a grid : continuously updated.
    else :
        create_all(WINDOW,grid,is_picker_opened,visible)
    cancelled = False
    previous_frame.button_activated = False
    next_frame.button_activated = False
pygame.quit()
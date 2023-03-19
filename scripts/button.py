from .settings import *

# The Button class is an abstract class that creates a button object that can be used to create a button on the
# StickyNote interface.
class Button :
    def __init__(self,x,y,width,height,color,border_color=LGREY,text=None,text_color=LGREY,icon=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.border_color = border_color
        self.text = text
        self.text_color = text_color
        self.icon = icon
        self.button_activated = False
    
    def draw(self,win):
        """
        This method draws the button on the interface. It draws a rectangle, a border around the rectangle, 
        an icon if an image is given, as well as text. If the button is clicked, it is to be redrawn to give
        feedback to the user. Thus, give_feeback is called.
        
        :param win: The window to draw the button on
        """
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
        pygame.draw.rect(win,self.border_color,(self.x,self.y,self.width,self.height), 2)
        if self.icon:
            win.blit(self.icon,(self.x,self.y))
        if self.text:
            button_font = get_font(22)
            text_surface = button_font.render(self.text, 1 , self.text_color)
            win.blit(text_surface,(self.x + self.width/2 - text_surface.get_width()/2,
                                    self.y + self.height/2 - text_surface.get_height()/2))
        self.give_feedback()

    def clicked(self, position):
        """
        If the position is within the bounds of the button, return True, otherwise return False.
        
        :param position: The position of the mouse click
        :return: a boolean value.
        """
        x, y = position 
        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y > self.y and y <= self.y + self.height):
            return False
        return True
    
    def give_feedback(self):
        """
        In order to give some feedback to the user, if the button is clicked (activated), 
        the border color becomes orange. Otherwise, it is light grey.
        """
        if(self.button_activated):
            self.border_color = ORANGE
        else:
            self.border_color = LGREY

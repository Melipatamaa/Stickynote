from .settings import *

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
        x, y = position 
        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y > self.y and y <= self.y + self.height):
            return False
        return True
    
    def give_feedback(self):
        if(self.button_activated):
            self.border_color = ORANGE
        else:
            self.border_color = LGREY

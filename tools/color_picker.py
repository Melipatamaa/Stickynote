from .settings import *
from .button import *

class ColorPicker(Button) :
    def __init__(self,x,y,width,height,color,text=None,text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color  
        self.text = text
        self.text_color = text_color

    def set_color(self,screen):
        surf = pygame.Surface((1,2))
        surf.fill((255,255,255))
        surf.set_at((0,1),(0,0,0))
        surf = pygame.transform.smoothscale(surf,screen.get_size())

        surf2 = pygame.Surface((2,1))
        surf2.fill((255,255,255))
        surf2.set_at((1,0),(255,0,0))
        surf2 = pygame.transform.smoothscale(surf2,screen.get_size())
        surf.blit(surf2,(0,0),special_flags=pygame.BLEND_MULT)

        screen.blit(surf, (0,0))
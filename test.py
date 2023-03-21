import pygame
from scripts.settings import *

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

using =  True
clock = pygame.time.Clock()

a = 20

while using:
    time_delta = clock.tick(FPS)/1000
    for event in pygame.event.get():
        pygame.draw.rect(WINDOW,WHITE,(0,0,WIDTH,BORDERS_COLS))
        pygame.draw.rect(WINDOW,WHITE,(0,0,BORDERS_ROWS,HEIGHT))
        pygame.draw.rect(WINDOW,WHITE,(0,HEIGHT-BORDERS_COLS,WIDTH,BORDERS_COLS))
        pygame.draw.rect(WINDOW,WHITE,(WIDTH-BORDERS_ROWS,0,BORDERS_ROWS,HEIGHT))

        pygame.draw.rect(WINDOW,ORANGE,(0,0,WIDTH,HEIGHT), 20)

        pygame.draw.rect(WINDOW,ORANGE,(a,a,a,a))
        pygame.draw.rect(WINDOW,ORANGE,(a+a,a,a,a))
        pygame.draw.rect(WINDOW,ORANGE,(a,a+a,a,a))

        pygame.draw.rect(WINDOW,ORANGE,(a,HEIGHT-2*a,a,a))
        pygame.draw.rect(WINDOW,ORANGE,(a+a,HEIGHT-2*a,a,a))
        pygame.draw.rect(WINDOW,ORANGE,(a,HEIGHT-3*a,a,a))

        pygame.draw.rect(WINDOW,ORANGE,(WIDTH-2*a,a,a,a))
        pygame.draw.rect(WINDOW,ORANGE,(WIDTH-2*a,a+a,a,a))
        pygame.draw.rect(WINDOW,ORANGE,(WIDTH-3*a,a,a,a))

        pygame.draw.rect(WINDOW,ORANGE,(WIDTH-2*a,HEIGHT-2*a,a,a))
        pygame.draw.rect(WINDOW,ORANGE,(WIDTH-2*a,HEIGHT-3*a,a,a))
        pygame.draw.rect(WINDOW,ORANGE,(WIDTH-3*a,HEIGHT-2*a,a,a))

        pygame.draw.rect(WINDOW,ORANGE,(BORDERS_ROWS,BORDERS_COLS,CANVAS_WIDTH,CANVAS_HEIGHT), 10)

        pygame.display.flip()
        if event.type == pygame.QUIT:
            using = False
pygame.quit()
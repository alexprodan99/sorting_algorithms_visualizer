import sys
import pygame
from pygame.locals import *
from colors import *

FPS = 60
WIDTH, HEIGHT = 640, 480
UNIT = .5
to_sort = [100,241,123,124,345,416, 500, 600, 10]
size = len(to_sort)


def draw_rect(surface, color, x, y, width, height):
    pygame.draw.rect(surface, color, pygame.Rect(x, y, width, height))

def draw_text(surface, text, font_name, font_size, x, y, text_color, background_color):
    font = pygame.font.Font(font_name, font_size)
    text = font.render(text, True, text_color, background_color)
    surface.blit(text, (x,y))

def draw(screen):
    screen.fill(BLACK)
    
    
    for i in range(size):
        x = 50 * i
        width = 30
        height = to_sort[i] * UNIT
        y = 400 - height
        draw_rect(screen, RED, x, y, width, height)
        draw_text(screen, str(to_sort[i]), 'freesansbold.ttf', 16, x, 400, GREEN, BLUE)
    
    pygame.display.flip()
    
    



def update(dt):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # pygame.display.update()



def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    fps_clock = pygame.time.Clock()
    pygame.display.set_caption('Sorting Algorithms Visualizer')


    dt = 1 / FPS
    
    while True:
        draw(screen)
        update(dt)
        dt = fps_clock.tick(FPS)

if __name__ == '__main__':
    main()
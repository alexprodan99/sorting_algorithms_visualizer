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

def highlight_element(screen, arr, index ):
    x = 50 * index
    width = 30
    height = arr[index] * UNIT
    y = 400 - height
    draw_rect(screen, BLUE, x, y, width, height)
    draw_text(screen, str(arr[index]), 'freesansbold.ttf', 16, x, 400, GREEN, BLUE)

def unhighlight_element(screen, arr, index):
    x = 50 * index
    width = 30
    height = arr[index] * UNIT
    y = 400 - height
    draw_rect(screen, RED, x, y, width, height)
    draw_text(screen, str(arr[index]), 'freesansbold.ttf', 16, x, 400, GREEN, BLUE)

def draw_array(screen, arr):
    screen.fill(BLACK)
    size = len(arr)
    for i in range(size):
        x = 50 * i
        width = 30
        height = arr[i] * UNIT
        y = 400 - height
        draw_rect(screen, RED, x, y, width, height)
        draw_text(screen, str(arr[i]), 'freesansbold.ttf', 16, x, 400, GREEN, BLUE)

        
def bubble_sort(screen, arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            highlight_element(screen, arr, j)
            pygame.display.flip()
            pygame.time.delay(1000)
            highlight_element(screen, arr, j+1)
            pygame.display.flip()
            pygame.time.delay(1000)
            unhighlight_element(screen, arr, j)
            pygame.display.flip()
            pygame.time.delay(1000)
            unhighlight_element(screen, arr, j+1)
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)
            draw_array(screen, arr)
            pygame.display.flip()
            pygame.time.delay(2000)


def draw(screen):
    screen.fill(BLACK)
    draw_array(screen, to_sort)
    pygame.display.flip()
    pygame.time.delay(2000)
    bubble_sort(screen, to_sort)
    



def update(dt):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()



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
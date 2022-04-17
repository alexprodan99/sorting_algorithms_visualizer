import sys
import argparse
import pygame
from pygame.locals import *
from algorithms import *
from data import *

FPS = 60
WIDTH, HEIGHT = 640, 480
args = {}

def draw(screen):
    global args
    screen.fill(BLACK)
    draw_array(screen, to_sort)
    pygame.display.flip()
    pygame.time.delay(2000)
    if 'algorithm' in args:
        eval(args['algorithm'])(screen, to_sort)

def update(dt):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


class ValidateAlgorithm(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values not in ['bubble_sort', 'insertion_sort', 'selection_sort', 'quick_sort']:
            parser.error(f"Please enter a valid algorithm. Got: {values}")
        setattr(namespace, self.dest, values)

def main():
    global args
    parser = argparse.ArgumentParser(description="Welcome to sorting algorithms visualizer. Please specify your sorting algorithm(bubble_sort/insertion_sort).")
    parser.add_argument('-a', '--algorithm', help="Sorting algorithm that will be used in demo.", required=True, action=ValidateAlgorithm)
    args = vars(parser.parse_args())
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
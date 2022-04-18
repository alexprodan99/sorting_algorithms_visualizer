import argparse
from ast import arg
import pygame
import sys
import threading
from pygame.locals import *
from algorithms import *
from data import *

FPS = 60
WIDTH, HEIGHT = 640, 480
args = {}
stop = False

def draw(screen):
    global args
    global stop
    screen.fill(BLACK)
    draw_array(screen, to_sort)
    pygame.display.flip()
    pygame.time.delay(2000)
    if 'algorithm' in args and not stop:
        stop = eval(args['algorithm'])(screen, to_sort)

def update(dt):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('QUIT')
            pygame.quit()
            sys.exit()
    pygame.display.update()


class ValidateAlgorithm(argparse.Action):
    algorithms = ['bubble_sort', 'insertion_sort', 'selection_sort', 'quick_sort']
    def __call__(self, parser, namespace, values, option_string=None):
        if values not in ValidateAlgorithm.algorithms:
            parser.error(f"Please enter a valid algorithm.({'/'.join(ValidateAlgorithm.algorithms)}) Got: {values}")
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
    draw_thread = threading.Thread(target=draw, args=(screen,))
    draw_thread.daemon = True
    draw_thread.start()
    while True:
        update(dt)
        dt = fps_clock.tick(FPS)

if __name__ == '__main__':
    main()
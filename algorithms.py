import pygame
from pygame.locals import *
from colors import *
from data import *
UNIT = .5

def flip_and_delay(delay):
    pygame.display.flip()
    pygame.time.delay(delay)

def draw_rect(surface, color, x, y, width, height):
    pygame.draw.rect(surface, color, pygame.Rect(x, y, width, height))

def draw_text(surface, text, font_name, font_size, x, y, text_color, background_color):
    font = pygame.font.Font(font_name, font_size)
    text = font.render(text, True, text_color, background_color)
    surface.blit(text, (x,y))

def draw_explanation(screen, explanation):
    draw_text(screen, explanation, 'freesansbold.ttf', 16, 25, 25, GREEN, BLUE)
    flip_and_delay(1500)

def highlight_element(screen, arr, index ):
    x = 50 * index
    width = 30
    height = arr[index] * UNIT
    y = 400 - height
    draw_rect(screen, BLUE, x, y, width, height)
    draw_text(screen, str(arr[index]), 'freesansbold.ttf', 16, x, 400, GREEN, BLUE)
    flip_and_delay(1500)

def unhighlight_element(screen, arr, index):
    x = 50 * index
    width = 30
    height = arr[index] * UNIT
    y = 400 - height
    draw_rect(screen, RED, x, y, width, height)
    draw_text(screen, str(arr[index]), 'freesansbold.ttf', 16, x, 400, GREEN, BLUE)
    flip_and_delay(1500)

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
            draw_explanation(screen, f'compare {arr[j]} and {arr[j+1]}')
            highlight_element(screen, arr, j)
            highlight_element(screen, arr, j+1)
            unhighlight_element(screen, arr, j)
            unhighlight_element(screen, arr, j+1)
            
            if arr[j] > arr[j + 1] :
                draw_explanation(screen, f'swap {arr[j]} and {arr[j+1]}')
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                draw_explanation(screen, f'not swap {arr[j]} and {arr[j+1]}')
            draw_array(screen, arr)
            

def insertion_sort(screen, arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        draw_explanation(screen, f'select {arr[i]} as key and compare it with {arr[i-1]}')
        highlight_element(screen, arr, i)
        
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        highlight_element(screen, arr, j)
        unhighlight_element(screen, arr, i)
        unhighlight_element(screen, arr, j)
        
        draw_array(screen, arr)
        while j >=0 and key < arr[j]:
            draw_explanation(screen, f'{key} < {arr[j]}')
            highlight_element(screen, arr, j)
            arr[j+1] = arr[j]
            j -= 1
            unhighlight_element(screen, arr, j)
        arr[j+1] = key
        draw_explanation(screen, f'put key {key} at index {j+1}')
        draw_array(screen, arr)
        

def selection_sort(screen, arr):
    for i in range(len(arr)):
        draw_explanation(screen, f'consider min_idx as {i}')
        highlight_element(screen, arr, i)
        unhighlight_element(screen, arr, i)
        
        min_idx = i
        for j in range(i+1, len(arr)):
            draw_explanation(screen, f'compare {arr[min_idx]} with {arr[j]}')
            highlight_element(screen, arr, min_idx)
            highlight_element(screen, arr, j)
            unhighlight_element(screen, arr, min_idx)
            unhighlight_element(screen, arr, j)
            
            if arr[min_idx] > arr[j]:
                draw_explanation(screen, f'change min_idx to {j}')
                min_idx = j
        draw_explanation(screen, f'swap {arr[i]} with {arr[min_idx]}')
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_array(screen, arr)
        
def partition(screen, arr, low, high):
    i = low - 1
    pivot = arr[high]
    draw_explanation(screen, f'choose pivot {pivot}')
    highlight_element(screen, arr, high)
    unhighlight_element(screen, arr, high)

    for j in range(low, high):
        draw_explanation(screen, f'compare {arr[j]} and {pivot}')
        highlight_element(screen, arr, j)
        highlight_element(screen, arr, high)
        unhighlight_element(screen, arr, j)
        unhighlight_element(screen, arr, high)
        if arr[j] <= pivot:
            i = i + 1
            draw_array(screen, arr)
            draw_explanation(screen, f'swap {arr[i]} and {arr[j]}')
            highlight_element(screen, arr, i)
            highlight_element(screen, arr, j)
            unhighlight_element(screen, arr, i)
            unhighlight_element(screen, arr, j)
            arr[i], arr[j] = arr[j], arr[i]
            draw_array(screen, arr)

    draw_explanation(screen, f'swap {arr[i+1]} and {arr[high]}')
    highlight_element(screen, arr, i+1)
    highlight_element(screen, arr, high)
    unhighlight_element(screen, arr, i+1)
    unhighlight_element(screen, arr, high)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    draw_array(screen, arr)
    return i + 1


def quicksort_util(screen, arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(screen, arr, low, high)
        
        quicksort_util(screen, arr, low, pi - 1)
        quicksort_util(screen, arr, pi + 1, high)


def quick_sort(screen, arr):
    low = 0
    high = len(arr) - 1
    quicksort_util(screen, arr, low, high)


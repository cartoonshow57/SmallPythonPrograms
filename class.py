# Creating a basic Snake Game
import pygame


# Drawing the Grid
from pygame.examples.video import *


def drawGrid(w, rows, surface):
    sizeBetween = width // rows
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBetween
        y = y + sizeBetween

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

# The Redraw Function

def redrawWindow(surface):
     global rows, width
     win.fill((0, 0, 0))
     drawGrid(width, rows, surface)
     pygame.display.update()


# The main Window

def snake():
    pass


def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))

    clock = pygame.time.clock()

    while(1):
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)
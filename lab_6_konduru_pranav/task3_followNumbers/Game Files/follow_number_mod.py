#import imp
#from tkinter import screen
from random import randint
from tkinter import N
from tracemalloc import stop
from unicodedata import numeric
#import pygame
import pgzrun
#from PIL import Image
from pgzero.builtins import Actor
WIDTH = 600
HEIGHT = 600

dots = []
lines = []
next_dot = 0
number_of_dots = 15     # Starts off with 15 dots
initial_number_of_dots = number_of_dots
def intialization():
    for dot in range(0,number_of_dots):            # Add more dots by changing range
        actor = Actor("dot")
        actor.pos = randint(20, WIDTH - 20), \
        randint(20, HEIGHT - 20)
        dots.append(actor)
def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), \
        (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number = number + 1
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))
def on_mouse_down(pos):
    global next_dot
    global lines
    #print(next_dot)
    #print(number_of_dots)
    if dots[next_dot].collidepoint(pos):
        #print("Ouch")
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot = next_dot + 1
    else:                       # Ends program when mistake is done
        lines = []          
        next_dot = 0
        print("Game Over")
        exit()
        
#def next_level
intialization()
pgzrun.go()
#from argparse import Action
from random import randint
#from sys import displayhook
#from tkinter import CENTER
#from turtle import screensize
import pgzrun 

#Define size of game window
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

#Contains list of dance moves
move_list = []
display_list = []

#Assigned integers needed for the game
score = 0
current_move = 0
count = 4
dance_length = 4

#Keep track of what's happening in game
say_dance = False
show_countdown = True
moves_complete = False
game_over = False

#Adding Actors

#Make dancers appear in starting position when game starts
dancer = Actor("dancer-start")
dancer.pos = CENTER_X + 5, CENTER_Y - 40

#Arrange the color squares
up = Actor("up")
up.pos = CENTER_X, CENTER_Y + 110
right = Actor("right")
right.pos = CENTER_X + 60, CENTER_Y + 170
down = Actor("down")
down.pos = CENTER_X, CENTER_Y + 230
left = Actor("left")
left.pos = CENTER_X - 60, CENTER_Y + 170

#Drawing the actors

def draw():
    global game_over, score, say_dance
    global count, show_countdown
    #When game is running
    if not game_over:
        screen.clear()
        screen.blit("stage", (0, 0))
        dancer.draw()
        up.draw()
        right.draw()
        left.draw()
        screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

        return

pgzrun.go()
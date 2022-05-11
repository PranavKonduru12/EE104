#from argparse import Action
from dis import dis
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

#Musical Statues

#Reset Actors
def reset_dancer():
    global game_over
    if not game_over:
        dancer.image = "dancer-start"
        up.image = "up"
        right.image = "right"
        down.image = "down"
        left.image = "left"
    return
#Moving dancer
def update_dancer(move):
    global game_over # Tells compiler which variable to use
    if not game_over:
        # Value tells the dancer which dance move to do
        if move == 0:
            up.image = "up-lit" # Highlights colored square 
            dancer.image = "dancer-up" 
            # Hold the move for half second before reset_dancer()
            clock.schedule(reset_dancer, 0.5)
        elif move == 1:
            right.image = "right-lit" 
            dancer.image = "dancer-right" 
            clock.schedule(reset_dancer, 0.5)
        elif move == 2:
            down.image = "down-lit" 
            dancer.image = "dancer-down" 
            clock.schedule(reset_dancer, 0.5)
        else:
            left.image = "left-lit" 
            dancer.image = "dancer-left" 
            clock.schedule(reset_dancer, 0.5)
    return
#Displays steps
def display_moves():
    global move_list, display_list, dance_length
    global say_dance, show_countdown, current_move
    #Checks if the list of dance moves has something in it
    if display_list:
        #Stores the first move in display_list
        this_move = display_list[0]
        #Removes the first item from display_list
        # so that the second item will be in position 0
        display_list = display_list[1:]
        if this_move == 0:
            #Value of this_move is 0, so it is passed 
            #on to this function
            update_dancer(0)
            clock.schedule(display_moves, 1) 
        elif this_move == 1:
            update_dancer(1)
            clock.schedule(display_moves, 1) 
        elif this_move == 2:
            update_dancer(2)
            #Schedules a call to the function 
            #display_moves() in one second
            clock.schedule(display_moves, 1) 
        else:
            update_dancer(3)
            clock.schedule(display_moves, 1) 
    else:
        say_dance = True
        show_countdown = False
    return
def generate_moves():
    pass
def countdown():
    pass
def next_move():
    pass
#Key interaction with dancer
def on_key_up(key):
    global score, game_over, move_list, current_move
    if key == keys.UP:
        update_dancer(0)
    elif key == keys.RIGHT:
        update_dancer(1)
    elif key == keys.DOWN:
        update_dancer(2)
    elif key == keys.LEFT:
        #When arrow key is pressed, update_dancer calls
        #parameter to make the dancer perform relevant moves
        update_dancer(3)
    return
def update():
    pass

#Random Numbers

pgzrun.go()
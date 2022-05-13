#from argparse import Action
# from dis import dis
# from http.client import MULTI_STATUS
from random import randint
# from shutil import move
# from tkinter import Toplevel, font
# from turtle import Turtle, screensize
#from sys import displayhook
#from tkinter import CENTER
#from turtle import screensize
import pygame
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
rounds = 0

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
        down.draw()
        right.draw()
        left.draw()
        screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

        if say_dance:
            #Will display the "Dance!" in black
            screen.draw.text("Dance!", color="black",    
                topleft=(CENTER_X - 65, 150), fontsize=60)
        if show_countdown:
            #Display current value of count in black
            screen.draw.text(str(count), color="black",
                topleft = (CENTER_X - 8, 150), fontsize=60)
    #Game over
    else:
        screen.clear()
        screen.blit("stage", (0, 0))
        screen.draw.text("Score: " + 
            str(score), color="black",
            topleft=(10, 10))  # Draws sccore in top-left column
        screen.draw.text("GAME OVER!", color="black", # Draws "GAME OVER!" in black
            topleft=(CENTER_X - 130, 220), fontsize=60)
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
            #when display_list is empty
            update_dancer(3)
            clock.schedule(display_moves, 1)    #Sets global variable "show_countdown" to false
    else:
        say_dance = True #Tells darw() function to display "Dance!"   
        show_countdown = False
    return
#Generate sequence of moves 
def generate_moves():
    global move_list, dance_length, count
    global show_countdown, say_dance
    count = 4
    move_list = []
    say_dance = False
    for move in range(0, dance_length):
        #assigns values 0, 1, 2, or 3 at random variables
        rand_move = randint(0, 3)
        move_list.append(rand_move)# Appends new move to the move_list
        display_list.append(rand_move)
    show_countdown = True # Tells draw function to display value in count
    countdown()
    return
#Displys 3, 2, 1
def countdown():
    global count, game_over, show_countdown
    if count > 1:
        #Updates the value in count by subtracting 1
        count -= 1
        clock.schedule(countdown, 1)
    else:
        show_countdown = False #Removes countdown sequence
        display_moves()
    return
# Move along the list of generated moves
def next_move():
    #identifies which moves you're dealing with 
    global dance_length, current_move, moves_complete, rounds
    #True if there are still some moves to check
    if current_move < dance_length - 1:
        current_move = current_move + 1
    # Longer Dance
    # elif (rounds % 3 == 0):
    #     dance_length = dance_length + 1
    else:
        #Blocks runs if there are no more move to check
        moves_complete = True
    return
#Key interaction with dancer
def on_key_up(key):
    global score, game_over, move_list, current_move
    if key == keys.UP:
        update_dancer(0)
        #Scoring on each move
        if move_list[current_move] == 0:
            score = score + 1 #Blocks run if player presses correct key
            next_move()
        else:
            game_over = True
    elif key == keys.RIGHT:
        update_dancer(1)
        if move_list[current_move] == 1:
            score = score + 1 
            next_move()
        else:
            game_over = True
    elif key == keys.DOWN:
        update_dancer(2)
        if move_list[current_move] == 2:
            score = score + 1 
            next_move()
        else:
            game_over = True
    elif key == keys.LEFT:
        #When arrow key is pressed, update_dancer calls
        #parameter to make the dancer perform relevant moves
        update_dancer(3)
        if move_list[current_move] == 3:
            score = score + 1 
            next_move()
        else:
            game_over = True
    return
generate_moves()
music.play("vanishing-horizon") #Start music
#Make game more challenging
def update():
    global game_over, current_move, moves_complete
    if not game_over:
        # Runs if all moves are completed
        if moves_complete:
            generate_moves() # generates new series of moves
            moves_complete = False
            current_move = 0
    else:
        music.stop() # music stop once game is over

#Random Numbers

pgzrun.go()
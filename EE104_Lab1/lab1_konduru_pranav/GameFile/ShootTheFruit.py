"""
    Imports various libraries with different functions and features used to make and run games
    similar to Shoot the Fruit from the interface to the mechanics
"""
import pgzrun
import pygame 
import pgzero 
#Reminder: pip install pgzero
from pgzero.builtins import Actor # From the library pgzero.builitins, only the Actor class is imported
from random import randint # From the random library, only the randint function/functions is imported 
from PIL import Image # Importing the functions/features used for image manipulation/resizinng from PIL library

# To resize the images 
#image = Image.open("/Users/pranavkonduru/Local_GIt_Repos/EE104/EE104_Lab1/GameFile/Images/transparent_pineapple.png") # Image object creation using local image file
#image = image.resize((250,250),Image.ANTIALIAS) # Resizing image 
#image.save(fp="/Users/pranavkonduru/Local_GIt_Repos/EE104/EE104_Lab1/GameFile/Images/new_pineapple.png") # Save resized image locally with new name

# Required to add the images into the game
apple = Actor("apple") # Defining actor apple using the Actor class
orange = Actor("orange") # Defining actor orange usingn the Actor class
pineapple = Actor("new_pineapple") # Defining actor pineapple usingn the Actor class

Hit=0 # Defining and initializing int Hit 
Miss=0 # Defining and initializing int Miss 

# Sets up the internface with the fruits and score 
def draw():
    screen.clear()
    apple.draw()
    orange.draw()
    pineapple.draw()
    # initial location of the Hit/Miss score were set to (10,10); Changed it to the top right 
    screen.draw.text("Hit: " +str(Hit) +"Miss: " +str(Miss), color="white", topleft=(690,10))

# Displays apple actor with random position range
def place_apple():
    apple.x = randint(50,800) #changing x value
    apple.y = randint(10,600)

# Displays orange actor with random position range
def place_orange():
    orange.x = randint(40,800)
    orange.y = randint(50,600)

# Displays pineapple actor with random position range
def place_pineapple():
    pineapple.x = randint(80,800)
    pineapple.y = randint(100,600)    
    

# Pointer and score counting mechanic 
def on_mouse_down(pos):
    global Hit
    global Miss
    # If actor apple is clicked, then the Hit counter gets incremented
    if apple.collidepoint(pos):
        #print("Good shot!")
        place_apple()
        Hit=Hit+1

    # If anything else is clicked, then the Miss counter gets incremented 
    else:
        #print("Missed!")
        Miss=Miss+1
        if randint(1,10)%2 :
            place_orange()
        else:
            place_pineapple()


pgzrun.go() # Execution happens while using all the defined functions above

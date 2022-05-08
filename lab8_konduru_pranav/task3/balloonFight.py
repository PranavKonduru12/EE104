from argparse import Action
from random import randint

#Screen size
WIDTH = 800
HEIGHT = 600

#Setting up balloon
balloon = Actor("balloon")
balloon.pos = 400, 300

#Obstacles
bird = Actor("bird-up")
bird.pos = randint(800, 1600), randint(10, 200) #Birds appear at random positions of x

house = Actor("house")      #Creates new actor using image of house
house.pos = randint(800, 1600), 460

tree = Actor("tree")
tree.pos = randint(800, 1600), 450

#Create global variables
bird_up = True  #Keep track of images used for bird actor
up = False      
game_over = False   
score = 0   #Keeps track of the player's score
number_of_updates = 0   #Keeps track of how many times game has updated 

scores = []     #Stores the top three high scores

#Manage high scores
def update_high_scores():
    pass

def display_high_scores():
    pass

#Draw function
def draw():
    
    #Adds background image of sky, clouds, and grass
    screen.blit("background", (0, 0))

    #Draw Actors on screen if game is not over
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text("Score: "+ str(score), (700, 5), color="black")
    else:
        #Show high score
        display_high_scores()
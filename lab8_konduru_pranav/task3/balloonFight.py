#from argparse import Actor
import pgzrun
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
    global score, scores

    filename = r"/Users/pranavkonduru/Local_GIt_Repos/EE104_Projects/lab8_konduru_pranav/task3/high-scores.txt"

    scores = []
    #Get current high score
    with open(filename, "r") as file:
        #global score, scores
        line = file.readline()
        high_scores = line.split()
        #Find highest score
        for high_score in high_scores:
            #Check if player's score is higher than existing score
            if(score > int(high_score)):
                scores.append(str(score) + " ")
                #Set score to the high score
                score = int(high_score)
            #Player hasn't beaten high score, then current high score is added to list
            else:
                scores.append(str(high_score) + " ")
    #Opens the high-scores text file to be written
    with open(filename, "w") as file:
        #writes new high scores to the .txt file
        for high_score in scores:
            file.write(high_score)

def display_high_scores():
    #Writes high score
    screen.draw.text("HIGH SCORES", (350, 150), color="black")
    y = 175 # Sets the first high score's position on the y-axis
    position = 1
    for high_score in scores:
        screen.draw.text(str(position) + ". " + high_score, (350, y), color="black")
        y += 25
        position += 1

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

#Mouse click reaction
def on_mouse_down():
    global up
    up = True
    balloon.y -= 50

def on_mouse_up():
    global up
    up = False

#Make bird flap
def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up = True

#Update function
def update():
    #Declacres that the variables in function should change
    global game_over, score, number_of_updates
    #Add gravity
    if not game_over:
        if not up:
            balloon.y += 1
        #Move bird
        if bird.x > 0:
            bird.x -= 7 #Speed it up
            #Make the bird flap wings every tenth time 
            #function is called
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        #Handling bird offscreen
        else:
            bird.x = randint(800, 1600) #Places bird at 
            bird.y = randint(10, 200)      #position off right screen
            score += 1  #Adds 1 to score for every obstacle that disapperas                      
            number_of_updates = 0
    
        #Move the house
        if house.right > 0:
            house.x -= 2
        else:
            #Line places at a random positon on right edge if house disappears to left edge
            house.x = randint(800, 1600)
            #Line will update score by one if house moves off screen
            score += 1
    
        #Move the tree
        if tree.right > 0:
            tree.x -= 2
        else:
            tree.x = randint(800, 1600)
            score += 1
    
        #Keeping baloon steady
        if balloon.top < 0 or balloon.bottom > 560:
            game_over = True
            update_high_scores()
    
    #Handle collision with obstacles
    #Checks to see if baloon hit three or more obstacles
    if balloon.collidepoint(bird.x, bird.y) or balloon.collidepoint(house.x, house.y) or balloon.collidepoint(tree.x, tree.y):
        game_over = True # Ends game
        update_high_scores()  #Updates high score

pgzrun.go() # For running game
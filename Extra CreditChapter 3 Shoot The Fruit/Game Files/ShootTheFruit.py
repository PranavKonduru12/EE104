#pip install pgzrun
#pip install pygame
#pip install pgzero
#import pgzrun
import pygame
import pgzero #Reminder: pip install pgzero
from pgzero.builtins import Actor
from random import randint

apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")
car = Actor("car32x32")
car2 = Actor("car32x32")

Hit=0
Miss=0

def draw():
    screen.clear()
    apple.draw()
    orange.draw()
    pineapple.draw()
    car.draw() # draw the car
    car2.draw()
    screen.draw.text("Hit: " +str(Hit) +"Miss: " +str(Miss), color="white", topleft=(10,10))


def place_apple():
    apple.x = randint(10,800)
    apple.y = randint(10,600)


def place_orange():
    orange.x = randint(40,800)
    orange.y = randint(50,600)


def place_pineapple():
    pineapple.x = randint(80,800)
    pineapple.y = randint(100,600)


def place_car():
    car.x = randint(400,800)
    car.y = randint(400,600)

def place_car2():
    car2.x = randint(400,700)
    car2.y = randint(300,400)

# place_apple()


def on_mouse_down(pos):
    global Hit
    global Miss
    if apple.collidepoint(pos):
        #print("Good shot!")
        place_apple()
        Hit=Hit+1

    else:
        #print("Missed!")
        Miss=Miss+1
        if randint(1,10)%2 :
            place_orange()
        elif randint(3,21)%3 :
           place_car()
        elif randint(3,200)%5 :
           place_car2()
        else:
            place_pineapple()


pgzrun.go()
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
bird.pos = randint(800, 1600), randint(10, 200)

house = Actor("house")      # Creates new actor using image of house
house.pos = randint(800, 1600), 460

tree = Actor("tree")
tree.pos = randint(800, 1600), 450
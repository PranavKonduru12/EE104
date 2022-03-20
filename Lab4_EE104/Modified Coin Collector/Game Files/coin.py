# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 15:50:09 2022

@author: chris.pham
"""

import pgzrun
import pygame
import pgzero
from pgzero.builtins import Actor
from random import randint

#Introducing the Actors
fox = Actor("hedgehog") # Changed actor to hedgehog
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

WIDTH = 600 # Changed area of the field
HEIGHT = 400

score = 0
game_over = False


#Time to draw
def draw():
    screen.fill("blue")       # Change color
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10), fontsize=60)
    if game_over:
        screen.fill("pink")
        screen.draw("Final Score: " + str(score), topleft=(10,10), fontsize=60)


def place_coin():
    coin.x = randint(20, (WIDTH-20))
    coin.y = randint(20, (HEIGHT-20))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    
    if keyboard.left:
        fox.x = fox.x - 4 # Change speed 
    elif keyboard.right:
        fox.x = fox.x + 4
    elif keyboard.up:
        fox.y = fox.y - 4
    elif keyboard.down:
        fox.y = fox.y + 4
        
    coin_collected = fox.colliderect(coin)
    
    if coin_collected:
        score = score + 10
        place_coin()
    
clock.schedule(time_up, 700.0)
place_coin()    
     


#Run it
pgzrun.go()
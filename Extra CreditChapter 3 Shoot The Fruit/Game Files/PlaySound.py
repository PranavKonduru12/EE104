# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 23:17:36 2022

@author: chris.pham
"""

import pgzrun
import keyboard, time

music.play("vanishing-horizon")

print("Enter \"s\" key to stop the music")

while (True):
    if keyboard.is_pressed('s'):
        break

music.stop()

# Use this website to convert any audio file format to ogg audio format https://convertio.co/mp3-ogg/

# Use this website for instructions to download any files you want https://superuser.com/questions/1224917/download-a-google-translate-pronunciation

# For example, download the sound file apple from https://dictionary.cambridge.org/us/pronunciation/english/apple

music.play("ukappen014")

print("Enter \"a\" key to stop the sound")

while (True):
    if keyboard.is_pressed('a'):
        break

music.stop()
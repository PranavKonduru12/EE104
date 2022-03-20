from time import sleep
from pynq import Overlay
overlay = Overlay("base.bit")

from pynq.overlays.base import BaseOverlay
base_overlay = BaseOverlay("base.bit")

help(base_overlay)
help(base_overlay.leds)

base_overlay.leds[0].toggle() #turn LED0 on
base_overlay.leds[0].toggle() #turn LED0 off

led0 = base_overlay.leds[0] #Corresponds to LED LD0
led1 = base_overlay.leds[1] #Corresponds to LED LD1
led2 = base_overlay.leds[2] #Corresponds to LED LD2
led3 = base_overlay.leds[3] #Corresponds to LED LD3

#note: switches only accounts for SW0 and SW1
sw0 = base_overlay.switches[0] #Corresponds to SW0
sw1 = base_overlay.switches[1] #Corresponds to SW1

#note: with buttons, we can access BUTTONS0-3
button0 = base_overlay.buttons[0] #Corresponds to BUTTON2
button1 = base_overlay.buttons[1] #Corresponds to BUTTON2
button2 = base_overlay.buttons[2] #Corresponds to BUTTON2
button3 = base_overlay.buttons[3] #Corresponds to BUTTON2

if (sw0.read() == False):   # Reads SW0 and check if it toggled
    led0.on()              # IF SW0 is ON --> Turn on LED0
    led1.on()              # IF SW0 is ON --> Turn on LED1

led0.off()             # ELSE Turn off LED0
led1.off()             # ELSE Turn off LED1

if (button0.read() == False):   # Reads SW0 and check if it toggled
    led2.off()              # IF SW0 is ON --> Turn on LED0
    led3.off()              # IF SW0 is ON --> Turn on LED1

if (button3.read() == False):  # All the code below after adding while(True) will run forever
    if (sw0.read() == False):   # Reads SW0 and check if it toggled
        led0.on()              # IF SW0 is ON --> Turn on LED0
        led1.on()              # IF SW0 is ON --> Turn on LED1
    else:
        led0.off()             # ELSE Turn off LED0
        led1.off()             # ELSE Turn off LED1
    
    if (sw1.read() == False):   # Reads SW1 and check if it toggled
        led2.on()              # IF SW1 is ON --> Turn on LED2
        led3.on()              # IF SW1 is ON --> Turn on LED3
    else:
        led2.off()             # ELSE Turn off LED2
        led3.off()             # ELSE Turn off LED3

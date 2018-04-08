# Written by Tariq A.
# Repositoy git://www.github.com/tariq-chameleon/asvs.git
# Randomize the colors and levels of the Pixel strip

 


import RPi.GPIO as gpio
from time import sleep
import sys as SYS
from led_pixel_controller import PaintPixel
from led_pixel_controller import InitPixels
import re
import random as R

PERIOD = 0.3
        
def randomize():             # Initialize by pin number (arg)


    PixelColor = [R.randint(0,255),R.randint(0,255),R.randint(0,255)]
    PaintPixel(R.randint(0, 11),PixelColor,R.randint(0, 100))



InitPixels()

    # Simple socket implementation (not recommended)
while True:
    randomize()
    sleep(PERIOD)
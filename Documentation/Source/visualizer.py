#Written by Tariq A.
#Repositoy git://www.github.com/tariq-chameleon/asvs.git
#This .py file has function(s) to help visualize a certain frequency on a certain GPIO

 


import RPi.GPIO as gpio
from time import sleep
import sys as SYS
from led_pixel_controller import PaintPixel
from led_pixel_controller import InitPixels
import re
import random

FREQ_DOMAIN_NUM_RANGES = 10

high_max = 100
high_min = 0
low_min = 0  
low_max = 20
  
           # start duty cycle 0 (off)  

Period = 0.05 # File reading period


def Convert_Range (arg):
    
    arg= int(arg)

    out = ( (arg - low_min) / (low_max - low_min) ) * (high_max - high_min) + high_min

    return int(out)


def FrequencyToColor(FreqPixel):

    GRB_Lvls = [0,0,0]

    if FreqPixel == 0:          #f0
        GRB_Lvls = [0,0,255] 
        return GRB_Lvls
    elif FreqPixel == 1:        #f1
        GRB_Lvls = [0,0,255]
        return GRB_Lvls    
    elif FreqPixel == 2:        #f2
        GRB_Lvls = [0,255,0]
        return GRB_Lvls    
    elif FreqPixel == 3:        #f3
        GRB_Lvls = [0,255,0]
        return GRB_Lvls    
    elif FreqPixel == 4:        #f4
        GRB_Lvls = [0,255,0]
        return GRB_Lvls    
    elif FreqPixel == 5:        #f5
        GRB_Lvls = [0,255,0]
        return GRB_Lvls    
    elif FreqPixel == 6:        #f6
        GRB_Lvls = [255,0,0]
        return GRB_Lvls    
    elif FreqPixel == 7:        #f7
        GRB_Lvls = [255,0,0]
        return GRB_Lvls    
    elif FreqPixel == 8:        #f8
        GRB_Lvls = [255,0,255]
        return GRB_Lvls    
    elif FreqPixel == 9:        #f9
        GRB_Lvls = [255,0,255]
        return GRB_Lvls
        
    else:
        return GRB_Lvls
        
def visualize(FreqPXL,FreqLvl):             # Initialize by pin number (arg)

   
    
    FreqLvl = Convert_Range(FreqLvl)
    PaintPixel(int(FreqPXL),FrequencyToColor(int(FreqPXL)),int(FreqLvl))



InitPixels()



    # Simple socket implementation (not recommended)
while True:
    try:

        # Get Frequency level from "fake" socket file
        with open('socket') as socket:
            FreqLvls = socket.read().split(',')
        print (FreqLvls)

        #visualizer frequencies
        for j in range (FREQ_DOMAIN_NUM_RANGES):
            
            visualize(int(j),int(FreqLvls[j])) # Enable to work with play.py
            

        sleep(Period)
        #visualize(int(CMD[0]),int(CMD[1]))    # debug

    except ValueError:
        continue
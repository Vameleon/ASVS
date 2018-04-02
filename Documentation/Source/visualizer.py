#Written by Tariq A.
#Repositoy git://www.github.com/tariq-chameleon/asvs.git
#This .py file has function(s) to help visualize a certain frequency on a certain GPIO

 


import RPi.GPIO as gpio
from time import sleep
import sys as SYS
  

  
           # start duty cycle 0 (off)  

Period = 0.015
DutyCycleMax = 30               # high duty cycle
DutyCycleMin = 0                # lowest duty cycle
DutyCycleIncrement = 1          # Increment per loop
DutyCycleDecrement = 1 * -1     # decrement per loop


def visualize(arg):             # Initialize by pin number (arg)
    gpio.setmode(gpio.BCM)      # choose BCM  
    gpio.setup(arg, gpio.OUT)   # set gpio as output   
    LED = gpio.PWM(arg, 100)    # create object at 100 Hertz  
    LED.start(0)   
#try:  
    #while True:  
    #for i in range(DutyCycleMin,DutyCycleMax+1,DutyCycleIncrement):      # +1  
    #    LED.ChangeDutyCycle(i)  
    #    sleep(Period)  
    for i in range(DutyCycleMax,DutyCycleMin-1,DutyCycleDecrement):      # from 100 to zero in steps of -1  
        LED.ChangeDutyCycle(i)  
        sleep(Period)  
#except KeyboardInterrupt:  
    LED.stop()                  # stop the LED PWM output  
    gpio.cleanup()              # clean up gpio on CTRL+C exit  


#visualize(int(SYS.argv[1]))    # debug

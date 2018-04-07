#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

#Modified by Tariq A.
#github.com/tariq-chameleon/asvs
#Thanks to https://tutorials-raspberrypi.com/ for inspiring me to use the Neopixel library





import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 12      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
OUTPUT_DELAY   = 5


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)



# Conver power level to brightness level in GRB
# Power level should be in range 0-100 %
def AbsPowerToBrightness (power_lvl,input_vector):
    output_vector = [0,0,0]
    output_vector[0] = int(input_vector[0]*((power_lvl)/100))  # R
    output_vector[1] = int(input_vector[1]*((power_lvl)/100))  # G
    output_vector[2] = int(input_vector[2]*((power_lvl)/100))  # B
    # print (output_vector)
    return output_vector

# Frequency Index (Pixel nr,), Color GRB vector and power percentage
def PaintPixel (FreqIdx,FreqColor,PowerPer):
    
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called1 once before other functions).
    strip.begin()
    #colorWipe(strip, Color(0,0,0), 10) # wipe
    LVLVector = AbsPowerToBrightness(PowerPer,[FreqColor[0],FreqColor[1],FreqColor[2]]) 
    strip.setPixelColor(FreqIdx,Color(LVLVector[0],LVLVector[1],LVLVector[2]))
    strip.show()
    # time.sleep(OUTPUT_DELAY/1000.0)





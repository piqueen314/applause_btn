#!/usr/bin/python3
#btntest.py
import time
import os
import RPi.GPIO as GPIO
from pygame import mixer

# Pins definitions
btn_pin = 12
led_pin = 32


# Set up pins
def gpio_setup():
 #Setup the wiring
 GPIO.setmode(GPIO.BOARD)
 #Setup Ports
 GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 GPIO.setup(led_pin, GPIO.OUT)

def main():
 gpio_setup()
 count=0
 btn_closed = True
 #GPIO.output(led_pin, GPIO.LOW)

 # Initialize pygame mixer
 mixer.init()

 # Load the sounds
 sound = mixer.Sound('applause-1.wav')

 while True:
     btn_val = GPIO.input(btn_pin)
     if btn_val and btn_closed:
         print("OPEN")
         btn_closed = False
     elif btn_val == False and btn_closed == False:
         count += 1
         print("CLOSE %s" % count)
         os.system("flite -t '%s'" % count)
         if mixer.get_busy():
             sound.stop()
             GPIO.output(led_pin, GPIO.LOW)
         else:
             GPIO.output(led_pin, GPIO.HIGH)
             sound.play()
         btn_closed = True
     time.sleep(0.1)
     # Only turn off LED if sound has stopped playing
     if not mixer.get_busy():
         GPIO.output(led_pin, GPIO.LOW)

try:
    main()
finally:
    GPIO.cleanup()
    print("Closed Everything. END")
    # End
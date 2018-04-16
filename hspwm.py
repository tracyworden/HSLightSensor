#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#Change this value to change the when the LED light comes on and goes off

#define the pins for the LEDs 
led1 = 7

#initiale the Pulse-Width Modulation
pwm1 = GPIO.PWM(led1,100)


def initializePin(pin):

    #Output on the pin for 
    GPIO.setup(pin, GPIO.OUT) 
    GPIO.output(pin, GPIO.LOW)
 

#Catch when script is interrupted, clean up correctly
try:
    # Main loop
    print('Starting')
    initializePin(led1)
    print('Pin Initialized')

    i = 0
    pwm1.start(i)
    while True:
        for i in range(0, 101, 5):
            pwm1.ChangeDutyCycle(i)
            time.sleep(.02)
            print(i)
        for i in range(95, 0, -5):
            pwm1.ChangeDutyCycle(i)
            time.sleep(.02)
            print(i)
            
except KeyboardInterrupt:
    pass
finally:
    pwm1.stop()
    GPIO.cleanup()

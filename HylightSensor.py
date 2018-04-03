#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

__author__ = 'Tracy adapted from Gus (Adapted from Adafruit)'
__license__ = "GPL"
__maintainer__ = "pimylifeup.com"

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the photo sensor circuit we are using pin 7
pin_to_circuit = 7
#define the pin that goes to the led circuit we are using pin 16
pin_to_led = 16
#Change this value to change the when the LED light comes on and goes off 
LedTime = 200

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT) 
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#this turns on / off the LED
def ToggleLed (pin_to_led,toggle):

    GPIO.setup(pin_to_led,GPIO.OUT)
    if (toggle):
      print("LED on")
      GPIO.output(pin_to_led,GPIO.HIGH)
      time.sleep(1)
    else:
      print("LED off")
      GPIO.output(pin_to_led,GPIO.LOW)

#Catch when script is interrupted, clean up correctly
try:
    # Main loop
    print('Starting')
    rcTime = 0
    
    while True:
        rcTime=rc_time(pin_to_circuit)
        print('Time = {}'.format(rcTime))
        if rcTime > LedTime:
            ToggleLed(pin_to_led,True)
        else:
            ToggleLed(pin_to_led,False)
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

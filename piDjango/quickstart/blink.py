# Test program to ensure your GPIO is correct. 
import RPi.GPIO as GPIO
import time
def blinkTest(pin, blinks, timeBetween):
    pause = float(timeBetween)
    numBlinks = int(blinks)
    pin = int(pin)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    for i in range(numBlinks):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(pause)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(pause)
        
    GPIO.cleanup()
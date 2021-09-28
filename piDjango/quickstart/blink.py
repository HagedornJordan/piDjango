# Test program to ensure your GPIO is correct. 
import RPi.GPIO as GPIO
import time
def blinkTest(blinks, timeBetween):
    pause = float(timeBetween)
    numBlinks = int(blinks)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(23, GPIO.OUT)
    for i in range(numBlinks):
        GPIO.output(23, GPIO.HIGH)
        time.sleep(pause)
        GPIO.output(23, GPIO.LOW)
        time.sleep(pause)
        
    GPIO.cleanup()
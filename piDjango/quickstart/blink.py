# Test program to ensure your GPIO is correct. 
import RPi.GPIO as GPIO
import time
sleepTime = .25
blinks = 10
def blinkTest():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(23, GPIO.OUT)
    for i in range(blinks):
        GPIO.output(23, GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(23, GPIO.LOW)
        time.sleep(sleepTime)
        
    GPIO.cleanup()

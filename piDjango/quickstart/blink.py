# Test program to ensure your GPIO is correct. 
import RPi.GPIO as GPIO
import time

def blinkTest():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, GPIO.HIGH)
    time.sleep(20)
    GPIO.output(23, GPIO.LOW)
    GPIO.cleanup()

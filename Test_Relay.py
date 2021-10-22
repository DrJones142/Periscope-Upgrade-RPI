import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

try:
    while True:
        GPIO.output(36, 1)
        GPIO.output(37, 1)
        sleep(1)
        GPIO.output(36, 0)
        GPIO.output(37, 0)
        sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup();

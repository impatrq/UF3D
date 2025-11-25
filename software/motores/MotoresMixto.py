import RPi.GPIO as GPIO
import time

pinStep_M1 = 12
pinStep_M2 = 13
pinDirection = 17

stepsPerRevolution = 200
stepDelay = 0.005

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinStep_M1, GPIO.OUT)
GPIO.setup(pinStep_M2, GPIO.OUT)
GPIO.setup(pinDirection, GPIO.OUT)


if __name__ == '__main__':
    try:
        GPIO.output(pinDirection, GPIO.HIGH)

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
        
        while True:
            print("Iniciando una vuelta completa (200 pasos)...")
            
            for step_count in range(stepsPerRevolution):
                GPIO.output(pinStep_M1, GPIO.HIGH)
                GPIO.output(pinStep_M2, GPIO.HIGH)
                time.sleep(stepDelay)
                
                GPIO.output(pinStep_M1, GPIO.LOW)
                GPIO.output(pinStep_M2, GPIO.LOW)
                time.sleep(stepDelay) 
                
            print("Vuelta completada. Pausa de 1 segundo.")
            time.sleep(1)

    except KeyboardInterrupt:
        pass 

    finally:
        GPIO.cleanup()
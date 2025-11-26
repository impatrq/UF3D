from machine import Pin, UART 
import utime as time 
import sys 


UART_TX_PIN = 0 
UART_RX_PIN = 1 
LIDAR_BAUDRATE = 115200 
LIDAR_STABILIZATION_MS = 500 
CMD_MEASURE_DISTANCE = b'\x55\xAA\x81\x00\xFA' 
RESPONSE_LEN = 8 

uart = UART(0, baudrate=LIDAR_BAUDRATE, tx=Pin(UART_TX_PIN), rx=Pin(UART_RX_PIN)) 


 
DIR_PIN = 17 
STEP_PIN = 18 
STEPS_PER_REV = 200 
STEP_DELAY = 0.001 

 
STEPS_PER_SAMPLE = 10  
TOTAL_SAMPLES = int(STEPS_PER_REV / STEPS_PER_SAMPLE) 

dir_pin = Pin(DIR_PIN, Pin.OUT) 
step_pin = Pin(STEP_PIN, Pin.OUT) 


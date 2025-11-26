from machine import Pin, UART 
import utime as time 
import sys 


UART_TX_PIN = 0 
UART_RX_PIN = 1 
LIDAR_BAUDRATE = 115200 
LIDAR_STABILIZATION_MS = 500 
CMD_MEASURE_DISTANCE = b'\x55\xAA\x81\x00\xFA' 
RESPONSE_LEN = 8 

import machine
import time
import json
import uos
from machine import UART, Pin
import sys

PIN_STEP_X = 18
PIN_DIR_X = 17

PINS_STEP_Y = [19, 3]
PINS_DIR_Y = [20, 2]

step_x = machine.Pin(PIN_STEP_X, machine.Pin.OUT)
dir_x = machine.Pin(PIN_DIR_X, machine.Pin.OUT)

steps_y = [machine.Pin(p, machine.Pin.OUT) for p in PINS_STEP_Y]
dirs_y = [machine.Pin(p, machine.Pin.OUT) for p in PINS_DIR_Y]

uart = machine.UART(0, baudrate=115200, rx=machine.Pin(1), tx=machine.Pin(0)) 

DELAY_PULSO_US = 500  
DIR_DERECHA = 1
DIR_IZQUIERDA = 0
DIR_ADELANTE = 1



def set_direccion(pines_dir, direccion):
    """Establece la dirección para uno o varios pines."""
    val = 0 if direccion else 1
    if isinstance(pines_dir, list):
        for pin in pines_dir:
            pin.value(val)
    else:
        pines_dir.value(val)

def toggle_step(pines_step):
    """Genera un flanco de subida y bajada en los pines STEP."""
    # High
    if isinstance(pines_step, list):
        for pin in pines_step: pin.value(1)
    else:
        pines_step.value(1)
    
    time.sleep_us(DELAY_PULSO_US)
    
    # Low
    if isinstance(pines_step, list):
        for pin in pines_step: pin.value(0)
    else:
        pines_step.value(0)
        
    time.sleep_us(DELAY_PULSO_US)

def generar_pulsos(pines_step, pines_dir, direccion, duracion_segundos):
    """
    Abstrae el movimiento generando pulsos durante un tiempo determinado.
    Maneja tanto motores simples (X) como dobles (Y).
    """
    set_direccion(pines_dir, direccion)
    
    start = time.ticks_ms()
    
    while time.ticks_diff(time.ticks_ms(), start) < (duracion_segundos * 1000):
        toggle_step(pines_step)

def obtener_lectura_lidar():
    HEADER_1 = 0x55 
    HEADER_2 = 0xAA
    FOOTER   = 0xFA
    RESPONSE_LEN = 8 
    CMD_MEASURE_DISTANCE = b'\x55\xAA\x81\x00\xFA' 

    LIDAR_STABILIZATION_MS = 200
    RETRY_DELAY_MS = 25
    
    """
    Bucle infinito hasta obtener una lectura válida.
    Basado en la lógica robusta de 'request-response'.
    """
    total_attempts = 0
    sys.stdout.write("   [LIDAR] Buscando dato válido...\n")
    
    
    if uart.any():
        uart.read()
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

while True: 
        total_attempts += 1
        
       
        uart.write(CMD_MEASURE_DISTANCE)
        
        
        time.sleep_ms(LIDAR_STABILIZATION_MS)
        
        count = uart.any()
        
        
        if count >= RESPONSE_LEN:
            recv = uart.read(RESPONSE_LEN)
            
            
            if (recv and len(recv) == RESPONSE_LEN and 
                recv[0] == HEADER_1 and 
                recv[1] == HEADER_2 and 
                recv[7] == FOOTER): 
                
                
                distance = (recv[4] * 256) + recv[5]
                if distance > 0:
                    sys.stdout.write('   [Dato ÚNICO] -> Distancia: %5d mm. Total intentos: %d\n' % 
                                     (distance, total_attempts))
                    
                    
                    if uart.any(): uart.read()
                    
                    
                    return distance, total_attempts
        
        
        if uart.any():
            uart.read()
            
        
        if total_attempts % 10 == 0:
            sys.stdout.write('   [ATTEMPT %d] -> FALLO. Reintentando...\n' % total_attempts)
            
        time.sleep_ms(RETRY_DELAY_MS)

def guardar_dato(x, y, z):
    """Guarda la tupla en el archivo JSONL (JSON Lines)."""
    linea = json.dumps({"x": x, "y": y, "z": z}) + "\n"
    try:
        
        with open('scan_data.json', 'a') as f:
            f.write(linea)
            f.flush() 
            uos.sync() 
    except OSError as e:
        print(f"Error escribiendo archivo: {e}")

def limpiar_archivo():
    print(f"--- Limpiando archivo ---")
    with open('scan_data.json', 'w') as f:
        pass 
    print("Archivo listo.")

def main():
    limpiar_archivo() 
    print("Iniciando Escáner 3D...")
    
    coord_y = 0
    
    
    while True:
        print(f"--- Iniciando Fila en Y={coord_y} ---")
        
        coord_x = 0
        tiempo_fila_inicio = time.time()
        movimientos_realizados = 0 
        
        
        while (time.time() - tiempo_fila_inicio) < 120:
            
            
            z, intentos = obtener_lectura_lidar()
            
            
            print(f"Guardando: X={coord_x}, Y={coord_y}, Z={z}")
            guardar_dato(coord_x, coord_y, z)
            
            
            generar_pulsos(step_x, dir_x, DIR_DERECHA, duracion_segundos=1.0)
            
           
            coord_x += 5
            movimientos_realizados += 1
            
        
        print("Fin de tiempo de fila. Retornando carro X...") 
        tiempo_retorno = movimientos_realizados * 1.0
        generar_pulsos(step_x, dir_x, DIR_IZQUIERDA, duracion_segundos=tiempo_retorno)
        
        
        coord_x = 0
        
        
        print(f"Avanzando eje Y...")
        
        generar_pulsos(steps_y, dirs_y, DIR_ADELANTE, duracion_segundos=2.0)

        coord_y += 10 
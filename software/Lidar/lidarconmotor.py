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


def take_step(): 
    step_pin.value(1) 
    time.sleep(STEP_DELAY) 
    step_pin.value(0) 
    time.sleep(STEP_DELAY) 


def get_lidar_distance(): 
    uart.write(CMD_MEASURE_DISTANCE) 
    time.sleep_ms(LIDAR_STABILIZATION_MS)  

    count = uart.any() 
    if count >= RESPONSE_LEN: 
        recv = uart.read(RESPONSE_LEN) 
         
        if recv[0] == 0x55 and recv[1] == 0xAA and recv[7] == 0xFA:  
             
            distance = (recv[4] * 256) + recv[5] 
            status_code = recv[6] 
             
            if status_code == 0x00: 
                return distance, status_code 
            else: 
                return -1, status_code 
        else: 
            return -2, None 
    return -3, None 


def main_scan(total_samples): 
    sys.stdout.write("Iniciando escaneo: %d muestras en 360 grados.\n" % total_samples) 
     
    dir_pin.value(1) 
     
    current_step = 0 

    for sample in range(total_samples): 
         
         
        for _ in range(STEPS_PER_SAMPLE): 
            take_step() 
            current_step += 1 
         
      
        distance, status = get_lidar_distance() 
         
       
        if distance > 0: 
            angle = (current_step / STEPS_PER_REV) * 360  
            sys.stdout.write('Muestra %2d | Angulo %.1f° | Distancia: %5d mm | Status: 0x%X\n' %  
                             (sample, angle, distance, status)) 
        else: 
             sys.stdout.write('Muestra %2d | Error de lectura: %d\n' % (sample, distance)) 


if __name__ == '__main__': 
    try: 
   
        main_scan(TOTAL_SAMPLES) 
        sys.stdout.write("Escaneo completado.\n") 
    except KeyboardInterrupt: 
        sys.stdout.write("Escaneo detenido por el usuario.\n")
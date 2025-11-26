import serial.tools.list_ports
import time
import numpy as np
import serial
import struct

ports = serial.tools.list_ports.comports()
for p in ports:
    print(p.device)
print(len(ports), 'ports found')

ser = serial.Serial()
ser.port = '/dev/ttyS0'
ser.baudrate = 115200

cmd = bytes.fromhex('55 AA 81 00 FA')

def getLidarData():

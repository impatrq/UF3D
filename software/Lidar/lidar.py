import serial.tools.list_ports
import time
import numpy as np
import serial
import struct

ports = serial.tools.list_ports.comports()
for p in ports:
    print(p.device)
print(len(ports), 'ports found')

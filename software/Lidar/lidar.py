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
    while True:
        ser.write(cmd)
        count = ser.in_waiting

        if count > 7:
            recv = ser.read(8)
            ser.reset_input_buffer()
            if recv[0] == 0x55 and recv[1] == 0xAA and recv[7] == 0xFA:
                
                distance = struct.unpack('>H', recv[4:6])[0] 
                
                print('distance = %5d mm' % (distance))
                ser.reset_input_buffer()
                time.sleep(0.1)
        else:
            time.sleep(0.1)

if _name_ == '_main_':
	try:
		if ser.is_open == False:
			try:
				ser.open()
			except:
				print('Open COM failed!')
		getLidarData()
	except KeyboardInterrupt:
		if ser != None:
			ser.close()
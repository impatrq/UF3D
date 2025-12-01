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


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
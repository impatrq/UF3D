import machine
import time
import json
import uos
from machine import UART, Pin
import sys

PIN_STEP_X = 18
PIN_DIR_X = 17
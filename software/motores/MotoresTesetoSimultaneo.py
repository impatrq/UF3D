from machine import Pin
import time
import sys

STEP_PIN_1 = 13 
DIR_PIN_1 = 12

STEP_PIN_2 = 3
DIR_PIN_2 = 2

STEP_PIN_3 = 19
DIR_PIN_3 = 18

def set_directions(dir1, dir2, dir3):
    dir_pin_1.value(dir1)
    dir_pin_2.value(dir2)
    dir_pin_3.value(dir3)
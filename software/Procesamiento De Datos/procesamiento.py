import json
import numpy as np
from stl import mesh
from scipy.spatial import Delaunay

INPUT_FILE = './matenme/scan_data.json'
OUTPUT_FILE = 'modelo_escaneado.stl'

def crear_stl():
    print("1. Leyendo archivo de puntos...")
    x_list = []
    y_list = []
    z_list = []

    try:
        with open(INPUT_FILE, 'r') as f:
            for linea in f:
                try:
                    data = json.loads(linea)
                    x_list.append(data['x'])
                   y_list.append(data['y'])
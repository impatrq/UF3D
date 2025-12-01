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
                    z_list.append(data['z'])
                except ValueError:
                    continue 
        except FileNotFoundError:
            print(f"Error: No encuentro el archivo {INPUT_FILE}")
        return
    x = np.array(x_list)
    y = np.array(y_list)
    z = np.array(z_list)

    points_2d = np.vstack([x, y]).T

    print(f"2. Generando malla con {len(x)} puntos...")

    tri = Delaunay(points_2d)
    num_triangles = len(tri.simplices)
    scan_mesh = mesh.Mesh(np.zeros(num_triangles, dtype=mesh.Mesh.dtype))

    for i, f in enumerate(tri.simplices):
        for j in range(3):


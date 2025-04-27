import cv2
import numpy as np
import glob

# Cargar imagen desde la Kinect (simulada por ahora con una imagen normal)
imagen = cv2.imread("Escaner3D/imagenes/pies")

if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Suavizar imagen para reducir ruido
suavizada = cv2.GaussianBlur(gris, (5, 5), 0)

# Aplicar umbralización (binarización)
_, umbral = cv2.threshold(suavizada, 100, 255, cv2.THRESH_BINARY_INV)

# Encontrar contornos
contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar contornos en una imagen nueva (solo para ver el resultado)
imagen_contornos = np.zeros_like(imagen)
cv2.drawContours(imagen_contornos, contornos, -1, (255, 255, 255), 2)

# Guardar la imagen con contornos
cv2.imwrite("procesado/contornos_pie.png", imagen_contornos)

# Calcular medidas aproximadas (asumiendo 1 píxel = 1 mm, ajustar según la Kinect)
if contornos:
    c = max(contornos, key=cv2.contourArea)  # Tomar el contorno más grande (el pie)
    x, y, w, h = cv2.boundingRect(c)
    largo_mm = h  # Largo del pie
    ancho_mm = w  # Ancho del pie
else:
    largo_mm = ancho_mm = 0

# Guardar las medidas en un archivo JSON
import json

datos = {"largo_mm": largo_mm, "ancho_mm": ancho_mm}
with open("procesado/medidas_pie.json", "w") as f:
    json.dump(datos, f)

print("Procesamiento completo. Datos guardados.")

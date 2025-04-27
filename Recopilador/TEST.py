import cv2
import numpy as np
import json

def estimate_depth(x, y, foot_center, max_depth=5):
    """
    Estima la profundidad Z basada en la distancia al centro del pie.
    """
    distance = np.linalg.norm(np.array([x, y]) - np.array(foot_center))
    normalized_depth = max_depth * (1 - (distance / max_distance))
    return max(0, normalized_depth)

def process_foot_image(image_path, output_json="foot_measurements.json"):
    # Cargar la imagen
    image = cv2.imread(image_path)
    if image is None:
        print("Error: No se pudo cargar la imagen.")
        return
    
    # Convertir a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplicar desenfoque para reducir ruido
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Umbralización adaptativa para mayor precisión
    _, thresh = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY_INV)
    
    # Encontrar contornos con jerarquía para diferenciar internos y externos
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours or hierarchy is None:
        print("No se encontraron contornos.")
        return
    
    # Filtrar solo los contornos internos (los que tienen un contorno padre)
    internal_contours = [contours[i] for i in range(len(contours)) if hierarchy[0][i][3] != -1]
    
    if not internal_contours:
        print("No se encontraron contornos internos.")
        return
    
    # Calcular centro del pie (aproximado con el centroide del contorno más grande)
    largest_contour = max(internal_contours, key=cv2.contourArea)
    M = cv2.moments(largest_contour)
    if M["m00"] != 0:
        foot_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    else:
        foot_center = (0, 0)
    
    # Calcular distancia máxima al centro
    global max_distance
    max_distance = max(np.linalg.norm(np.array(pt[0]) - np.array(foot_center)) for pt in largest_contour)
    
    # Extraer todos los contornos internos con sus puntos y estimar Z
    all_contours = []
    all_inner_points = []
    
    for contour in internal_contours:
        contour_points = [(int(point[0][0]), int(point[0][1]), estimate_depth(point[0][0], point[0][1], foot_center)) for point in contour]
        all_contours.append(contour_points)
        
        # Crear una máscara del tamaño de la imagen para identificar puntos internos
        mask = np.zeros_like(gray, dtype=np.uint8)
        cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)
        
        # Obtener las coordenadas de todos los puntos dentro del contorno
        inner_points = np.column_stack(np.where(mask == 255))
        inner_points = [(int(p[1]), int(p[0]), estimate_depth(p[1], p[0], foot_center)) for p in inner_points]  # Convertir a formato (x, y, z)
        all_inner_points.append(inner_points)
    
    # Datos a exportar
    data = {
        "contornos_internos": all_contours,  # Lista de listas de puntos (x, y, z) para cada contorno interno
        "puntos_internos": all_inner_points  # Lista de todos los puntos internos de cada contorno con Z estimado
    }
    
    # Guardar en un archivo JSON
    with open(output_json, "w") as f:
        json.dump(data, f, indent=4)
    
    # Mostrar resultados
    output_image = image.copy()
    cv2.drawContours(output_image, internal_contours, -1, (0, 255, 0), 2)
    
    # Marcar los puntos internos en la imagen
    for inner_points in all_inner_points:
        for x, y, _ in inner_points:
            cv2.circle(output_image, (x, y), 1, (255, 0, 0), -1)  # Azul para puntos internos
    
    cv2.imshow("Internal Foot Contours and Points", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    print(f"Datos guardados en {output_json}")

# Ejemplo de uso
process_foot_image("pie.jpg")

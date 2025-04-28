import numpy as np
import open3d as o3d
import trimesh
from scipy.interpolate import Rbf

# Parámetros globales
LARGO = 260.0        # mm de largo del pie
ANCHO = 100.0        # mm de ancho del pie
BASE_THICKNESS = 5.0 # mm de grosor base interna
ROWS, COLS = 4, 4    # Matriz de sensores

def simulate_point_cloud(grid_x=50, grid_y=20,
                         largo=LARGO, ancho=ANCHO,
                         base_thickness=BASE_THICKNESS):
    """
    Genera una nube plana simulada con grosor base constante.
    Reemplazar por lectura real de scan.xyz cuando esté disponible.
    """
    x = np.linspace(0, ancho, grid_x)
    y = np.linspace(0, largo, grid_y)
    xx, yy = np.meshgrid(x, y)
    zz = np.full_like(xx, base_thickness)
    points = np.column_stack((xx.ravel(), yy.ravel(), zz.ravel()))
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    return pcd

def simulate_fsr_readings(shape=(ROWS, COLS)):
    """
    Simula lecturas crudas de FSR (valores entre 0 y 1).
    Reemplazar por np.loadtxt("fsr.csv", delimiter=",") si está disponible.
    """
    return np.random.rand(*shape)

def calibrate(raw_vals):
    """Normaliza valores brutos a rango [0–1]."""
    return raw_vals / raw_vals.max()

def build_mesh(pcd, depth=8, density_threshold=0.01):
    """
    Reconstruye un mesh Triangular desde la PointCloud usando método Poisson,
    y filtra los vértices de densidad baja.
    """
    # Asignar normales todas hacia +Z
    N = np.asarray(pcd.points).shape[0]
    normals = np.tile([0, 0, 1.0], (N, 1))
    pcd.normals = o3d.utility.Vector3dVector(normals)

    # Poisson reconstruction
    mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
        pcd, depth=depth
    )
    densities = np.asarray(densities)

    # Filtrar vértices de baja densidad
    mask = densities > np.quantile(densities, density_threshold)
    mesh = mesh.select_by_index(np.where(mask)[0])
    return mesh

def map_pressure_to_mesh(mesh, pressures,
                         largo=LARGO, ancho=ANCHO,
                         rows=ROWS, cols=COLS,
                         scale=8.0, smooth_iters=5):
    """
    Aplica relieve según presiones interpoladas:
    - pressures: ndarray shape (rows, cols), valores normalizados [0–1]
    - scale: mm máximos de elevación
    - smooth_iters: iteraciones de suavizado Laplaciano
    """
    # Coordenadas XY de sensores
    dx = ancho / (cols - 1)
    dy = largo / (rows - 1)
    sensor_coords = np.array([(j*dx, i*dy)
                              for i in range(rows)
                              for j in range(cols)])

    # Vértices actuales
    verts = np.asarray(mesh.vertices)
    verts_xy = verts[:, :2]

    # Interpolación RBF
    xs, ys = sensor_coords[:,0], sensor_coords[:,1]
    ps = pressures.flatten()
    rbf = Rbf(xs, ys, ps, function='thin_plate', smooth=0.1)

    # Presión en cada vértice
    p_vert = rbf(verts_xy[:,0], verts_xy[:,1])

    # Aplica relieve
    verts[:, 2] += scale * p_vert
    mesh.vertices = o3d.utility.Vector3dVector(verts)

    # Suavizado Laplaciano
    mesh = mesh.filter_smooth_laplacian(number_of_iterations=smooth_iters)
    return mesh

def export_stl(mesh, filename="plantilla_optima.stl"):
    """
    Exporta el mesh a STL usando trimesh.
    """
    verts = np.asarray(mesh.vertices)
    faces = np.asarray(mesh.triangles)
    tri = trimesh.Trimesh(vertices=verts, faces=faces)
    tri.export(filename)
    print(f"STL exportado a {filename}")

def evaluate_mesh(mesh, pressures,
                  base_thickness=BASE_THICKNESS,
                  alpha=1.0, beta=0.1, max_height=15.0):
    """
    Calcula el coste de la malla:
    - R: suma de (presión * elevación)
    - S: varianza de defectos (curvatura)
    - penalty: penalización si supera la altura máxima
    """
    # 1) Reconstruir RBF para presiones
    verts = np.asarray(mesh.vertices)
    verts_xy = verts[:, :2]

    dx = ANCHO / (COLS - 1)
    dy = LARGO / (ROWS - 1)
    sensor_coords = np.array([(j*dx, i*dy)
                              for i in range(ROWS)
                              for j in range(COLS)])
    xs, ys = sensor_coords[:,0], sensor_coords[:,1]
    ps = pressures.flatten()
    rbf = Rbf(xs, ys, ps, function='thin_plate', smooth=0.1)
    p_vert = rbf(verts_xy[:,0], verts_xy[:,1])

    # 2) Relief score R
    zs = verts[:, 2] - base_thickness
    R = np.sum(p_vert * zs)

    # 3) Smoothness score S
    tri = trimesh.Trimesh(vertices=verts, faces=np.asarray(mesh.triangles))
    defects = tri.vertex_defects    # ← sin paréntesis
    S = np.var(defects)

    # 4) Penalización por altura máxima
    penalty = max(0, zs.max() - max_height)**2

    # 5) Coste total
    return -alpha * R + beta * S + penalty


def main():
    # 1) Simular datos
    pcd = simulate_point_cloud()
    raw = simulate_fsr_readings()
    norm = calibrate(raw)

    # 2) Grid-search de parámetros
    best = None
    for scale in [5, 8, 12]:
        for iters in [3, 5, 8]:
            mesh_t = build_mesh(pcd)
            mesh_t = map_pressure_to_mesh(mesh_t, norm,
                                          scale=scale,
                                          smooth_iters=iters)
            score = evaluate_mesh(mesh_t, norm)
            if best is None or score < best[0]:
                best = (score, scale, iters)

    score, best_scale, best_iters = best
    print(f"Mejor: score={score:.2f}, scale={best_scale}, smooth_iters={best_iters}")

    # 3) Generar mesh óptimo y exportar STL
    mesh_opt = build_mesh(pcd)
    mesh_opt = map_pressure_to_mesh(mesh_opt, norm,
                                    scale=best_scale,
                                    smooth_iters=best_iters)
    export_stl(mesh_opt, "plantilla_optima.stl")

if __name__ == "__main__":
    main()


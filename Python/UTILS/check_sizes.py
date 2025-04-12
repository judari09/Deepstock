import os
import cv2

# Ruta de la carpeta que contiene las imágenes
folder_path = "db_yolo\\comb"

# Extensiones válidas para imágenes
valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

# Obtener la lista de archivos de imagen en la carpeta
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(valid_extensions)]

if not image_files:
    print("No se encontraron imágenes en la carpeta.")
    exit()

# Variable para almacenar el tamaño de referencia
reference_size = None
inconsistencies = False

# Recorrer cada imagen y verificar su tamaño
for filename in image_files:
    path = os.path.join(folder_path, filename)
    image = cv2.imread(path)
    
    if image is None:
        print(f"Error al cargar la imagen: {filename}")
        continue

    # Obtener las dimensiones: (ancho, alto)
    h, w = image.shape[:2]
    size = (w, h)

    if reference_size is None:
        reference_size = size
        print(f"Tamaño de referencia establecido en: {reference_size}")
    else:
        if size != reference_size:
            print(f"La imagen '{filename}' tiene un tamaño diferente: {size} (se esperaba {reference_size})")
            inconsistencies = True

if not inconsistencies:
    print(f"Todas las imágenes tienen el mismo tamaño: {reference_size}")
else:
    print("Se encontraron inconsistencias en el tamaño de las imágenes.")

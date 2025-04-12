import os
import cv2

# Rutas de la carpeta de entrada y salida
input_folder = "frames_videos\\frames_prueba_noche_big\\frames_cam9"
output_folder = "frames_videos\\frames_prueba_noche_big\\frames_cam9"

# Crear la carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Dimensiones a las que se desea redimensionar (ancho, alto)
new_width, new_height = 640, 360

# Iterar sobre cada archivo en la carpeta de entrada
for filename in os.listdir(input_folder):
    # Filtrar archivos por extensión (ajusta según tus necesidades)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        input_path = os.path.join(input_folder, filename)
        image = cv2.imread(input_path)
        
        if image is None:
            print(f"No se pudo cargar la imagen: {filename}")
            continue
        
        # Aplicar resize a la imagen
        resized_image = cv2.resize(image, (new_width, new_height))
        
        # Guardar la imagen redimensionada en la carpeta de salida
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, resized_image)
        print(f"Imagen '{filename}' redimensionada y guardada en: {output_path}")

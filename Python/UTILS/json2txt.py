import os
import json
import numpy as np
import glob
import cv2
from tqdm import tqdm

# Carpeta de entrada y salida
input_dir = "frames_videos\\labels_frames_prueba_noche"  # Carpeta con los archivos JSON
output_dir = "frames_videos\\labelstxt"  # Carpeta de salida para las etiquetas

os.makedirs(output_dir, exist_ok=True)

# Función para convertir coordenadas a formato YOLO
def convert_to_yolo_format(points, img_width, img_height):
    yolo_format = []
    for point in points:
        x = point[0] / img_width
        y = point[1] / img_height
        yolo_format.append(f"{x:.6f} {y:.6f}")
    return " ".join(yolo_format)

# Procesar cada archivo JSON
json_files = glob.glob(os.path.join(input_dir, "*.json"))

for json_file in tqdm(json_files, desc="Convirtiendo etiquetas"):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Obtener dimensiones de la imagen
    img_path = os.path.join(input_dir, data["imagePath"])
    if not os.path.exists(img_path):
        print(f"Imagen {img_path} no encontrada, omitiendo...")
        #continue

    #img = cv2.imread(img_path)
    img_height, img_width = 360,640#img.shape[:2]

    # Archivo de salida con el mismo nombre que la imagen pero extensión .txt
    txt_filename = os.path.splitext(os.path.basename(json_file))[0] + ".txt"
    txt_filepath = os.path.join(output_dir, txt_filename)

    with open(txt_filepath, "w") as txt_file:
        for shape in data["shapes"]:
            label = shape["label"]
            points = shape["points"]

            # Convertir los puntos al formato YOLO
            yolo_points = convert_to_yolo_format(points, img_width, img_height)

            # En YOLO, cada línea tiene el formato: <class_id> <x1> <y1> <x2> <y2> ...
            if label == "linea_delimitadora":
                class_id = 0# Ajusta esto según tu lista de clases
            elif label == "llanta":
                class_id = 1
            else:
                class_id = 2
            txt_file.write(f"{class_id} {yolo_points}\n")

print("Conversión completada. Archivos guardados en:", output_dir)

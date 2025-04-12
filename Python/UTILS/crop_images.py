import cv2
import os

# Directorio de entrada y salida
input_folder = "DB_yolo_seg\\videos_sincronizados\\prueba_5_to_crop"
output_folder = "DB_yolo_seg\\videos_sincronizados\\prueba_cropped"

# Crear el directorio de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Definir la región a recortar (x, y, w, h)
# Por ejemplo, recortar desde (50, 100) con un ancho de 200 y alto de 100 píxeles
x1,x2,y1,y2 = 176,384,50,152

# Recorrer cada imagen en el directorio de entrada
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
        img_path = os.path.join(input_folder, filename)
        # Leer la imagen
        img = cv2.imread(img_path)
        if img is None:
            print(f"No se pudo leer {img_path}")
            continue

        # Verificar que la imagen tenga el tamaño suficiente para recortar la región definida
        height, width, _ = img.shape
        if x2-x1 > width or y2-y1 > height:
            print(f"La imagen {filename} es demasiado pequeña para la región definida.")
            continue

        # Recortar la imagen
        cropped_img = img[y1:y2, x1:x2]

        # Guardar la imagen recortada
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, cropped_img)
        print(f"Imagen recortada guardada en {output_path}")

import os
import shutil
import random

def separar_datos(carpeta_origen, carpeta_train, carpeta_val, split_ratio=0.8):
    # Crear carpetas de destino si no existen
    for carpeta in [carpeta_train, carpeta_val]:
        if not os.path.exists(carpeta):
            os.makedirs(os.path.join(carpeta, "images"))
            os.makedirs(os.path.join(carpeta, "labels"))
    
    # Obtener lista de imágenes
    archivos = [f for f in os.listdir(carpeta_origen) if f.endswith(('.jpg', '.png', '.jpeg'))]
    random.shuffle(archivos)
    
    # Dividir los archivos en entrenamiento y validación
    num_train = int(len(archivos) * split_ratio)
    train_files = archivos[:num_train]
    val_files = archivos[num_train:]
    
    # Mover archivos a las carpetas correspondientes
    for archivo in train_files:
        mover_archivo(carpeta_origen, archivo, carpeta_train)
    for archivo in val_files:
        mover_archivo(carpeta_origen, archivo, carpeta_val)
    
    print(f"Datos separados: {len(train_files)} en entrenamiento, {len(val_files)} en validación")

def mover_archivo(carpeta_origen, archivo, carpeta_destino):
    nombre, _ = os.path.splitext(archivo)
    imagen_origen = os.path.join(carpeta_origen, archivo)
    label_origen = os.path.join(carpeta_origen, nombre + ".txt")
    
    shutil.copy2(imagen_origen, os.path.join(carpeta_destino, archivo))
    if os.path.exists(label_origen):
        shutil.copy2(label_origen, os.path.join(carpeta_destino, "labels", nombre + ".txt"))

# Ejemplo de uso
carpeta_origen = "DB_yolo_seg\\videos_sincronizados\\prueba_cropped"
carpeta_train = "DB_yolo_seg\\videos_sincronizados\\prueba_cropped\\train"
carpeta_val = "DB_yolo_seg\\videos_sincronizados\\prueba_cropped\\val"

# Llamar a la función para separar los datos
separar_datos(carpeta_origen, carpeta_train, carpeta_val, split_ratio=0.8)


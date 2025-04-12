import os
import shutil

def mover_imagenes_con_txt(carpeta_origen, carpeta_destino):
    # Crear la carpeta de destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
    
    # Obtener lista de archivos en la carpeta de origen
    archivos = os.listdir(carpeta_origen)
    
    # Filtrar archivos de texto
    archivos_txt = {os.path.splitext(f)[0] for f in archivos if f.endswith('.txt')}
    
    # Extensiones de imagen comunes
    extensiones_imagen = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}
    
    for archivo in archivos:
        nombre, extension = os.path.splitext(archivo)
        
        # Verificar si el archivo es una imagen y tiene un .txt correspondiente
        if extension.lower() in extensiones_imagen and nombre in archivos_txt:
            origen = os.path.join(carpeta_origen, archivo)
            destino = os.path.join(carpeta_destino, archivo)
            shutil.copy2(origen, destino)
            print(f"Movido: {archivo}")

# Ejemplo de uso
carpeta_origen = "frames_videos\\frames_prueba_noche"
carpeta_destino = "db_yolo\\new_img"
mover_imagenes_con_txt(carpeta_origen, carpeta_destino)


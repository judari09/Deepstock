import os
import glob

input_folder = "D:/YARAYOTO/Cam03/20250201"  # Carpeta con los videos
output_base_folder = "imagenes_OCR_prueba"  # Carpeta donde se guardarán los frames

# Buscar todos los archivos de video en la carpeta (puedes cambiar "*.avi" por otro formato si es necesario)
video_files = glob.glob(os.path.join(input_folder, "*.avi"))

if not video_files:
    print("⚠ No se encontraron archivos de video en la carpeta.")
else:
    for video_file in video_files:
        # Obtener el nombre base del archivo sin extensión
        video_name = os.path.splitext(os.path.basename(video_file))[0]

        # Crear una carpeta específica para los frames de cada video
        output_folder = os.path.join(output_base_folder, video_name)
        os.makedirs(output_folder, exist_ok=True)

        # Comando FFmpeg para extraer los frames
        ffmpeg_cmd = f'ffmpeg -i "{video_file}" "{output_folder}/frame_%04d.png"'
        print(f"⏳ Procesando: {video_file} → Guardando en {output_folder}")
        
        os.system(ffmpeg_cmd)

    print("✅ ¡Proceso completado! Los frames han sido guardados.")


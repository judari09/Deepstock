import os
from paddleocr import PaddleOCR

# Inicializar PaddleOCR
# Puedes ajustar 'lang' según el idioma de tus displays (ej. 'en' para inglés, 'ch' para chino, etc.)
ocr = PaddleOCR(use_angle_cls=True, lang="en",drop_confidence = 0.5)  

# Carpeta de imágenes de entrada y archivo de salida
input_folder = "DB_yolo_seg\\videos_sincronizados\\prueba_cropped\\val"
output_file = "labels_val.txt"


with open(output_file, "w", encoding="utf-8") as f:
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
            image_path = os.path.join(input_folder, filename)
            result = ocr.ocr(image_path,det=True, rec=True, cls=True, bin=True)
            
            # Inicializamos la etiqueta como "0" en caso de que no se detecte nada
            label = "    0"
            if result and result[0]:
                detected_texts = []
                for result_ocr in result[0]:
                    bbox, (texto, confidence) = result_ocr
                # Si se detectó texto, unirlo; de lo contrario, se mantiene "0"
                if texto:
                    label = f"    {texto}"
            
            f.write(f"{filename}{label}\n")
            print(f"Procesada: {filename} -> {label}")

print(f"\nArchivo de etiquetas generado: {output_file}")
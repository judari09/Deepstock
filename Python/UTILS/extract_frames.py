import cv2
import os

def extract_frames(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    frame_count = 0
    for filename in os.listdir(input_dir):
        if filename.endswith(".mp4"):
            video_path = os.path.join(input_dir, filename)
            cap = cv2.VideoCapture(video_path,cv2.CAP_ANY)
            
            if not cap.isOpened():
                print(f"Error al abrir el video: {filename}")
                continue
            
            #video_name = os.path.splitext(filename)[0]
            #frame_dir = os.path.join(output_dir, video_name)
            #os.makedirs(frame_dir, exist_ok=True)
            
        
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                """frame_copy = frame.copy()
                frame_copy2 = frame.copy()
                #division frame camara 7
                x1,x2,y1,y2 = int(frame.shape[1]/2),int(frame.shape[1]),0,int(frame.shape[0]/2)
                frame_copy = frame_copy[y1:y2,x1:x2]
                #division frame camara 9
                x1_2,x2_2,y1_2,y2_2 = 0,int(frame.shape[1]/2),int(frame.shape[0]/2),int(frame.shape[0])
                frame_copy2 = frame_copy2[y1_2:y2_2,x1_2:x2_2]"""
                if frame_count % 10 == 0:
                    frame_filename = os.path.join(output_dir,f"frame_{frame_count:04d}_display.png")
                    cv2.imwrite(frame_filename, frame)
                    #frame_count += 1 
                    #frame_filename = os.path.join(output_dir,f"frame_{frame_count:04d}.png")
                    #cv2.imwrite(frame_filename, frame_copy2)
                frame_count += 1
            
            cap.release()
            print(f"Frames extraídos de {filename}: {frame_count}")
    
    print("Proceso completado.")

# Directorios de entrada y salida (modifica según tu necesidad)
input_directory = "DB_yolo_seg\\videos_sincronizados\\prueba_5"  # Carpeta donde están los videos .avi
output_directory = "DB_yolo_seg\\videos_sincronizados\\prueba_5"  # Carpeta donde se guardarán los frames

extract_frames(input_directory, output_directory)

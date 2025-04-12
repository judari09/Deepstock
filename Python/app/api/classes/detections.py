#clase que se encargara de llamar al modelo de inteligencia artificial por yolo y devolvera el resultado
# adicionalmente hara el preprocesamiento de la imagen y el postprocesamiento de la salida del modelo
import cv2
import numpy as np
import os
from ultralytics import YOLO

class detector():
    def __init__(self, model_path: str, conf: float = 0.5):
        self.model_path = model_path
        self.conf = conf
        self.model = YOLO(model_path) # Load the YOLO model

    def detect(self, image_path: str):
        # Preprocess the image
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (640, 640))
        results = self.model(image)
        return results
    
    def postprocess(self, results):
        # Postprocess the results
        processed_results = {
            'boxes': [],
            'scores': [],
            'classes': []
        }
        for result in results:
            processed_results['boxes'].append(result.boxes.xyxy[0].cpu().numpy())
            processed_results['scores'].append(result.boxes.conf[0].cpu().numpy())
            processed_results['classes'].append(result.boxes.cls[0].cpu().numpy())
        return processed_results

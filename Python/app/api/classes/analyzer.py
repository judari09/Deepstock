import numpy as np

class analyzer():
    def __init__(self):
        self.empty_threshold = 50
        self.taken_threshold = 20
        self.is_empty = False
        self.is_taken = False
        self.y_threshold = 20

    def analyze(self, detections: dict):
        # Check if the detections are empty
        
        areas = {
            'detections': [],
            'horizontal_groups': []  # Lista de detecciones, cada una con su box y área
        }
        
        for i, box in enumerate(detections['boxes']):
            x1, y1, x2, y2 = box
            area = (x2 - x1) * (y2 - y1)
            detection = {
                'box': box,
                'area': area,
                'y1': y1,
                'class_id': detections['class_ids'][i]  # Agregamos el class_id de la detección
            }
            areas['detections'].append(detection)

        # Sort areas by x1 and y1 coordinates
        areas['detections'].sort(key=lambda x: x['y1'])

        current_group = []
        for detection in areas['detections']:
            if not current_group:
                current_group.append(detection)
            else:
                if abs(detection['y1'] - current_group[-1]['y1']) <= self.y_threshold:
                    current_group.append(detection)
                else:
                    if len(current_group) > 1:
                        areas['horizontal_groups'].append(current_group)
                    current_group = [detection]
        
        if len(current_group) > 1:
            areas['horizontal_groups'].append(current_group)

        return areas
    
    def is_taken(self, areas: dict):

        products_taken = []

        for group in areas['horizontal_groups']:
            # Ordenar el grupo por coordenada x1 para asegurar que comparamos detecciones contiguas
            group.sort(key=lambda x: x['box'][0])  # Ordenar por coordenada x1
            for area in group:
                if area['area'] < self.taken_threshold:
                    products_taken.append(area['class_id'])

        if len(products_taken) > 0:
            self.is_taken = True
        else:
            self.is_taken = False

        return self.is_taken, products_taken
    
    def is_empty(self, areas: dict):
        products_empty = []
        for group in areas['horizontal_groups']:
            group.sort(key=lambda x: x['box'][0])
            for i in range(len(group) - 1):
                if i == 1:
                    previous_center = group[i - 1]['box'][0] + group[i - 1]['box'][2] / 2
                current_center = group[i]['box'][0] + group[i]['box'][2] / 2
                next_center = group[i + 1]['box'][0] + group[i + 1]['box'][2] / 2

                if i >= 1:
                    if abs(current_center - previous_center) > self.empty_threshold:
                        if group[i]['class_id'] not in products_empty:
                            products_empty.append(group[i]['class_id'])
                    elif abs(next_center - current_center) > self.empty_threshold:
                        if group[i]['class_id'] not in products_empty:
                            products_empty.append(group[i]['class_id'])
                else:
                    if abs(next_center - current_center) > self.empty_threshold:
                        if group[i]['class_id'] not in products_empty:
                            products_empty.append(group[i]['class_id'])
        
        if len(products_empty) > 0:
            self.is_empty = True
        else:
            self.is_empty = False

        return self.is_empty, products_empty

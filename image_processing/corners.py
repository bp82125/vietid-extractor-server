from ultralytics import YOLO
import numpy as np
from image_processing.config import CORNER_MODEL, CLASS_NAMES

corner_model = YOLO(CORNER_MODEL)

def get_corner_number(yolo_res):
    corner_boxes = yolo_res[0].boxes
    return len(set(round(x.item(), 2) for x in corner_boxes.cls.cpu()))

def get_corner_points(yolo_res):
    corner_boxes = yolo_res[0].boxes
    coords = corner_boxes.xyxy
    class_ids = corner_boxes.cls

    corners_dict = {class_name: None for class_name in CLASS_NAMES}

    print(corners_dict)

    for coord, class_id in zip(coords, class_ids):
        class_id = int(class_id.item())
        if corners_dict[class_id] is None:
            x1, y1, x2, y2 = coord
            corners_dict[class_id] = [(x1.item() + x2.item()) / 2, (y1.item() + y2.item()) / 2]

    corners_dict = {CLASS_NAMES[class_id]: coord for class_id, coord in corners_dict.items()}

    return corners_dict

def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

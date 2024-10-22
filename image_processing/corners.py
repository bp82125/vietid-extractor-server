from ultralytics import YOLO
import numpy as np
import cv2
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

    for coord, class_id in zip(coords, class_ids):
        if (x1 := coord[0]) is not None and (y1 := coord[1]) is not None and (x2 := coord[2]) is not None and (y2 := coord[3]) is not None:
            class_name = CLASS_NAMES[int(class_id.item())]
            corners_dict[class_name] = [(x1.item() + x2.item()) / 2, (y1.item() + y2.item()) / 2]

    corners_dict = {key: [float(val[0]), float(val[1])] if val is not None else None for key, val in corners_dict.items()}

    return corners_dict

def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

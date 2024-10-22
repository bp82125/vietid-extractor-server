import cv2
import numpy as np

def get_bounding_box(box):
    x_coords = box[:, 0]
    y_coords = box[:, 1]
    x_min = np.min(x_coords)
    x_max = np.max(x_coords)
    y_min = np.min(y_coords)
    y_max = np.max(y_coords)
    
    return (x_min, y_min, x_max, y_max)

def merge_bounding_boxes(bounding_boxes):
    boxes = np.array(bounding_boxes)

    x_min = np.min(boxes[:, 0])
    y_min = np.min(boxes[:, 1])
    x_max = np.max(boxes[:, 2])
    y_max = np.max(boxes[:, 3])

    return (x_min, y_min, x_max, y_max)

def get_center(bounding_box):
    x_min, y_min, x_max, y_max = bounding_box
    
    x_center = (x_min + x_max) / 2
    y_center = (y_min + y_max) / 2
    
    return x_center, y_center

def draw_bounding_boxes(image, bounding_boxes, color=(0, 255, 0), thickness=2):
    output_image = image.copy()
    
    for box in bounding_boxes:
        box = np.array(box).astype(np.int32)
        cv2.polylines(output_image, [box.reshape((-1, 1, 2))], isClosed=True, color=color, thickness=thickness)

    return output_image

def extract_roi(image, bbox):
    x1, y1, x2, y2 = map(int, bbox)

    roi = image[y1:y2, x1:x2]

    return roi

def resize_image(warped, new_height):
    (h, w) = warped.shape[:2]
    aspect_ratio = w / h
    
    new_width = int(new_height * aspect_ratio)
    resized = cv2.resize(warped, (new_width, new_height))
    
    return resized
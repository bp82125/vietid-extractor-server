import cv2
import numpy as np

def draw_bounding_boxes(image, bounding_boxes, color=(0, 255, 0), thickness=2):
    output_image = image.copy()
    
    for box in bounding_boxes:
        box = np.array(box).astype(np.int32)
        cv2.polylines(output_image, [box.reshape((-1, 1, 2))], isClosed=True, color=color, thickness=thickness)

    return output_image

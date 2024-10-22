from ultralytics import YOLO

from image_processing.config import ICON_MODEL
from image_processing.utils import get_bounding_box

icon_model = YOLO(ICON_MODEL)

def filter_bboxes(img, bboxes):
    icon_results = icon_model.predict(img)
    
    icon_box = icon_results[0].boxes.xyxy.cpu().numpy().flatten()
    icon_box_ymax = icon_box[3]

    filtered_bboxes = [bbox for bbox in [get_bounding_box(box) for box in bboxes] if bbox[1] > icon_box_ymax]

    return filtered_bboxes

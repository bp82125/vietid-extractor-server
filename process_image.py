import os
import cv2

from flask import current_app

from image_processing.transform import transform_card_image
from image_processing.usage import detect_text_craft
from image_processing.processing_utils import draw_bounding_boxes

def process_image(upload_path, filename):    
    processed_filename = f"processed_{filename}"
    processed_path = os.path.join(current_app.config['UPLOAD_FOLDER'], processed_filename)

    transformed_image = transform_card_image(upload_path)

    boxes, _ = detect_text_craft(transformed_image, trained_model='./models/craft_mlt_25k.pth')
    detected_image = draw_bounding_boxes(transformed_image, boxes)

    cv2.imwrite(processed_path, detected_image)
    current_app.logger.info(f"Final processed image saved: {processed_filename}")

    return processed_filename, processed_path



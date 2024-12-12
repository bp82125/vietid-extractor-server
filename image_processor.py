from image_processing.config import CRAFT_MODEL
from image_processing.merge_boxes import merge_bboxes
from image_processing.ocr import predict_text
from image_processing.post_processing import label_text, process_text
from image_processing.transform import transform_card_image
from image_processing.text_detector import detect_text_craft
from image_processing.icon import filter_bboxes

def process_image(upload_path):
    transformed_image = transform_card_image(upload_path)
    yield "Biến đổi hình ảnh để lấy được toàn bộ CCCD"

    bboxes, _ = detect_text_craft(transformed_image, trained_model=CRAFT_MODEL)
    filtered_bboxes = filter_bboxes(transformed_image, bboxes)
    merged_bboxes = merge_bboxes(filtered_bboxes)
    yield "Phát hiện các vùng có chứa văn bản"

    raw_text = predict_text(transformed_image, merged_bboxes)
    yield "Trích xuất thông tin trong các vùng"

    processed_text = process_text(raw_text)
    yield "Xử lý dữ liệu đã trích xuất"

    yield processed_text
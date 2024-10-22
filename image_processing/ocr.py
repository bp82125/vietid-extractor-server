from PIL import Image

from vietocr.tool.config import Cfg
from vietocr.tool.predictor import Predictor

from image_processing.config import VIETOCR_MODEL
from image_processing.utils import extract_roi

config = Cfg.load_config_from_name(
    VIETOCR_MODEL
)
config["cnn"]["pretrained"] = False
config['device'] = 'cuda:0'
config["predictor"]["beamsearch"] = False
config["weights"] = "./models/vgg_transformer.pth"
detector = Predictor(config)

def process_roi(img, bbox):
    roi = extract_roi(img, bbox)
    roi_pil = Image.fromarray(roi)
    
    return roi_pil

def predict_text(img, merged_boxes):
    content_text = []
    
    for bbox in merged_boxes:
        roi = process_roi(img, bbox)
        text = detector.predict(roi)
        content_text.append(text)
    
    return content_text
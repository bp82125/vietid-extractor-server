CORNER_MODEL = "./models/corners.pt"
ICON_MODEL = "./models/icon.pt"
MASK_MODEL = "./models/mask.pt"
CRAFT_MODEL = "./models/craft_mlt_25k.pth"

VIETOCR_MODEL = "vgg_transformer"

CLASS_NAMES = {
    0: "bottom_left",
    1: "bottom_right",
    2: "top_left",
    3: "top_right"
}


SKIP_ROI_TEXT = [
    "Full name",
    "Họ và tên",
    "Place of origin",
    "Quê quán",
    "Place of residence",
    "Nơi thường trú",
]

EXTRACT_ROI_TEXT = [
    "No",
    "Date of birth",
    "Nationality",
]
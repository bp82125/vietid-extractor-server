import cv2

def resize_image(warped, new_height):
    (h, w) = warped.shape[:2]
    aspect_ratio = w / h
    
    new_width = int(new_height * aspect_ratio)
    resized = cv2.resize(warped, (new_width, new_height))
    
    return resized
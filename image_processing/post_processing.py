import re

from image_processing.config import EXTRACT_ROI_TEXT, SKIP_ROI_TEXT

def clean_string(s):
    return re.sub(r'[^\w\s,]', ' ', s)

def replace_abundant_whitespace(s):
    return re.sub(r'\s+', ' ', s).strip()

def check_text(s, text_to_check):
    for text in text_to_check:
        if text in s:
            return text
    return ""

def handle_date_of_expiry(s):
    numbers = re.findall(r'\d+', s)
    if numbers:
        return ' '.join(numbers)
    else:
        return "Không thời hạn"

def handle_id_number(s):
    return ''.join(re.findall(r'\d+', s))

def handle_sex_and_nationality(s):
    words = s.split()
    
    res = []
    for i in range(len(words) - 1):
        if words[i] == 'Sex':
            res.append(words[i + 1])
            break
    
    for i in range(len(words) - 1):
        if words[i] == 'Nationality':
            res.append(" ".join(words[i+1:]))
            break

    return res

def handle_extract_text(s, keyword):
    index = s.find(keyword)
    return s[index + len(keyword) + 1:]


def process_text(raw_text):
    cleaned_text = [replace_abundant_whitespace(clean_string(text)) for text in raw_text]
    
    processed_text = []
    for idx, text in enumerate(cleaned_text):
        if idx == len(cleaned_text) - 1:
            processed_text.extend([handle_date_of_expiry(text)])
            
        elif "Sex" in text or "Nationality" in text:
            processed_text.extend(handle_sex_and_nationality(text))
    
        elif check_text(text, SKIP_ROI_TEXT) != "":
            continue
        
        elif check_text(text, EXTRACT_ROI_TEXT) != "":
            keyword = check_text(text, EXTRACT_ROI_TEXT)
            processed_text.extend([handle_extract_text(text, keyword)])   
        else:      
            processed_text.extend([text])

    return processed_text

def label_text(content_text):    
    return {
        "no": content_text[0],
        "full_name": content_text[1],
        "date_of_birth": content_text[2],
        "sex": content_text[3],
        "nationality": content_text[4],
        "place_of_origin": content_text[5],
        "place_of_residence": ", ".join(content_text[6:8]),
        "date_of_expiry": content_text[8],
    }
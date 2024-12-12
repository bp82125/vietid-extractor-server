import os
from flask import current_app
from config import ALLOWED_EXTENSIONS

from werkzeug.utils import secure_filename

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_uploaded_file(uploaded_file, filename):
    upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    uploaded_file.save(upload_path)
    return upload_path

def handle_file_upload(request):
    if 'file' not in request.files:
        return None, "Không tồn tại file trong yêu cầu"
    
    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return None, "Bạn chưa chọn file nào"
    
    if allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)
        return uploaded_file, filename
    file_type = uploaded_file.filename.rsplit('.', 1)[-1]
    return None, f"Định dạng hình ảnh không được hỗ trợ (.{file_type})"
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
        return None, "No file part in the request"
    
    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return None, "No selected file"
    
    if allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)
        return uploaded_file, filename
    return None, "Invalid file type"
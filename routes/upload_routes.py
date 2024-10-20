from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, send_from_directory
import os

from image_processing.transform import transform_card_image

import cv2
import numpy as np

from image_processing.usage import detect_text_craft

from process_image import process_image

upload_blueprint = Blueprint('upload', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@upload_blueprint.route('/', methods=['GET'])
def index():
    processed_filename = request.args.get('processed_filename', None)
    return render_template('index.html', processed_filename=processed_filename)

@upload_blueprint.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part in the request')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No file selected')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = file.filename
        upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)

        try:
            processed_filename, _ = process_image(upload_path, filename)
                        
            flash(f'File "{filename}" successfully uploaded and processed')
            os.remove(upload_path)

            return redirect(url_for('upload.index', filename=filename, processed_filename=processed_filename))

        except Exception as e:
            flash(f'Error processing the image: {str(e)}')
            return redirect(request.url)

    flash('Allowed file types are: png, jpg, jpeg, gif')
    return redirect(request.url)

@upload_blueprint.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
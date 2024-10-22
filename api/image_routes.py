import os
import json
from flask import Blueprint, Response, current_app, jsonify, request, stream_with_context

from werkzeug.utils import secure_filename

from file_utils import handle_file_upload
from image_processor import process_image

from api_response import APIResponse

image_api_bp = Blueprint('images', __name__)

@image_api_bp.route('', methods=['POST'])
def upload_image():
    def generate_updates():
        uploaded_file, error = handle_file_upload(request)
        if not uploaded_file:
            response = APIResponse(status="error", message=f'Đã xảy ra lỗi khi upload hình ảnh: {error}')
            yield response.to_json()
            return

        upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename))
        uploaded_file.save(upload_path)
        
        response = APIResponse(status="success", message=f'Hình ảnh đã được upload thành công: {secure_filename(uploaded_file.filename)}')
        yield response.to_json()

        yield APIResponse(status="progress", message='Bắt đầu trích xuất thông tin CCCD').to_json() + "\n\n"
        
        try:
            for update in process_image(upload_path):
                if isinstance(update, str):
                    response = APIResponse(status="progress", message=update)
                else:
                    response = APIResponse(status="completed", message="Trích xuất thông tin từ CCCD thành công", data=update)
                yield response.to_json()
        except Exception as e:
            current_app.logger.error(f"Error processing image: {str(e)}")
            response = APIResponse(status="error", message='Đã xảy ra lỗi trong lúc trích xuất thông tin', data=[str(e)])
            yield response.to_json()
            
        finally:
            os.remove(upload_path)

    return Response(stream_with_context(generate_updates()), mimetype='text/event-stream')
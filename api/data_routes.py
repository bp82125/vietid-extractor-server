from flask import Blueprint, request, current_app
from api_response import APIResponse
from extensions import mongo
from datetime import datetime

data_api_bp = Blueprint('data', __name__)

@data_api_bp.route('', methods=['POST'])
def save_data():
    try:
        data = request.get_json()
        
        if not data:
            return APIResponse(status="error", message="No data provided in request").to_json(), 400
        
        data['createdAt'] = datetime.utcnow().isoformat()
        result = mongo.db.id.insert_one(data)
        created_document = mongo.db.id.find_one({"_id": result.inserted_id})
        
        created_document['_id'] = str(created_document['_id'])
        
        return APIResponse(
            status="success",
            message="Dữ liệu được lưu thành công",
            data=created_document
        ).to_json(), 201

    except Exception as e:
        current_app.logger.error(f"Error saving data to MongoDB: {str(e)}")
        return APIResponse(
            status="error",
            message="Đã xảy ra lỗi khi lưu dữ liệu",
            data=" ".join([str(e)])
        ).to_json(), 500

@data_api_bp.route('', methods=['GET'])
def get_latest_data():
    try:
        documents = mongo.db.id.find().sort('createdAt', -1).limit(3)
        
        data = []
        for doc in documents:
            doc['_id'] = str(doc['_id'])
            data.append(doc)
        
        return APIResponse(
            status="success",
            message="Thông tin các CCCD được trích xuất gần đây đã được lấy thành công",
            data=data
        ).to_json(), 200

    except Exception as e:
        current_app.logger.error(f"Error fetching latest data from MongoDB: {str(e)}")
        return APIResponse(
            status="error",
            message="Đã xảy ra lỗi khi lấy dữ liệu",
            data=[str(e)]
        ).to_json(), 500

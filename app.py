from flask import Flask, jsonify
from flask_sse import sse
from flask_cors import CORS

import os

from api.image_routes import image_api_bp

app = Flask(__name__)
app.config.from_pyfile('config.py')

app.register_blueprint(sse, url_prefix='/stream')
app.register_blueprint(image_api_bp, url_prefix=app.config['API_PREFIX'] + '/images')

CORS(app)

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404


os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)

import os

API_PREFIX = '/api/v1'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads/')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'output/')

MAX_CONTENT_LENGTH = 16 * 1024 * 1024
SECRET_KEY = 'supersecretkey'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

REDIS_URL = "redis://localhost:6379"
SSE_CHANNEL = "image-processing"

import os
from dotenv import load_dotenv

load_dotenv()

API_PREFIX = '/api/v1'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads/')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'output/')

MAX_CONTENT_LENGTH = 16 * 1024 * 1024
SECRET_KEY = 'supersecretkey'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/default')
MONGO_COLLECTION_NAME = os.getenv('MONGO_COLLECTION_NAME', 'default_collection')
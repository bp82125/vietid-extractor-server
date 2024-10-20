from flask import Flask, redirect, url_for
from routes.upload_routes import upload_blueprint
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.errorhandler(404)
def not_found_error(error):
    return redirect(url_for('upload.index'))

app.register_blueprint(upload_blueprint)

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

if __name__ == '__main__':
    app.run(debug=True)

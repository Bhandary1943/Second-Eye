# flask_server.py

from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "ESP32-CAM Upload Server is running"

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']
    filename = datetime.now().strftime("%Y%m%d_%H%M%S.jpg")
    path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(path)
    return jsonify({"message": "Image uploaded", "filename": filename}), 200

@app.route('/latest', methods=['GET'])
def latest_image():
    files = sorted(os.listdir(UPLOAD_FOLDER), reverse=True)
    if not files:
        return jsonify({"error": "No images found"}), 404
    return jsonify({"filename": files[0], "url": f"/uploads/{files[0]}"}), 200

@app.route('/uploads/<filename>')
def serve_image(filename):
    return open(os.path.join(UPLOAD_FOLDER, filename), 'rb').read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

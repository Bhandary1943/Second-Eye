# import os
# import requests

# GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
# REPO_NAME = "Bhandary1943/Second-Eye"
# FOLDER = "known_faces"

# def upload_to_github(filename, file_path):
#     with open(file_path, "rb") as f:
#         content = f.read()

#     from base64 import b64encode
#     content_base64 = b64encode(content).decode()

#     api_url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FOLDER}/{filename}"

#     headers = {
#         "Authorization": f"token {GITHUB_TOKEN}",
#         "Accept": "application/vnd.github+json"
#     }

#     data = {
#         "message": f"Add {filename}",
#         "content": content_base64
#     }

#     response = requests.put(api_url, headers=headers, json=data)
#     return response.status_code == 201


import os
import requests
from flask import Flask, request, jsonify
from base64 import b64encode

# 👇 Make sure your GitHub PAT is stored in Streamlit/Render secrets as GITHUB_TOKEN
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = "Bhandary1943/Second-Eye"
FOLDER = "known_faces"

app = Flask(__name__)  # ✅ This is what Render looks for

def upload_to_github(filename, file_path):
    with open(file_path, "rb") as f:
        content = f.read()
    content_base64 = b64encode(content).decode()

    api_url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FOLDER}/{filename}"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "message": f"Add {filename}",
        "content": content_base64
    }

    response = requests.put(api_url, headers=headers, json=data)
    return response.status_code == 201

@app.route("/upload-known", methods=["POST"])
def upload_known():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    filename = image.filename
    save_path = os.path.join("/tmp", filename)
    image.save(save_path)

    success = upload_to_github(filename, save_path)
    os.remove(save_path)

    if success:
        return jsonify({"message": "Image uploaded successfully"}), 200
    else:
        return jsonify({"error": "Failed to upload image"}), 500


import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = "Bhandary1943/Second-Eye"
FOLDER = "known_faces"

def upload_to_github(filename, file_path):
    with open(file_path, "rb") as f:
        content = f.read()

    from base64 import b64encode
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

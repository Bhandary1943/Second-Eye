
# import streamlit as st
# from deepface import DeepFace
# import requests
# from PIL import Image
# from gtts import gTTS
# import os

# KNOWN_FOLDER = "known_faces"
# SERVER_URL = "https://esp32-upload-server.onrender.com"

# def get_latest_image():
#     r = requests.get(f"{SERVER_URL}/latest")
#     if r.status_code != 200:
#         return None
#     filename = r.json()["filename"]
#     image_url = f"{SERVER_URL}/uploads/{filename}"
#     return image_url

# def compare_with_known_faces(unknown_img_path):
#     for filename in os.listdir(KNOWN_FOLDER):
#         known_img_path = os.path.join(KNOWN_FOLDER, filename)
#         try:
#             result = DeepFace.verify(img1_path=unknown_img_path, img2_path=known_img_path, enforce_detection=False)
#             if result["verified"]:
#                 return filename.split('.')[0]
#         except Exception as e:
#             print(f"Error comparing with {filename}: {e}")
#     return None

# st.title("ESP32-CAM Face Recognition with DeepFace")

# if st.button("Check for New Image"):
#     image_url = get_latest_image()
#     if image_url:
#         st.image(image_url, caption="Captured Image")
#         response = requests.get(image_url)
#         with open("latest.jpg", "wb") as f:
#             f.write(response.content)

#         match = compare_with_known_faces("latest.jpg")
#         if match:
#             st.success(f"✅ Match found: {match}")
#             tts = gTTS(f"Match found: {match}")
#         else:
#             st.error("❌ No match found")
#             tts = gTTS("No match found")
#         tts.save("result.mp3")
#         st.audio("result.mp3", autoplay=True)
#     else:
#         st.warning("No image found on server.")



import streamlit as st
from deepface import DeepFace
import requests
from PIL import Image
from gtts import gTTS
import os

KNOWN_FOLDER = "known_faces"
SERVER_URL = "https://esp32-upload-server.onrender.com"

def get_latest_image():
    r = requests.get(f"{SERVER_URL}/latest")
    if r.status_code != 200:
        return None
    filename = r.json()["filename"]
    image_url = f"{SERVER_URL}/uploads/{filename}"
    return image_url

def is_face_detected(image_path):
    try:
        faces = DeepFace.extract_faces(img_path=image_path, enforce_detection=True)
        return len(faces) > 0
    except:
        return False

def compare_with_known_faces(unknown_img_path):
    for filename in os.listdir(KNOWN_FOLDER):
        known_img_path = os.path.join(KNOWN_FOLDER, filename)
        try:
            result = DeepFace.verify(img1_path=unknown_img_path, img2_path=known_img_path, enforce_detection=True)
            if result["verified"]:
                return filename.split('.')[0]
        except Exception as e:
            print(f"No face detected or comparison failed with {filename}: {e}")
    return None

st.title("ESP32-CAM Face Recognition with DeepFace")

if st.button("Check for New Image"):
    image_url = get_latest_image()
    if image_url:
        st.image(image_url, caption="Captured Image")
        response = requests.get(image_url)
        with open("latest.jpg", "wb") as f:
            f.write(response.content)

        if is_face_detected("latest.jpg"):
            match = compare_with_known_faces("latest.jpg")
            if match:
                st.success(f"✅ Match found: {match}")
                tts = gTTS(f"Match found: {match}")
            else:
                st.error("❌ No match found")
                tts = gTTS("No match found")
        else:
            st.warning("😕 No face detected in the captured image.")
            tts = gTTS("No face detected")
        tts.save("result.mp3")
        st.audio("result.mp3", autoplay=True)
    else:
        st.warning("No image found on server.")






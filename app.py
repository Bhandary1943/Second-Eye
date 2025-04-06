# import streamlit as st
# import face_recognition
# import requests
# from PIL import Image
# import os
# from gtts import gTTS

# KNOWN_FOLDER = "known_faces"
# SERVER_URL = "https://esp32-upload-server.onrender.com"

# def get_latest_image():
#     r = requests.get(f"{SERVER_URL}/latest")
#     if r.status_code != 200:
#         return None
#     filename = r.json()["filename"]
#     image_url = f"{SERVER_URL}/uploads/{filename}"
#     return image_url

# def compare_faces(unknown_path):
#     unknown_image = face_recognition.load_image_file(unknown_path)
#     unknown_encodings = face_recognition.face_encodings(unknown_image)
#     if not unknown_encodings:
#         return None

#     for name in os.listdir(KNOWN_FOLDER):
#         path = os.path.join(KNOWN_FOLDER, name)
#         known_image = face_recognition.load_image_file(path)
#         known_encodings = face_recognition.face_encodings(known_image)
#         if known_encodings and face_recognition.compare_faces([known_encodings[0]], unknown_encodings[0])[0]:
#             return name.split('.')[0]
#     return None

# st.title("ESP32-CAM Face Recognition")

# if st.button("Check for New Image"):
#     image_url = get_latest_image()
#     if image_url:
#         st.image(image_url, caption="Captured Image")
#         response = requests.get(image_url)
#         with open("latest.jpg", "wb") as f:
#             f.write(response.content)

#         match = compare_faces("latest.jpg")
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

def compare_with_known_faces(unknown_img_path):
    best_match = None
    best_distance = 1.0  # initialize with max distance
    for filename in os.listdir(KNOWN_FOLDER):
        known_img_path = os.path.join(KNOWN_FOLDER, filename)
        try:
            result = DeepFace.verify(
                img1_path=unknown_img_path,
                img2_path=known_img_path,
                enforce_detection=True
            )
            distance = result['distance']
            verified = result['verified']
            print(f"Compared with {filename}: Verified={verified}, Distance={distance}")

            if verified and distance < best_distance:
                best_distance = distance
                best_match = filename.split('.')[0]
        except Exception as e:
            print(f"❌ Error comparing with {filename}: {e}")
    return best_match

st.title("🔍 ESP32-CAM Face Recognition with DeepFace")

if st.button("📸 Check for New Image"):
    image_url = get_latest_image()
    if image_url:
        st.image(image_url, caption="📷 Captured Image", use_column_width=True)
        response = requests.get(image_url)
        with open("latest.jpg", "wb") as f:
            f.write(response.content)

        match = compare_with_known_faces("latest.jpg")
        if match:
            st.success(f"✅ Match found: {match}")
            tts = gTTS(f"Match found: {match}")
        else:
            st.error("❌ No match found or face not clearly visible")
            tts = gTTS("No match found")
        tts.save("result.mp3")
        st.audio("result.mp3", autoplay=True)
    else:
        st.warning("⚠️ No image found on the server.")

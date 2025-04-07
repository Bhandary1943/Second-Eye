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



# import streamlit as st
# from deepface import DeepFace
# import requests
# from PIL import Image
# from gtts import gTTS
# import os

# KNOWN_FOLDER = "known_faces"
# SERVER_URL = "https://esp32-upload-server.onrender.com"
# MATCH_THRESHOLD = 0.6  # 🔐 Only match if distance < 0.6

# def get_latest_image():
#     try:
#         r = requests.get(f"{SERVER_URL}/latest", timeout=5)
#         if r.status_code != 200:
#             return None
#         filename = r.json()["filename"]
#         image_url = f"{SERVER_URL}/uploads/{filename}"
#         return image_url
#     except Exception as e:
#         print("Error fetching image:", e)
#         return None

# def compare_with_known_faces(unknown_img_path):
#     best_match = None
#     best_distance = 1.0  # start with max distance

#     for filename in os.listdir(KNOWN_FOLDER):
#         known_img_path = os.path.join(KNOWN_FOLDER, filename)
#         try:
#             result = DeepFace.verify(
#                 img1_path=unknown_img_path,
#                 img2_path=known_img_path,
#                 model_name="Dlib",
#                 enforce_detection=False
#             )
#             distance = result['distance']
#             print(f"Comparing with {filename}: Distance = {distance:.4f}, Verified = {result['verified']}")

#             if distance < best_distance and distance < MATCH_THRESHOLD:
#                 best_distance = distance
#                 best_match = filename.split('.')[0]
#         except Exception as e:
#             print(f"Error comparing with {filename}: {e}")
#     return best_match

# st.title("📸 ESP32-CAM Face Recognition with DeepFace (Dlib - Accurate)")

# if st.button("🔍 Check for New Image"):
#     image_url = get_latest_image()
#     if image_url:
#         st.image(image_url, caption="Captured Image", use_column_width=True)
#         response = requests.get(image_url)
#         with open("latest.jpg", "wb") as f:
#             f.write(response.content)

#         match = compare_with_known_faces("latest.jpg")
#         if match:
#             st.success(f"✅ Match found: {match}")
#             tts = gTTS(f"Match found: {match}")
#         else:
#             st.error("❌ No accurate match found")
#             tts = gTTS("No accurate match found")
#         tts.save("result.mp3")
#         st.audio("result.mp3", autoplay=True)
#     else:
#         st.warning("⚠️ No image found on server.")


import streamlit as st
import face_recognition
import requests
from PIL import Image
from gtts import gTTS
import os

KNOWN_FOLDER = "known_faces"  # Folder with known faces
SERVER_URL = "https://esp32-upload-server.onrender.com"  # ESP32-CAM upload server

def get_latest_image():
    try:
        r = requests.get(f"{SERVER_URL}/latest", timeout=5)
        if r.status_code != 200:
            return None
        filename = r.json()["filename"]
        image_url = f"{SERVER_URL}/uploads/{filename}"
        return image_url
    except Exception as e:
        st.error(f"Error getting latest image: {e}")
        return None

def compare_with_known_faces(unknown_img_path):
    try:
        unknown_image = face_recognition.load_image_file(unknown_img_path)
        unknown_encodings = face_recognition.face_encodings(unknown_image)
        if not unknown_encodings:
            return None  # No face found
        unknown_encoding = unknown_encodings[0]

        for filename in os.listdir(KNOWN_FOLDER):
            known_img_path = os.path.join(KNOWN_FOLDER, filename)
            known_image = face_recognition.load_image_file(known_img_path)
            known_encodings = face_recognition.face_encodings(known_image)
            if not known_encodings:
                continue  # Skip if no face in known image
            match = face_recognition.compare_faces([known_encodings[0]], unknown_encoding)
            if match[0]:
                return os.path.splitext(filename)[0]  # Return name (without extension)
        return None
    except Exception as e:
        st.error(f"Face comparison error: {e}")
        return None

def speak(text):
    tts = gTTS(text)
    tts.save("result.mp3")
    st.audio("result.mp3", autoplay=True)

st.title("📸 ESP32-CAM Face Recognition (using face_recognition)")

if st.button("Check for New Image"):
    image_url = get_latest_image()
    if image_url:
        st.image(image_url, caption="Captured Image")

        # Download image
        try:
            response = requests.get(image_url, timeout=5)
            with open("latest.jpg", "wb") as f:
                f.write(response.content)
        except Exception as e:
            st.error(f"Image download failed: {e}")
            st.stop()

        # Compare with known faces
        match = compare_with_known_faces("latest.jpg")
        if match:
            st.success(f"✅ Match found: {match}")
            speak(f"Match found with {match}")
        else:
            st.error("❌ No match found")
            speak("No match found")

        # Optional: delete downloaded image
        os.remove("latest.jpg")
    else:
        st.warning("⚠️ No image found on server.")



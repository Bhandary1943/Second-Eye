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
import os
from gtts import gTTS

# Folder where known/reference images are stored
REFERENCE_FOLDER = "known_faces"
# ESP32-CAM image server
SERVER_URL = "https://esp32-upload-server.onrender.com"
SAVE_PATH = "latest.jpg"

def get_latest_image():
    try:
        r = requests.get(f"{SERVER_URL}/latest", timeout=10)
        if r.status_code != 200:
            return None
        filename = r.json()["filename"]
        image_url = f"{SERVER_URL}/uploads/{filename}"
        return image_url
    except Exception as e:
        print("Error getting latest image:", e)
        return None

def compare_faces(image1_path, image2_path):
    try:
        img1 = face_recognition.load_image_file(image1_path)
        img2 = face_recognition.load_image_file(image2_path)

        encodings1 = face_recognition.face_encodings(img1)
        encodings2 = face_recognition.face_encodings(img2)

        if encodings1 and encodings2:
            result = face_recognition.compare_faces([encodings1[0]], encodings2[0])
            return result[0]
        else:
            print("No faces found in one of the images.")
            return False
    except Exception as e:
        print("Comparison error:", e)
        return False

def speak(message):
    tts = gTTS(message)
    tts.save("result.mp3")
    st.audio("result.mp3", autoplay=True)

# Streamlit UI
st.title("🔍 ESP32-CAM Face Recognition (with face_recognition)")

if st.button("📸 Check for New Image"):
    image_url = get_latest_image()
    if image_url:
        st.image(image_url, caption="Captured Image", use_column_width=True)
        response = requests.get(image_url)
        with open(SAVE_PATH, "wb") as f:
            f.write(response.content)

        match_found = False
        for ref_file in os.listdir(REFERENCE_FOLDER):
            ref_path = os.path.join(REFERENCE_FOLDER, ref_file)
            if compare_faces(SAVE_PATH, ref_path):
                name = os.path.splitext(ref_file)[0]
                message = f"Match found with {name}"
                st.success(f"✅ {message}")
                speak(message)
                match_found = True
                break

        if not match_found:
            message = "No match found"
            st.error("❌ No match found")
            speak(message)
    else:
        st.warning("⚠️ No image found on the server.")




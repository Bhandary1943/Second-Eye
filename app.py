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
    try:
        r = requests.get(f"{SERVER_URL}/latest", timeout=5)
        if r.status_code != 200:
            return None
        filename = r.json()["filename"]
        return f"{SERVER_URL}/uploads/{filename}"
    except Exception as e:
        print("Error fetching image:", e)
        return None

def test_face_detection(img_path):
    try:
        analysis = DeepFace.analyze(
            img_path=img_path,
            actions=['emotion'],  # force face detection
            enforce_detection=False
        )
        print("Detection success:", analysis)
        return True
    except Exception as e:
        print("Face not detected:", e)
        return False

def compare_with_known_faces(unknown_img_path):
    try:
        result = DeepFace.find(
            img_path=unknown_img_path,
            db_path=KNOWN_FOLDER,
            model_name='Facenet512',
            distance_metric='cosine',
            enforce_detection=False  # allow weak ESP32-CAM images
        )
        if len(result) > 0 and len(result[0]) > 0:
            top_match = result[0].iloc[0]
            distance = top_match["distance"]
            print("Top match:", top_match["identity"], "| Distance:", distance)

            if distance < 0.35:  # Looser threshold
                return os.path.basename(top_match["identity"]).split(".")[0]
        return None
    except Exception as e:
        print("DeepFace error:", e)
        return None

# Streamlit UI
st.title("🔍 ESP32-CAM Face Recognition with DeepFace")

if st.button("📸 Check for New Image"):
    image_url = get_latest_image()
    if image_url:
        st.image(image_url, caption="Captured Image", use_column_width=True)
        response = requests.get(image_url)
        with open("latest.jpg", "wb") as f:
            f.write(response.content)

        if test_face_detection("latest.jpg"):
            match = compare_with_known_faces("latest.jpg")
            if match:
                st.success(f"✅ Match found: {match}")
                tts = gTTS(f"Match found: {match}")
            else:
                st.error("❌ No accurate match found")
                tts = gTTS("No accurate match found")
        else:
            st.error("❌ No face detected in the image. Please try again with better lighting or camera angle.")
            tts = gTTS("No face detected in the image. Please try again.")
        
        tts.save("result.mp3")
        st.audio("result.mp3", autoplay=True)
    else:
        st.warning("⚠️ No image found on the server.")




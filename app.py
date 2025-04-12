
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

# def get_latest_image():
#     r = requests.get(f"{SERVER_URL}/latest")
#     if r.status_code != 200:
#         return None
#     filename = r.json()["filename"]
#     image_url = f"{SERVER_URL}/uploads/{filename}"
#     return image_url

# def is_face_detected(image_path):
#     try:
#         faces = DeepFace.extract_faces(img_path=image_path, enforce_detection=True)
#         return len(faces) > 0
#     except:
#         return False

# def compare_with_known_faces(unknown_img_path):
#     for filename in os.listdir(KNOWN_FOLDER):
#         known_img_path = os.path.join(KNOWN_FOLDER, filename)
#         try:
#             result = DeepFace.verify(img1_path=unknown_img_path, img2_path=known_img_path, enforce_detection=True)
#             if result["verified"]:
#                 return filename.split('.')[0]
#         except Exception as e:
#             print(f"No face detected or comparison failed with {filename}: {e}")
#     return None

# st.title("ESP32-CAM Face Recognition with DeepFace")

# if st.button("Check for New Image"):
#     image_url = get_latest_image()
#     if image_url:
#         st.image(image_url, caption="Captured Image")
#         response = requests.get(image_url)
#         with open("latest.jpg", "wb") as f:
#             f.write(response.content)

#         if is_face_detected("latest.jpg"):
#             match = compare_with_known_faces("latest.jpg")
#             if match:
#                 st.success(f"✅ Match found: {match}")
#                 tts = gTTS(f"Match found: {match}")
#             else:
#                 st.error("❌ No match found")
#                 tts = gTTS("No match found")
#         else:
#             st.warning("😕 No face detected in the captured image.")
#             tts = gTTS("No face detected")
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
# ESP32_SERVER_URL = "https://esp32-upload-server.onrender.com"
# FLASK_UPLOAD_URL = "https://flask-upload-pzch.onrender.com/upload"

# # Page Navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Face Recognition", "Upload Known Face"])

# # Function to get latest image from ESP32 server
# def get_latest_image():
#     r = requests.get(f"{ESP32_SERVER_URL}/latest")
#     if r.status_code != 200:
#         return None
#     filename = r.json()["filename"]
#     image_url = f"{ESP32_SERVER_URL}/uploads/{filename}"
#     return image_url

# # Function to check if face is detected
# def is_face_detected(image_path):
#     try:
#         faces = DeepFace.extract_faces(img_path=image_path, enforce_detection=True)
#         return len(faces) > 0
#     except:
#         return False

# # Function to compare image with known faces
# def compare_with_known_faces(unknown_img_path):
#     for filename in os.listdir(KNOWN_FOLDER):
#         known_img_path = os.path.join(KNOWN_FOLDER, filename)
#         try:
#             result = DeepFace.verify(img1_path=unknown_img_path, img2_path=known_img_path, enforce_detection=True)
#             if result["verified"]:
#                 return filename.split('.')[0]
#         except Exception as e:
#             print(f"No face detected or comparison failed with {filename}: {e}")
#     return None

# # -------------------- PAGE 1: Face Recognition --------------------
# if page == "Face Recognition":
#     st.title("ESP32-CAM Face Recognition with DeepFace")

#     if st.button("Check for New Image"):
#         image_url = get_latest_image()
#         if image_url:
#             st.image(image_url, caption="Captured Image", use_container_width=True)
#             response = requests.get(image_url)
#             with open("latest.jpg", "wb") as f:
#                 f.write(response.content)

#             if is_face_detected("latest.jpg"):
#                 match = compare_with_known_faces("latest.jpg")
#                 if match:
#                     st.success(f"✅ Match found: {match}")
#                     tts = gTTS(f"Match found: {match}")
#                 else:
#                     st.error("❌ No match found")
#                     tts = gTTS("No match found")
#             else:
#                 st.warning("😕 No face detected in the captured image.")
#                 tts = gTTS("No face detected")

#             tts.save("result.mp3")
#             st.audio("result.mp3", autoplay=True)
#         else:
#             st.warning("No image found on server.")

# # -------------------- PAGE 2: Upload Known Face --------------------
# # Upload Known Face Page
# elif page == "Upload Known Face":
#     st.title("Upload New Known Face")
#     MAX_FILE_SIZE_MB = 3
#     MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

#     uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
#     if uploaded_file is not None:
#         st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

#         if st.button("Upload to GitHub"):
#             file_data = uploaded_file.getvalue()

#             if len(file_data) > MAX_FILE_SIZE_BYTES:
#                 st.error(f"❌ File too large. Please upload a file under {MAX_FILE_SIZE_MB} MB.")
#             else:
#                 try:
#                     safe_filename = uploaded_file.name.replace(" ", "_")
#                     files = {"file": (safe_filename, file_data)}
#                     response = requests.post(FLASK_UPLOAD_URL, files=files, timeout=30)

#                     if response.status_code == 201:
#                         st.success("✅ Image uploaded to GitHub successfully.")
#                     else:
#                         st.error(f"❌ Upload failed. Status code: {response.status_code}\n{response.text}")
#                 except requests.exceptions.ChunkedEncodingError:
#                     st.error("⚠️ Upload failed due to network or encoding error. Try again or use a smaller image.")
#                 except requests.exceptions.RequestException as e:
#                     st.error(f"⚠️ Upload failed: {str(e)}")



import streamlit as st
from deepface import DeepFace
import requests
from PIL import Image
import os
import io

KNOWN_FOLDER = "known_faces"
ESP32_SERVER_URL = "https://esp32-upload-server.onrender.com"
FLASK_UPLOAD_URL = "https://flask-upload-pzch.onrender.com/upload"

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Face Recognition", "Upload Known Face"])

# Load light SFace model
@st.cache_resource
def load_sface_model():
    return DeepFace.build_model("SFace")

model = load_sface_model()

# Get latest image
def get_latest_image():
    try:
        r = requests.get(f"{ESP32_SERVER_URL}/latest", timeout=10)
        if r.status_code != 200:
            return None
        filename = r.json()["filename"]
        return f"{ESP32_SERVER_URL}/uploads/{filename}"
    except:
        return None

# Face detection
def is_face_detected(image_path):
    try:
        faces = DeepFace.extract_faces(img_path=image_path, enforce_detection=True)
        return len(faces) > 0
    except:
        return False

# Face matching
def compare_with_known_faces(unknown_img_path):
    for filename in os.listdir(KNOWN_FOLDER):
        known_img_path = os.path.join(KNOWN_FOLDER, filename)
        try:
            if not is_face_detected(known_img_path):
                continue

            result = DeepFace.verify(
                img1_path=unknown_img_path,
                img2_path=known_img_path,
                model_name="SFace",
                model=model,
                enforce_detection=True,
                distance_metric='cosine'
            )

            if result["verified"] or result["distance"] < 0.4:
                return filename.split('.')[0]

        except:
            pass
    return None

# ------------ PAGE 1 ------------
if page == "Face Recognition":
    st.title("ESP32-CAM Face Recognition")

    if st.button("Check for New Image"):
        image_url = get_latest_image()
        if image_url:
            st.image(image_url, caption="Captured Image", use_container_width=True)

            # Save image as RGB
            response = requests.get(image_url)
            img = Image.open(io.BytesIO(response.content)).convert("RGB")
            img.save("latest.jpg")

            if is_face_detected("latest.jpg"):
                match = compare_with_known_faces("latest.jpg")
                if match:
                    st.success(f"✅ Match found: {match}")
                else:
                    st.error("❌ No match found")
            else:
                st.warning("😕 No face detected in the image.")
        else:
            st.warning("No image found on server.")

# ------------ PAGE 2 ------------
elif page == "Upload Known Face":
    st.title("Upload New Known Face")
    MAX_MB = 3
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        if st.button("Upload to GitHub"):
            if len(uploaded_file.getvalue()) > MAX_MB * 1024 * 1024:
                st.error("❌ File too large. Max 3MB.")
            else:
                try:
                    files = {"file": (uploaded_file.name.replace(" ", "_"), uploaded_file.getvalue())}
                    res = requests.post(FLASK_UPLOAD_URL, files=files, timeout=30)
                    if res.status_code == 201:
                        st.success("✅ Uploaded to GitHub successfully.")
                    else:
                        st.error(f"❌ Upload failed: {res.status_code}")
                except:
                    st.error("⚠️ Upload error.")







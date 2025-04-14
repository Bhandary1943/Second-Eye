
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




# using sklearn

# import streamlit as st
# from deepface import DeepFace
# import requests
# from PIL import Image
# from gtts import gTTS
# import os
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# # Configuration
# KNOWN_FOLDER = "known_faces"
# ESP32_SERVER_URL = "https://esp32-upload-server.onrender.com"
# FLASK_UPLOAD_URL = "https://flask-upload-pzch.onrender.com/upload"
# MODEL_NAME = "Facenet"
# THRESHOLD = 0.4  # Lower = stricter match

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

# # Improved comparison function using embeddings
# def compare_with_known_faces(unknown_img_path, model_name=MODEL_NAME, threshold=THRESHOLD):
#     try:
#         unknown_embedding = DeepFace.represent(img_path=unknown_img_path, model_name=model_name, enforce_detection=True)[0]["embedding"]
#     except:
#         return None

#     best_match = None
#     best_score = 1  # Lowest distance = best match

#     for filename in os.listdir(KNOWN_FOLDER):
#         known_img_path = os.path.join(KNOWN_FOLDER, filename)
#         try:
#             known_embedding = DeepFace.represent(img_path=known_img_path, model_name=model_name, enforce_detection=True)[0]["embedding"]
#             similarity = cosine_similarity([unknown_embedding], [known_embedding])[0][0]
#             distance = 1 - similarity
#             print(f"Compared with {filename}, distance: {distance:.4f}")

#             if distance < threshold and distance < best_score:
#                 best_score = distance
#                 best_match = filename.split('.')[0]
#         except Exception as e:
#             print(f"Error comparing with {filename}: {e}")

#     return best_match

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
from gtts import gTTS
import os
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Configuration
KNOWN_FOLDER = "known_faces"
ESP32_SERVER_URL = "https://esp32-upload-server.onrender.com"
FLASK_UPLOAD_URL = "https://flask-upload-pzch.onrender.com/upload"
MODEL_NAME = "Facenet"
THRESHOLD = 0.4  # Lower = stricter match

# Page Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Face Recognition", "About Us", "Upload Known Face"])

# Function to get latest image from ESP32 server
def get_latest_image():
    r = requests.get(f"{ESP32_SERVER_URL}/latest")
    if r.status_code != 200:
        return None
    filename = r.json()["filename"]
    image_url = f"{ESP32_SERVER_URL}/uploads/{filename}"
    return image_url

# Function to check if face is detected
def is_face_detected(image_path):
    try:
        faces = DeepFace.extract_faces(img_path=image_path, enforce_detection=True)
        return len(faces) > 0
    except:
        return False

# Improved comparison function using embeddings
def compare_with_known_faces(unknown_img_path, model_name=MODEL_NAME, threshold=THRESHOLD):
    try:
        unknown_embedding = DeepFace.represent(img_path=unknown_img_path, model_name=model_name, enforce_detection=True)[0]["embedding"]
    except:
        return None

    best_match = None
    best_score = 1  # Lowest distance = best match

    for filename in os.listdir(KNOWN_FOLDER):
        known_img_path = os.path.join(KNOWN_FOLDER, filename)
        try:
            known_embedding = DeepFace.represent(img_path=known_img_path, model_name=model_name, enforce_detection=True)[0]["embedding"]
            similarity = cosine_similarity([unknown_embedding], [known_embedding])[0][0]
            distance = 1 - similarity
            print(f"Compared with {filename}, distance: {distance:.4f}")

            if distance < threshold and distance < best_score:
                best_score = distance
                best_match = filename.split('.')[0]
        except Exception as e:
            print(f"Error comparing with {filename}: {e}")

    return best_match

# -------------------- PAGE 1: Face Recognition --------------------
if page == "Face Recognition":
    st.title("📸 ESP32-CAM Face Recognition")

    if st.button("Check for New Image"):
        image_url = get_latest_image()
        if image_url:
            st.image(image_url, caption="Captured Image", use_container_width=True)
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

# -------------------- PAGE 2: About Us --------------------
elif page == "About Us":
    st.title("💡 About Second Eye Project")

    st.markdown("""
    ### 👁️ What is Second Eye?
    **Second Eye** is an assistive vision system designed for **visually impaired individuals**. It uses an **ESP32-CAM** module to capture images of people in front of the user. These images are then analyzed using advanced face recognition to determine who is in the frame.

    ### 🛠️ How it Works:
    1. The **ESP32-CAM** captures a photo and uploads it to a cloud server.
    2. Our **Streamlit web app** fetches this image and uses **DeepFace with FaceNet** to extract facial features.
    3. It compares the captured face with a database of **known faces** using **cosine similarity**.
    4. If a match is found, the app plays an **audio alert** saying the person’s name using **Google Text-to-Speech (gTTS)**.
    5. If no match is found or no face is detected, it notifies the user accordingly.

    ### 🌐 System Architecture:
    - ESP32-CAM for image capture
    - Flask server for uploading & storing images
    - GitHub as a cloud face database
    - DeepFace for face recognition
    - Streamlit as the user interface

    ### 🚀 Purpose:
    Our goal is to **empower the visually impaired** by giving them a way to recognize people around them using face recognition and audio feedback, making the world more accessible and safer.

    ---
    *Made with ❤️ by Team Second Eye.*
    """)

# -------------------- PAGE 3: Upload Known Face --------------------
elif page == "Upload Known Face":
    st.title("📤 Upload New Known Face")
    MAX_FILE_SIZE_MB = 3
    MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        if st.button("Upload to GitHub"):
            file_data = uploaded_file.getvalue()

            if len(file_data) > MAX_FILE_SIZE_BYTES:
                st.error(f"❌ File too large. Please upload a file under {MAX_FILE_SIZE_MB} MB.")
            else:
                try:
                    safe_filename = uploaded_file.name.replace(" ", "_")
                    files = {"file": (safe_filename, file_data)}
                    response = requests.post(FLASK_UPLOAD_URL, files=files, timeout=30)

                    if response.status_code == 201:
                        st.success("✅ Image uploaded to GitHub successfully.")
                    else:
                        st.error(f"❌ Upload failed. Status code: {response.status_code}\n{response.text}")
                except requests.exceptions.ChunkedEncodingError:
                    st.error("⚠️ Upload failed due to network or encoding error. Try again or use a smaller image.")
                except requests.exceptions.RequestException as e:
                    st.error(f"⚠️ Upload failed: {str(e)}")

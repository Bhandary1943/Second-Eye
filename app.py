
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

# ---------------- Configuration ----------------
KNOWN_FOLDER = "known_faces"
ESP32_SERVER_URL = "https://esp32-upload-server.onrender.com"
FLASK_UPLOAD_URL = "https://flask-upload-pzch.onrender.com/upload"
MODEL_NAME = "Facenet"
THRESHOLD = 0.4  # Lower = stricter match

st.set_page_config(page_title="Second Eye", layout="centered")

# --------------- Sidebar Navigation ---------------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3601/3601536.png", width=100)
st.sidebar.title("🔍 Second Eye Navigation")
page = st.sidebar.radio("Go to", [
    "🏠 Home", 
    "📚 About Us", 
    "🧑‍🏫 Supervisor", 
    "🙋‍♂️ User - Face Recognition", 
    "📤 Upload Known Face"
])

# ---------------- Utility Functions ----------------
def get_latest_image():
    r = requests.get(f"{ESP32_SERVER_URL}/latest")
    if r.status_code != 200:
        return None
    filename = r.json()["filename"]
    return f"{ESP32_SERVER_URL}/uploads/{filename}"

def is_face_detected(image_path):
    try:
        faces = DeepFace.extract_faces(img_path=image_path, enforce_detection=True)
        return len(faces) > 0
    except:
        return False

def compare_with_known_faces(unknown_img_path, model_name=MODEL_NAME, threshold=THRESHOLD):
    try:
        unknown_embedding = DeepFace.represent(img_path=unknown_img_path, model_name=model_name, enforce_detection=True)[0]["embedding"]
    except:
        return None

    best_match = None
    best_score = 1

    for filename in os.listdir(KNOWN_FOLDER):
        known_img_path = os.path.join(KNOWN_FOLDER, filename)
        try:
            known_embedding = DeepFace.represent(img_path=known_img_path, model_name=model_name, enforce_detection=True)[0]["embedding"]
            similarity = cosine_similarity([unknown_embedding], [known_embedding])[0][0]
            distance = 1 - similarity
            if distance < threshold and distance < best_score:
                best_score = distance
                best_match = filename.split('.')[0]
        except:
            pass
    return best_match

# -------------------- 🏠 Home Page --------------------
if page == "🏠 Home":
    st.markdown("<h1 style='text-align: center;'>👁️ Second Eye</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: gray;'>Empowering the visually impaired with smart vision</h3>", unsafe_allow_html=True)
    st.image("https://cdn.pixabay.com/photo/2017/03/05/18/59/eye-2116108_1280.jpg", use_column_width=True)
    st.markdown("""
        <div style='padding: 1rem; font-size: 18px;'>
            Welcome to <b>Second Eye</b> – an assistive system designed for the visually impaired using AI-powered facial recognition. 
            <br><br>
            With just a glance from an ESP32-CAM, the device identifies known individuals and speaks out their names using speech synthesis.
            <br><br>
            Navigate through the menu to explore how it works, meet our team, and test the system!
        </div>
    """, unsafe_allow_html=True)

# -------------------- 📚 About Us Page --------------------
elif page == "📚 About Us":
    st.markdown("<h2 style='text-align: center;'>📚 About Second Eye</h2>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/4370/4370564.png", width=120)

    st.markdown("""
        <div style='font-size: 17px; padding-top: 1rem;'>
            <b>Second Eye</b> is a real-time face recognition system built with the goal of assisting visually impaired individuals.
            <br><br>
            Our system uses:
            <ul>
                <li>📸 An ESP32-CAM module to capture live images</li>
                <li>🧠 Deep learning models (Facenet via DeepFace) to recognize faces</li>
                <li>🔊 Text-to-speech to announce the matched identity</li>
                <li>☁️ Cloud storage and interfaces for managing known faces</li>
            </ul>
            <br>
            It is easy to use, reliable, and can be expanded into a complete wearable smart vision solution.
        </div>
    """, unsafe_allow_html=True)

# -------------------- 🧑‍🏫 Supervisor Page --------------------
elif page == "🧑‍🏫 Supervisor":
    st.markdown("<h2 style='text-align: center;'>🧑‍🏫 Our Guide</h2>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)

    st.markdown("""
        <div style='font-size: 17px; padding-top: 1rem;'>
            We are grateful to our project supervisor:
            <ul>
                <li><b>Dr. John Doe</b> – Associate Professor, Department of Electronics</li>
                <li>Expert in Embedded Systems & AI</li>
            </ul>
            <br>
            <i>"Guidance is the light that shows the path when technology meets purpose."</i>
        </div>
    """, unsafe_allow_html=True)

# -------------------- 🙋‍♂️ Face Recognition Page --------------------
elif page == "🙋‍♂️ User - Face Recognition":
    st.title("🙋‍♂️ ESP32-CAM Face Recognition")

    if st.button("🔍 Check for New Image"):
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
            st.warning("⚠️ No image found on server.")

# -------------------- 📤 Upload Known Face Page --------------------
elif page == "📤 Upload Known Face":
    st.title("📤 Upload New Known Face")
    MAX_MB = 3
    MAX_BYTES = MAX_MB * 1024 * 1024

    uploaded_file = st.file_uploader("Choose a face image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        if st.button("⬆️ Upload to GitHub"):
            file_data = uploaded_file.getvalue()
            if len(file_data) > MAX_BYTES:
                st.error(f"❌ File too large. Please keep under {MAX_MB} MB.")
            else:
                try:
                    safe_filename = uploaded_file.name.replace(" ", "_")
                    files = {"file": (safe_filename, file_data)}
                    response = requests.post(FLASK_UPLOAD_URL, files=files, timeout=30)

                    if response.status_code == 201:
                        st.success("✅ Image uploaded successfully.")
                    else:
                        st.error(f"❌ Upload failed. Status: {response.status_code}\n{response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"⚠️ Upload failed: {str(e)}")

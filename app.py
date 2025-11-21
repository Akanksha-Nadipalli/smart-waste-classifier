import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import io

# Load model
model = tf.keras.models.load_model("garbage_mobilenet_augmented.keras")
CLASS_NAMES = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# styling
st.markdown("""
<style>
.stApp {
    background-color: #3D6FAD;
    color: #333333;
}
div.stButton > button:first-child {
    color: #ffffff;
    border-radius: 10px;
    padding: 0.5em 1em;
    font-size: 16px;
}
.stFileUploader>label {
    font-weight: bold;
    color: #ffffff;        
}
.app-title {
    color: #ffffff;      
    text-shadow: 2px 2px #383636;
    font-family: 'Arial', sans-serif;
    font-size: 40px;
}            
.stFileUploader > label {
    color: white !important;
}

            
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Settings")
lang = st.sidebar.selectbox("Choose Language / भाषा चुनें:", ["English", "हिन्दी"])


st.markdown('<h1 class="app-title">♻️ Smart Waste Classification App</h1>', unsafe_allow_html=True)

if lang == "English":
    st.markdown("Upload an image or use your camera to classify waste in real-time!")
else:
    st.markdown("अपशिष्ट वर्गीकृत करने के लिए एक छवि अपलोड करें या अपने कैमरे का उपयोग करें।")

choice = st.radio("Select input method / इनपुट विकल्प चुनें:", ["Upload Image", "Use Camera"])

image = None
if choice == "Upload Image":
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
elif choice == "Use Camera":
    camera_image = st.camera_input("Take a photo with your camera")
    if camera_image is not None:
        image = Image.open(camera_image).convert("RGB")

# Prediction
if image is not None:
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Input Image", use_container_width=True)

    img = image.resize((224,224))
    img_array = np.array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    
    with st.spinner('Classifying your image, please wait...'):
        predictions = model.predict(img_array)
    
    class_index = np.argmax(predictions)
    confidence = np.max(predictions)

    with col2:
        st.markdown(f"<h2 style='color:#E4ECF0'>Prediction: {CLASS_NAMES[class_index]}</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3>Confidence: {confidence*100:.2f}%</h3>", unsafe_allow_html=True)

       

if st.button("Rerun"):
    st.session_state.clear()
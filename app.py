import streamlit as st
import pickle
from PIL import Image
import numpy as np

# Load the trained model
with open('diabetic_retinopathy_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app title
im = Image.open('logo.png')
st.set_page_config(page_title="Diabetic Retinopathy Detection", page_icon=im)
st.title('Diabetic Retinopathy Detection')

# File uploader for image input
uploaded_file = st.file_uploader("Choose a retinal image...", type=["jpg", "png"])

if uploaded_file is not None:
    # Load and preprocess the image
    img = Image.open(uploaded_file)
    img = img.resize((224, 224))  # Resize to match model input
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = img_array.reshape(1, -1)  # Reshape for model input

    # Display the uploaded image
    st.image(img, caption='Uploaded Image', use_column_width=True)

    # Button for prediction
    if st.button('Predict'):
        prediction = model.predict(img_array)
        st.write(f'Prediction: {"Diabetic Retinopathy Detected" if prediction[0] != 0 else "No Diabetic Retinopathy"}')

# Contact Me section
st.markdown("""
    <hr>
    <h3>Contact Me</h3>
    <p>
        <a href="https://github.com/Heet852003" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/ffffff/github.png" width="30" height="30">
        </a>
        <a href="https://www.linkedin.com/in/heet-mehta-41b862225" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/ffffff/linkedin.png" width="30" height="30">
        </a>
        <a href="mailto:mehtaheet5@gmail.com">
            <img src="https://fontawesome.com/v5/icons/inbox?f=classic&s=solid" width="30" height="30">
        </a>
    </p>
    <style>
        hr {
            border: 0;
            height: 1px;
            background: #333;
            background-image: linear-gradient(to right, #ccc, #333, #ccc);
        }
        h3 {
            text-align: center;
        }
        p {
            text-align: center;
        }
        p img {
            margin: 0 10px;
        }
    </style>
""", unsafe_allow_html=True)


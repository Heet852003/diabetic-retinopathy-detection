import streamlit as st
import pickle
from PIL import Image
import numpy as np
import os

# Load the trained model
with open('diabetic_retinopathy_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app title
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
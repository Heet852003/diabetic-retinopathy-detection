import streamlit as st
import pickle
from PIL import Image
import numpy as np
import base64

# Load the trained model
with open('diabetic_retinopathy_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Function to encode image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Set page configuration with custom favicon and layout
im = Image.open('logo.png')
st.set_page_config(page_title="Diabetic Retinopathy Detection", page_icon=im, layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Background Color */
        body {
            background-color: #f0f4fa;
        }
        
        /* Button Styles */
        div.stButton > button {
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
        }
        
        div.stButton > button:hover {
            background-color: #0056b3;
        }
        
        /* Center logo and title */
        h1 {
            text-align: center;
            color: #003366;
        }
        
        /* Image uploader styling */
        .stFileUploader label {
            color: #007bff;
        }

        /* Contact section styling */
        hr {
            border: 0;
            height: 1px;
            background: #333;
            background-image: linear-gradient(to right, #ccc, #333, #ccc);
        }
        h3 {
            text-align: center;
            color: #003366;
        }
        p {
            text-align: center;
        }
        p img {
            margin: 0 10px;
        }

        /* Animated shapes */
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0px); }
        }

        .floating-shape {
            position: absolute;
            width: 50px;
            height: 50px;
            background-color: #007bff;
            border-radius: 50%;
            animation: float 4s ease-in-out infinite;
            opacity: 0.6;
        }
    </style>
""", unsafe_allow_html=True)

# Inject animated shapes
st.markdown("""
    <div class="floating-shape" style="top: 20px; left: 80px;"></div>
    <div class="floating-shape" style="top: 150px; right: 50px;"></div>
""", unsafe_allow_html=True)

# Display logo at the top
logo_base64 = get_base64_image('logo.png')
st.markdown(f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{logo_base64}' width='100' height='100'/>
    </div>
""", unsafe_allow_html=True)

# App title
st.title('Diabetic Retinopathy Detection')

# Image input section
st.subheader("Upload Retinal Image:")
uploaded_file = st.file_uploader("Choose a retinal image...", type=["jpg", "png"])

# Side-by-side layout for image and prediction
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img = img.resize((224, 224))  # Resize to match model input
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = img_array.reshape(1, -1)  # Reshape for model input

    # Show the uploaded image in one column, and the predict button in another
    col1, col2 = st.columns([1, 1])

    with col1:
        # Display the uploaded image
        st.markdown(f"""
            <div style='text-align: center;'>
                <img src='data:image/png;base64,{base64.b64encode(uploaded_file.getvalue()).decode()}' width='300' height='300'/>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        # Predict button
        if st.button('Predict'):
            prediction = model.predict(img_array)
            st.write(f'**Prediction:** {"Diabetic Retinopathy Detected" if prediction[0] != 0 else "No Diabetic Retinopathy"}')

# Contact section with social media icons
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
            <img src="https://img.icons8.com/?size=100&id=12623&format=png&color=FFFFFF" width="30" height="30">
        </a>
    </p>
""", unsafe_allow_html=True)

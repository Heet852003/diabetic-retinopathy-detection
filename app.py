import streamlit as st
import pickle
from PIL import Image
import numpy as np
import base64

# Load the trained model
with open('diabetic_retinopathy_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Set page configuration with custom favicon and layout
im = Image.open('logo.png')
st.set_page_config(page_title="Diabetic Retinopathy Detection", page_icon=im, layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Body and font */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f0f4fa !important;
            text-align: center;
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

        /* Welcome message typing effect */
        .typing-demo {
            width: 40ch;  /* Adjusted width for full sentence */
            animation: typing 3s steps(40), blink 0.5s step-end infinite alternate;
            white-space: nowrap;
            overflow: hidden;
            border-right: 3px solid;
            font-size: 22px;
            font-weight: bold;
            color: #003366;
            text-align: center;
            margin-top: 20px;
        }
        
        @keyframes typing {
            from { width: 0 }
            to { width: 40ch }
        }
        
        @keyframes blink {
            50% { border-color: transparent }
        }

        /* Central alignment for all content */
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            text-align: center;
        }

        /* Fix for contact section icons */
        p img {
            background-color: #007bff;  /* Blue background for white logos */
            border-radius: 50%;
            padding: 5px;
            margin: 0 10px;
        }

        /* Sidebar styling */
        .css-1d391kg {
            background-color: #007bff;
            color: white;
            border-radius: 10px;
            padding: 15px;
        }

        .css-1d391kg .css-1vbd788 {
            font-weight: bold;
            font-size: 18px;
            text-transform: uppercase;
        }

        .css-1vbd788:hover {
            background-color: #0056b3;
            transition: 0.3s;
        }

        /* Moving Shapes */
        @keyframes float {
            0% { transform: translate(0, 0); }
            50% { transform: translate(20px, -30px); }
            100% { transform: translate(0, 0); }
        }
        
        .floating-shape {
            position: absolute;
            width: 80px;
            height: 80px;
            background-color: rgba(0, 123, 255, 0.3);
            border-radius: 50%;
            animation: float 10s infinite ease-in-out;
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
        }

        /* Random directions for shapes */
        .floating-shape-1 { top: 100px; left: 50px; animation-duration: 12s; animation-delay: 0s; }
        .floating-shape-2 { top: 200px; right: 100px; animation-duration: 8s; animation-delay: 1s; }
        .floating-shape-3 { bottom: 150px; left: 30px; animation-duration: 10s; animation-delay: 2s; }
        .floating-shape-4 { top: 300px; right: 200px; animation-duration: 15s; animation-delay: 1.5s; }
        .floating-shape-5 { bottom: 50px; right: 80px; animation-duration: 20s; animation-delay: 0.5s; }

    </style>
""", unsafe_allow_html=True)

# Inject moving shapes
st.markdown("""
    <div class="floating-shape floating-shape-1"></div>
    <div class="floating-shape floating-shape-2"></div>
    <div class="floating-shape floating-shape-3"></div>
    <div class="floating-shape floating-shape-4"></div>
    <div class="floating-shape floating-shape-5"></div>
""", unsafe_allow_html=True)

# Display the logo using Streamlit's st.image method
st.image('logo.png', width=120)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Upload Image", "Contact"])

# Welcome message with typing effect
if page == "Home":
    st.markdown("""
        <div class="typing-demo">
            Welcome to Diabetic Retinopathy Detection
        </div>
    """, unsafe_allow_html=True)

# About section
if page == "About":
    st.title("About This Application")
    st.write("""
        This application is designed to assist in the detection of Diabetic Retinopathy from retinal images. 
        Using machine learning, the system analyzes uploaded images and predicts whether diabetic retinopathy is present. 
        Diabetic retinopathy is a serious condition caused by damage to the blood vessels in the retina due to high blood sugar levels, which can lead to vision loss if left untreated.
    """)

# Upload Image Section
if page == "Upload Image":
    st.title("Diabetic Retinopathy Detection")
    
    # Image input section
    st.subheader("Upload Retinal Image:")
    uploaded_file = st.file_uploader("Choose a retinal image...", type=["jpg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        img = img.resize((224, 224))  # Resize to match model input
        img_array = np.array(img) / 255.0  # Normalize pixel values
        img_array = img_array.reshape(1, -1)  # Reshape for model input

        # Side-by-side layout for image and prediction
        col1, col2 = st.columns([1, 1])

        with col1:
            # Display the uploaded image
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        with col2:
            # Predict button
            if st.button('Predict'):
                prediction = model.predict(img_array)
                st.write(f'**Prediction:** {"Diabetic Retinopathy Detected" if prediction[0] != 0 else "No Diabetic Retinopathy"}')
                
                # Display advice based on prediction
                if prediction[0] != 0:
                    st.write("""
                        ### Medical Advice:
                        - Consult an ophthalmologist immediately.
                        - Control your blood sugar levels to prevent further damage.
                        - Regular eye exams are recommended for early detection and treatment.
                    """)
                else:
                    st.write("""
                        ### Medical Advice:
                        - Your retinal image shows no signs of diabetic retinopathy.
                        - Maintain a healthy lifestyle and have regular eye check-ups.
                    """)

# Contact section
if page == "Contact":
    st.title("Contact Me")
    st.markdown("""
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

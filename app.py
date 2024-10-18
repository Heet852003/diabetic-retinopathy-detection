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
        /* Body and font */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f0f4fa !important;
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
            width: 22ch;
            animation: typing 2s steps(22), blink 0.5s step-end infinite alternate;
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
            to { width: 22ch }
        }
        
        @keyframes blink {
            50% { border-color: transparent }
        }

        /* Moving Shapes */
        @keyframes float {
            0% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
            100% { transform: translateY(0px) rotate(360deg); }
        }
        
        .floating-shape {
            position: absolute;
            width: 80px;
            height: 80px;
            background-color: rgba(0, 123, 255, 0.3);
            border-radius: 50%;
            animation: float 6s ease-in-out infinite;
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
        }
        
        .floating-shape-1 {
            top: 100px;
            left: 50px;
        }

        .floating-shape-2 {
            top: 200px;
            right: 100px;
        }
        
        /* Contact section logo visibility fix */
        p img {
            background-color: #007bff;
            border-radius: 50%;
            padding: 5px;
            margin: 0 10px;
        }
        
        h1 {
            text-align: center;
            color: #003366;
        }

    </style>
""", unsafe_allow_html=True)

# Inject moving shapes
st.markdown("""
    <div class="floating-shape floating-shape-1"></div>
    <div class="floating-shape floating-shape-2"></div>
""", unsafe_allow_html=True)

# Typing welcome message
st.markdown("""
    <div class="typing-demo">
        Welcome to Diabetic Retinopathy Detection
    </div>
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

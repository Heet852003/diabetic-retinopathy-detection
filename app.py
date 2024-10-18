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

# Custom CSS for styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #f8f9fa;
        color: #333;
    }
    .stApp {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 2rem;
    }
    .upload-container {
        border: 2px dashed #bdc3c7;
        border-radius: 5px;
        padding: 2rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton > button {
        background-color: #3498db;
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #2980b9;
    }
    .result {
        background-color: #ecf0f1;
        border-radius: 5px;
        padding: 1rem;
        margin-top: 2rem;
    }
    .result h3 {
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    .contact-section {
        text-align: center;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #bdc3c7;
    }
    .contact-section a {
        margin: 0 10px;
        text-decoration: none;
        color: #3498db;
    }
    .contact-section a:hover {
        color: #2980b9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title and logo
logo_base64 = get_base64_image('logo.png')
st.markdown(f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{logo_base64}' width='100' height='100'/>
        <h1>Diabetic Retinopathy Detection</h1>
    </div>
""", unsafe_allow_html=True)

# File uploader with custom styling
st.markdown("<div class='upload-container'>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose a retinal image...", type=["jpg", "png"])
st.markdown("</div>", unsafe_allow_html=True)

if uploaded_file is not None:
    # Load and preprocess the image
    img = Image.open(uploaded_file)
    img = img.resize((224, 224))  # Resize to match model input
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = img_array.reshape(1, -1)  # Reshape for model input

    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

    # Button for prediction
    if st.button('Predict'):
        prediction = model.predict(img_array)[0]

        # Mapping predictions to stages and messages
        results = {
            0: ("No Diabetic Retinopathy detected.", "Maintain regular eye check-ups.", ""),
            1: ("Mild Diabetic Retinopathy detected.", "Consider lifestyle changes such as diet and exercise.", "Consult an ophthalmologist for further evaluation."),
            2: ("Moderate Diabetic Retinopathy detected.", "Regular monitoring is essential.", "Discuss treatment options with your healthcare provider."),
            3: ("Severe Diabetic Retinopathy detected.", "Immediate medical attention is required.", "Follow up with a specialist urgently."),
            4: ("Proliferative Diabetic Retinopathy detected.", "Urgent intervention is necessary.", "Seek treatment from a retinal specialist immediately.")
        }

        result_message, suggestions, remedy = results.get(prediction, ("Unable to determine.", "Please consult with a healthcare professional.", ""))

        # Display results in a styled container
        st.markdown('<div class="result">', unsafe_allow_html=True)
        st.success(result_message)
        st.markdown(f"### Suggestions:\n{suggestions}")
        if remedy:
            st.markdown(f"### Remedies:\n{remedy}")
        st.markdown('</div>', unsafe_allow_html=True)

# Contact Me section
st.markdown("""
    <div class="contact-section">
        <h3>Contact Me</h3>
        <a href="https://github.com/Heet852003" target="_blank">GitHub</a>
        <a href="https://www.linkedin.com/in/heet-mehta-41b862225" target="_blank">LinkedIn</a>
        <a href="mailto:mehtaheet5@gmail.com">Email</a>
    </div>
""", unsafe_allow_html=True)

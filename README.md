# 👁️ **Diabetic Retinopathy Detection**
### 🔍 **AI-Based Early Diagnosis System for Retinal Health Monitoring**

![Python](https://img.shields.io/badge/Python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=tensorflow&logoColor=white)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-%23E34F26.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

---

## 📄 **Overview**

The **Diabetic Retinopathy Detection** project is an AI-powered solution aimed at facilitating early diagnosis of diabetic retinopathy through image-based analysis. Leveraging the power of **Convolutional Neural Networks (CNN)** and **Deep Learning** frameworks, the system analyzes retinal images to detect various stages of diabetic retinopathy, thus aiding in timely intervention and treatment.

This project uses a comprehensive dataset of retinal fundus images and implements a multi-layered CNN architecture to achieve high accuracy in identifying symptoms such as microaneurysms, hemorrhages, and exudates. The model is hosted on a web interface, enabling healthcare professionals to upload retinal images and receive instant diagnostic results.

---

## ✨ **Key Features**

- **🔹 Automated Diagnosis**  
  Automatically classifies retinal images into different stages of diabetic retinopathy, minimizing the need for manual examination.

- **🔹 CNN-Based Model**  
  A well-trained Convolutional Neural Network with multiple layers for feature extraction and classification.

- **🔹 Web-Based Interface**  
  A user-friendly web interface where users can upload images, view results, and understand the diagnostic confidence levels.

- **🔹 Interactive Visualizations**  
  Generates heatmaps and overlay visualizations to highlight areas of concern in the retinal images.

- **🔹 Cloud Hosting**  
  Hosted on a cloud platform for remote access, with support for real-time data processing.

---

## 🛠️ **Tech Stack**

- **Programming Language:**  
  ![Python](https://img.shields.io/badge/Python-3.8-blue.svg?style=for-the-badge&logo=python&logoColor=white)  
  Used for implementing the model and backend functionalities.

- **Frameworks:**  
  ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0-orange.svg?style=for-the-badge&logo=tensorflow&logoColor=white)  
  The primary library for building and training the deep learning model.  

  ![Keras](https://img.shields.io/badge/Keras-2.4.3-red.svg?style=for-the-badge&logo=keras&logoColor=white)  
  Used for constructing the neural network layers and model management.

- **Frontend & Hosting:**  
  ![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-red?style=for-the-badge&logo=streamlit)  
  ![Heroku](https://img.shields.io/badge/Heroku-Deployed-blueviolet.svg?style=for-the-badge&logo=heroku)  
  Streamlit is used for building the web interface, and the application is hosted on Heroku for easy access and scalability.

- **Libraries Used:**  
  - `NumPy`  
  - `Pandas`  
  - `OpenCV`  
  - `Matplotlib`

---

## 🚀 **Getting Started**

### Prerequisites
Before you begin, ensure you have the following installed on your local machine:
- Python 3.8 or above
- TensorFlow and Keras libraries
- Streamlit for the web interface

### Installation
Follow the steps below to set up the project on your local environment:

1. **Navigate to the Project Directory:**
   ```bash
   cd diabetic-retinopathy-detection
2. **Install Dependencies: Install the necessary dependencies using the requirements.txt file**
   ```bash
   pip install -r requirements.txt
   
3. **Run the Application: Launch the Streamlit app locally.**
   ```bash
   streamlit run app.py

4. **Access the Interface: Open your web browser and go to the following URL to interact with the application**
   ```bash
   http://localhost:8501

---


## 📊 **Model Performance**
The model achieves an accuracy of 85% on the validation dataset and a precision of 88%. The results are visualized using confusion matrices and ROC curves, providing a clear understanding of the model's classification performance. The model has been fine-tuned to minimize false negatives, ensuring reliable predictions and robust detection of diabetic retinopathy stages.

---


## 📋 **Future Enhancements**

- 🌟 **Implement Hybrid Models:**
Integrate a hybrid model combining CNNs with RNNs to capture temporal dependencies for more comprehensive analysis.
- 🌟 **Expand Diagnostic Scope:**
Extend the model's capabilities to include detection of other retinal conditions such as glaucoma and macular degeneration.
- 🌟 **Enhanced Web Interface:**
Upgrade the web interface with more interactive diagnostic insights and patient management features, making it a one-stop solution for retinal health monitoring.

---


## 🤝 **Contributing**
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or create a pull request. Let's collaborate to make this project even better!

---


## 📬 **Contact**
For any inquiries or suggestions, please feel free to reach out:

- **Name: Heet Mehta**
- **Email: mehtaheet5@gmail.com**
- **GitHub: Heet852003**




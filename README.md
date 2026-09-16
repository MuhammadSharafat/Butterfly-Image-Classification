# 🦋 Butterfly Vision AI

<p align="center">
  <strong>AI-powered butterfly species classification from images</strong>
</p>

<p align="center">
  <a href="https://butterfly-image-classification-ms3rdvz5jwqvagpqrthedo.streamlit.app/">🌐 Live Demo</a>
  ·
  <a href="https://github.com/MuhammadSharafat/Butterfly-Image-Classification">📦 GitHub Repository</a>
</p>

# 📌 Overview

Butterfly Vision AI is a deep-learning image classification application that identifies butterfly species from an uploaded image.

The project uses a Convolutional Neural Network (CNN) for image classification and an ONNX Runtime model for fast inference. A user can upload a butterfly image through the Streamlit web interface and receive the predicted species along with its confidence score and the Top 5 predictions.

The current application supports 75 butterfly species.

# ✨ Features

 => 🦋 Butterfly species identification from images

 => 🤖 CNN-based image classification

 => ⚡ ONNX Runtime inference

 => 🌐 Interactive Streamlit web application

 => 📤 Supports JPG, JPEG, PNG, and WEBP images

 => 🎯 Displays the predicted species and confidence score

 => 📊 Shows the Top 5 model predictions

 => 💾 Uses a trained .onnx model for deployment

 =>🎨 Modern dark-themed user interface

# 🧠 How It Works

The application follows this pipeline:

Butterfly Image
      │
      ▼
Image Upload
      │
      ▼
RGB Conversion
      │
      ▼
Resize to 150 × 150
      │
      ▼
Normalize Pixel Values
      │
      ▼
CNN Model (ONNX)
      │
      ▼
Class Probabilities
      │
      ├──► Best Prediction
      │
      └──► Top 5 Predictions

# 🛠️ Technologies Used

Technology

Purpose

Python

Core programming language

TensorFlow / Keras

CNN model development and training

ONNX

Model deployment format

ONNX Runtime

Model inference

NumPy

Numerical and image-array processing

Pillow

Image loading and preprocessing

Streamlit

Web application and user interface

Jupyter Notebook

Model development and experimentation

# 📂 Project Structure

Butterfly-Image-Classification/
│
├── train/                                      # Training images
├── test/                                       # Testing images
│
├── Training_set.csv                            # Training dataset labels
├── Testing_set.csv                             # Testing dataset labels
│
├── butterfly-multiclass-image-classification-cnn.ipynb
│                                                # CNN training notebook
│
├── butterfly_model.onnx                        # Exported trained model
├── class_names.json                             # Butterfly class mapping
│
├── app.py                                      # Streamlit application
├── requirements.txt                            # Python dependencies
└── README.md                                   # Project documentation

# 🚀 Run Locally

1. Clone the repository

git clone https://github.com/MuhammadSharafat/Butterfly-Image-Classification.git
cd Butterfly-Image-Classification

2. Create a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

macOS / Linux:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run the Streamlit application

streamlit run app.py

The application will open in your browser at the local Streamlit address.

# 🌐 Live Demo

Try the deployed application:

https://butterfly-image-classification-ms3rdvz5jwqvagpqrthedo.streamlit.app/

# 🖼️ Using the Application

 1. Open the Butterfly Vision AI web application.

 2. Upload a butterfly image.

 3. Click Identify Species.

 4. The model processes the image.

 5. View the predicted butterfly species and confidence score.

 6. Check the Top 5 predictions for additional model outputs.

# 📊 Model Inference

For each uploaded image, the application:

 => Converts the image to RGB.

 => Resizes it to 150 × 150 pixels.

 => Normalizes pixel values to the range 0–1.

 => Sends the processed image to the ONNX model.

 => Sorts the model's class probabilities.

 => Displays the highest-probability species.

 => Displays the Top 5 predictions with confidence percentages.

# 📓 Model Development

The repository includes a Jupyter Notebook:

butterfly-multiclass-image-classification-cnn.ipynb

It contains the CNN-based multiclass butterfly image-classification workflow used to develop the model.

The trained model is exported to:

butterfly_model.onnx

The corresponding class labels are stored in:

class_names.json

# 📦 Dependencies

The deployed application uses:

Pillow
NumPy
ONNX Runtime
Streamlit

See requirements.txt for the project dependency list.

# 🔮 Future Improvements

Potential future improvements include:

 => 📈 Improving classification accuracy

 => 🔍 Adding more butterfly species

 => 📱 Improving mobile responsiveness

 => 📚 Adding detailed information about each species

 => 📷 Supporting camera-based image capture

 => 📊 Adding model performance metrics and confusion matrix

 => 🧠 Exploring stronger CNN architectures and transfer learning

 => ⚡ Further optimizing inference speed

# 👨‍💻 Author

Mohammad Sharafat Alam Saki

Computer Science & Technology

Project Links

 => GitHub: https://github.com/MuhammadSharafat/Butterfly-Image-Classification

 => Live Demo: https://butterfly-image-classification-ms3rdvz5jwqvagpqrthedo.streamlit.app/

<p align="center">
  🦋 <strong>Butterfly Vision AI</strong><br>
  Built with Python, CNN, ONNX Runtime & Streamlit
</p>

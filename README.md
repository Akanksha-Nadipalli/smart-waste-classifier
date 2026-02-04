<p align="center"> <img src="https://img.shields.io/badge/Smart%20Waste%20Classifier-Streamlit%20App-brightgreen?style=for-the-badge" /> </p> <p align="center"> <b>AI-Powered Waste Classification using Transfer Learning with MobileNetV2 </b><br/> Turning trash into structured data for smarter recycling ♻️ </p>

## 🚀 Live Demo

🔗 https://smart-waste-classifier-5sbkuevrfz8twxwx3ptdcc.streamlit.app/

## ♻️ Smart Waste Classification App

An end-to-end deep learning project that classifies waste images into six categories using a transfer-learned MobileNetV2 model and deploys it as an interactive Streamlit web app.

This project demonstrates:

• Computer Vision

• Transfer Learning

• Data Augmentation

• Model Deployment

• Real-time inference in a web UI

## 🧠 Problem Statement

Improper waste segregation is a major challenge in recycling systems. Manual sorting is inefficient and error-prone.

This project uses deep learning to automatically identify waste type from an image, enabling smarter recycling workflows and forming the foundation for smart bins / IoT-based waste systems.

🛠️ Tech Stack
<p align="left"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" /> <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" /> <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white" /> <img src="https://img.shields.io/badge/MobileNetV2-000000?style=for-the-badge&logo=google&logoColor=white" /> </p>

## ✨ Features

• Upload image or capture from camera

• Real-time waste classification

• Prediction confidence score

• Clean and responsive UI

• Transfer learning with data augmentation

• Deployable ML model as a web app

## 🗂️ Waste Categories

• The model predicts:

• Cardboard

• Glass

• Metal

• Paper

• Plastic

• Trash

## 🧠 Model Architecture

Transfer learning with MobileNetV2 pretrained on ImageNet.

Key techniques:

• Frozen convolutional base

• Custom classification head

• Extensive data augmentation

• Fine-tuning on waste dataset

• Softmax output for 6-class prediction

## 📊 Model Performance

Add your actual values here after training

Metric	Value
Training Accuracy	XX%
Validation Accuracy	XX%
Test Accuracy	XX%

Adding an accuracy graph and confusion matrix here will significantly boost project credibility.

## 📸 Screenshots

### Home Page
![Home](./screenshots/home.png)

### Classification Result
![Result1](./screenshots/result1.png)
![Result2](./screenshots/result2.png)

## Installation

1. Clone the repository:

```
git clone https://github.com/Akanksha-Nadipalli/smart-waste-classifier.git
```

2. Navigate to the folder:

```
cd smart-waste-classifier
```

3. Create a virtual environment (optional but recommended):

```
python -m venv env
source env/bin/activate # Linux/Mac
env\Scripts\activate # Windows
```

Install dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:

```
streamlit run app.py
```

Open the provided URL in your browser and start classifying waste.

## 🚀 Future Improvements

• Edge deployment on Raspberry Pi (Smart Bin)

• Add more waste categories

• Live video classification

• Model quantization for faster inference

• Integration with IoT sensors

## 📄 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this project with appropriate attribution.

See the [LICENSE](./LICENSE) file for full details.

<p align="center">
<img src="https://img.shields.io/badge/Smart%20Waste%20Classifier-Streamlit%20App-brightgreen?style=for-the-badge" />
</p>

<p align="center">
<b>AI-powered waste classification using MobileNetV2 + Streamlit</b>
</p>

## 🚀 Live Demo
🔗 https://smart-waste-classifier-5sbkuevrfz8twxwx3ptdcc.streamlit.app/

# ♻️ Smart Waste Classification App
A Streamlit-based web application that classifies waste into six categories using a MobileNetV2 deep learning model.
---

## Tech Stack  
<p align="left">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
<img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white" />
<img src="https://img.shields.io/badge/MobileNetV2-000000?style=for-the-badge&logo=google&logoColor=white" />
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
<img src="https://img.shields.io/badge/Pillow-007ACC?style=for-the-badge&logo=python&logoColor=white" />

</p>

## Features

- Upload an image of waste or take a photo using your camera
- Real-time waste classification
- User-friendly interface with clean styling
- Confidence score for predictions
- MobileNetV2 model with data augmentation
---

## Waste Categories

The model classifies images into the following classes:

- Cardboard

- Glass

- Metal

- Paper

- Plastic

- Trash

---

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

## 📸 Screenshots

### Home Page
![Home](./screenshots/home.png)

### Classification Result
![Result1](./screenshots/result1.png)
![Result2](./screenshots/result2.png)

## 🧠 Model Information

Model file: garbage_mobilenet_augmented.keras

Architecture: MobileNetV2 (pretrained on ImageNet)

Training: Includes extensive data augmentation for robustness

Output: Six waste categories with prediction probabilities

## 📄 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this project with appropriate attribution.

See the [LICENSE](./LICENSE) file for full details.

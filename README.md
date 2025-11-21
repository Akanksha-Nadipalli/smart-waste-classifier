# ♻️ Smart Waste Classification App

This is a **Streamlit web app** that classifies waste into six categories: cardboard, glass, metal, paper, plastic, and trash. The model is trained using **MobileNetV2** with data augmentation for better accuracy.

---

## Features

- Upload an image of waste or take a photo using your camera.
- Real-time classification of waste.
- User-friendly interface with clean styling.
- Confidence score for predictions.
- Fully open-source and ready for deployment.

---

## Installation

1. Clone the repository:

```
git clone https://github.com/<your-username>/waste-classifier.git
```

2. Navigate to the folder:

```
cd waste-classifier
```

3. Create a virtual environment (optional but recommended):

```
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
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
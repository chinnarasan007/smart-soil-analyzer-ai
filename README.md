# smart-soil-analyzer-ai
AI-powered soil classification and crop recommendation system using TensorFlow and Flask


# 🌱 Smart Soil Analyzer AI

An AI-powered web application that detects soil type using Deep Learning and recommends suitable crops, fertilizer suggestions, soil quality, and live weather information.

---

# 🚀 Features

✅ Soil Type Detection using Deep Learning
✅ Image Upload Support
✅ Crop Recommendation System
✅ Fertilizer Suggestion
✅ Soil Quality Analysis
✅ Live Weather Integration
✅ Season-Based Crop Recommendation
✅ Flask Web Application
✅ TensorFlow CNN Model

---

# 🧠 Technologies Used

* Python
* Flask
* TensorFlow / Keras
* OpenCV
* NumPy
* HTML / CSS
* JavaScript
* OpenWeather API

---

# 📂 Project Structure

```bash
Project/
│
├── app.py
├── recommendation.py
├── location.py
├── weather.py
├── train_model.py
├── requirements.txt
├── class_names.json
├── best_model.h5
├── soil_model.h5
│── screenshot/
    └── home.png
    └── result.png
├── static/
│   └── uploads/
├── templates/
├── .gitignore

```

---

# ⚙️ How It Works

1. User uploads a soil image
2. Deep Learning model predicts soil type
3. Weather API fetches live weather
4. System analyzes:

   * Soil type
   * Temperature
   * Humidity
   * Season
5. Application recommends:

   * Suitable crops
   * Fertilizer
   * Soil quality

---

# 🧪 Soil Classes Supported

* Alluvial Soil
* Black Soil
* Red Soil
* Laterite Soil
* Arid Soil
* Mountain Soil
* Yellow Soil
* Non Soil Detection

---

# 🧠 Deep Learning Model

The project uses a custom CNN architecture inspired by VGG-style networks.

### Model Features

* Data Augmentation
* Batch Normalization
* Dropout Regularization
* Early Stopping
* ReduceLROnPlateau
* Model Checkpointing
* Class Weight Balancing

---

# 📸 Image Prediction Flow

```python
Image Upload
     ↓
Preprocessing
     ↓
CNN Model Prediction
     ↓
Soil Classification
     ↓
Crop Recommendation
```

---

# 🌦 Weather Integration

The project fetches live weather data using OpenWeather API.

Weather Details:

* Temperature
* Humidity
* Weather Condition

These values are used for better crop recommendation.

---

# 🌱 Crop Recommendation Logic

Recommendations are generated based on:

* Soil Type
* Temperature
* Humidity
* Farming Season

Supported Seasons:

* Kharif
* Rabi
* Zaid

---

# 💻 Installation Guide

## Step 1 — Clone Repository

```bash
git clone https://github.com/chinnarasan007/smart-soil-analyzer-ai
```

---

## Step 2 — Open Project

```bash
cd smart-soil-analyzer-ai
```

---

## Step 3 — Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 4 — Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Step 5 — Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

# 📦 Requirements

Example packages:

```txt
flask
tensorflow
opencv-python
numpy
requests
matplotlib
scikit-learn
```

---

# 🔑 API Configuration

Add your OpenWeather API key inside:

```python
weather.py
```

Example:

```python
api_key = "YOUR_API_KEY"
```

Get free API key from:

https://openweathermap.org/api

---

# 📊 Model Training

To retrain model:

```bash
python train_model.py
```

The model automatically saves:

* best_model.h5
* soil_model.h5
* class_names.json

---

# 📷 Screenshots

## Home Page

![Home Page](screenshots/home.png)

## Result Page

![Result Page](screenshots/result.png)

---

# 🌍 Future Improvements

* Mobile App Integration
* Fertilizer Marketplace
* Multi-language Support
* Satellite Soil Analysis
* IoT Sensor Integration
* Disease Detection Module

---

# 👨‍💻 Author

Chinnarajan M
Aspiring Data Scientist
---

# 📜 License

This project is developed for educational and research purposes.

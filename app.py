from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import cv2
import os
import time
import json

from recommendation import *
from weather import get_weather

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ✅ LOAD BEST MODEL
model = tf.keras.models.load_model("best_model.h5")

# ✅ LOAD CLASS LABELS
with open("class_names.json") as f:
    class_indices = json.load(f)

class_labels = {v: k for k, v in class_indices.items()}


# ---------------- IMAGE PREDICTION ----------------
def predict_image(path):
    img = cv2.imread(path)

    if img is None:
        return "Invalid", 0.0

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img, verbose=0)[0]

    class_index = int(np.argmax(pred))
    confidence = float(np.max(pred))

    soil = class_labels[class_index]

    if soil == "Non_Soil" or confidence < 0.65:
        return "Invalid", confidence

    return soil, confidence


# ---------------- ROUTE ----------------
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        city = request.form.get("city")
        file = request.files['image']

        # ✅ CREATE FILENAME FIRST
        filename = f"{int(time.time())}_{file.filename}"

        # ✅ SAVE IMAGE
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)

        # ✅ CORRECT IMAGE PATH FOR HTML 
        img_path = f"uploads/{filename}"

        soil, confidence = predict_image(path)

        # ---------------- INVALID ----------------
        if soil == "Invalid":
            return render_template(
                "result.html",
                soil="Invalid Image",
                crops=[],
                fertilizer="N/A",
                quality="N/A",
                temp=0,
                humidity=0,
                weather="Invalid",
                city=city,
                region="India",
                img_path=img_path,   # ✅ FIXED
                confidence=round(confidence * 100, 2),
                season="N/A"
            )

        # ---------------- VALID ----------------
        temp, humidity, weather = get_weather(city)

        crops = recommend_crop(soil, temp, humidity)
        fert = fertilizer_suggestion(soil, temp, humidity)
        quality = soil_quality(soil, temp, humidity)
        season = get_season()

        return render_template(
            "result.html",
            soil=soil,
            crops=crops,
            fertilizer=fert,
            quality=quality,
            temp=temp,
            humidity=humidity,
            weather=weather,
            city=city,
            region="India",
            img_path=img_path,   # ✅ FIXED
            confidence=round(confidence * 100, 2),
            season=season
        )

    return render_template("index.html")



# ---------------- START SERVER ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Running on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
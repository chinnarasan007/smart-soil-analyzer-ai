from datetime import datetime

# ---------------- SEASON DETECTION ----------------
def get_season():
    month = datetime.now().month

    if month in [6,7,8,9]:
        return "Kharif"
    elif month in [10,11,12,1,2]:
        return "Rabi"
    else:
        return "Zaid"

# ---------------- CROP RECOMMENDATION ----------------
def recommend_crop(soil_type, temp, humidity):

    if soil_type in ["Non_Soil", "Invalid"]:
        return ["Invalid Soil Image"]

    season = get_season()
    crops = []

    if soil_type == "Alluvial_Soil":
        crops = ["Rice","Sugarcane"] if season=="Kharif" else ["Wheat","Maize"]

    elif soil_type == "Black_Soil":
        crops = ["Cotton","Soybean"] if season=="Kharif" else ["Groundnut","Wheat"]

    elif soil_type == "Red_Soil":
        crops = ["Millets","Pulses"]
        if humidity < 60:
            crops.append("Groundnut")

    elif soil_type == "Laterite_Soil":
        crops = ["Tea","Coffee"] if humidity>70 else ["Cashew"]

    elif soil_type == "Arid_Soil":
        crops = ["Millets","Barley"]
        if temp > 30:
            crops.append("Maize")

    elif soil_type == "Mountain_Soil":
        crops = ["Tea","Spices","Apple"]

    elif soil_type == "Yellow_Soil":
        crops = ["Pulses","Oilseeds","Maize"]

    return list(set(crops)) if crops else ["No crop found"]


# ---------------- FERTILIZER ----------------
def fertilizer_suggestion(soil_type, temp, humidity):

    if soil_type in ["Non_Soil", "Invalid"]:
        return "Not Applicable"

    mapping = {
        "Alluvial_Soil":"Nitrogen-rich fertilizer",
        "Black_Soil":"Phosphorus-rich fertilizer",
        "Red_Soil":"Organic compost + Potassium",
        "Laterite_Soil":"Lime + Organic fertilizer",
        "Arid_Soil":"Moisture-retaining fertilizer",
        "Mountain_Soil":"Organic manure",
        "Yellow_Soil":"Balanced NPK fertilizer"
    }

    return mapping.get(soil_type,"General fertilizer")


# ---------------- SOIL QUALITY ----------------
def soil_quality(soil_type, temp, humidity):

    if soil_type in ["Non_Soil","Invalid"]:
        return "Invalid"

    base = {
        "Alluvial_Soil":8,
        "Black_Soil":9,
        "Red_Soil":6,
        "Laterite_Soil":4,
        "Arid_Soil":3,
        "Mountain_Soil":6,
        "Yellow_Soil":5
    }.get(soil_type,5)

    if humidity > 70:
        base += 1
    if temp > 35:
        base -= 1

    if base >= 8: return "Very High"
    elif base >= 6: return "High"
    elif base >= 4: return "Medium"
    else: return "Low"
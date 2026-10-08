from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from datetime import datetime

app = Flask(__name__)

# Load model
with open("final_model_cat.pkl", "rb") as f:
    model = pickle.load(f)

# Haversine distance calculator
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    return R * 2 * np.arcsin(np.sqrt(a))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        pickup_lat  = float(data["pickup_lat"])
        pickup_lon  = float(data["pickup_lon"])
        dropoff_lat = float(data["dropoff_lat"])
        dropoff_lon = float(data["dropoff_lon"])
        passengers  = int(data["passengers"])
        datetime_str = data["datetime"]          # "YYYY-MM-DDTHH:MM"

        dt = datetime.fromisoformat(datetime_str)
        hour      = dt.hour
        day       = dt.day
        month     = dt.month
        year      = dt.year
        dayofweek = dt.weekday()   # 0=Mon … 6=Sun

        # Feature order must match training:
        # pickup_longitude, pickup_latitude, dropoff_longitude,
        # dropoff_latitude, passenger_count, hour, day, month, year, dayofweek
        features = np.array([[
            pickup_lon, pickup_lat,
            dropoff_lon, dropoff_lat,
            passengers,
            hour, day, month, year, dayofweek
        ]])

        fare = float(model.predict(features)[0])
        fare = max(2.5, round(fare, 2))   # floor at base fare

        distance_km = round(haversine(pickup_lat, pickup_lon, dropoff_lat, dropoff_lon), 2)
        est_minutes = round((distance_km / 30) * 60)   # ~30 km/h city speed

        return jsonify({
            "fare": fare,
            "fare_range_low":  round(fare * 0.90, 2),
            "fare_range_high": round(fare * 1.10, 2),
            "distance_km": distance_km,
            "est_minutes": est_minutes
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)

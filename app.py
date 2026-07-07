import sqlite3
import joblib
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
model = joblib.load("models/disaster_model.pkl")

API_KEY = "bca046d77051fc0999a04255806f90e6"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():

    city = request.form["city"]

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

   
    if data["cod"] != 200:
        return "City Not Found"

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["main"]

    return f"""
    <h2>Weather Report</h2>

    <p><b>City :</b> {city}</p>

    <p><b>Temperature :</b> {temperature} °C</p>

    <p><b>Humidity :</b> {humidity}%</p>

    <p><b>Weather :</b> {weather}</p>

    <a href="/">⬅ Back</a>
    """
@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        rainfall = float(request.form["rainfall"])

        result = model.predict([[temperature, humidity, rainfall]])

        conn = sqlite3.connect("database/disaster.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO prediction (temperature, humidity, rainfall, risk) VALUES (?, ?, ?, ?)",
            (temperature, humidity, rainfall, result[0])
        )

        conn.commit()
        conn.close()

        return "Risk : " + result[0]

    return render_template("predict.html")
@app.route("/history")
def history():

    conn = sqlite3.connect("database/disaster.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM prediction")

    data = cursor.fetchall()

    conn.close()

    return render_template("history.html", data=data)
@app.route("/emergency")
def emergency():
    return render_template("emergency.html")
@app.route("/safety")
def safety():
    return render_template("safety.html")

@app.route("/alerts")
def alerts():

    cities = [
        "Mumbai",
        "Pune",
        "Nagpur",
        "Nashik",
        "Kolhapur",
        "Satara",
        "Solapur",
        "Aurangabad",
        "Amravati",
        "Thane"
    ]

    alerts = []

    for city in cities:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            continue

        temp = data["main"]["temp"]
        weather = data["weather"][0]["main"]

        if weather in ["Rain", "Thunderstorm"]:
            level = "🔶 Orange Alert"

        elif temp >= 40:
            level = "🔴 Heatwave Alert"

        else:
            level = "🟢 Normal"

        alerts.append({
            "city": city,
            "temp": temp,
            "weather": weather,
            "level": level
        })

    return render_template("alerts.html", alerts=alerts)

@app.route("/map")

def map():

  return render_template("map.html")

@app.route("/reports")

def reports():

  return render_template("reports.html")

if __name__ == "__main__":
    app.run(debug=True)
import joblib

# Model Load 
model = joblib.load("models/disaster_model.pkl")

# Sample Data
temperature = 32
humidity = 85
rainfall = 70

# Prediction
result = model.predict([[temperature, humidity, rainfall]])

print("Risk :", result[0])
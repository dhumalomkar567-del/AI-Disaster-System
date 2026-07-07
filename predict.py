<<<<<<< HEAD
import joblib

# Model Load 
model = joblib.load("models/disaster_model.pkl")

# Sample Data
temperature = 32
humidity = 85
rainfall = 70

# Prediction
result = model.predict([[temperature, humidity, rainfall]])

=======
import joblib

# Model Load 
model = joblib.load("models/disaster_model.pkl")

# Sample Data
temperature = 32
humidity = 85
rainfall = 70

# Prediction
result = model.predict([[temperature, humidity, rainfall]])

>>>>>>> 8bf753ab96844de6f412956b5129f8d13d0c50c5
print("Risk :", result[0])
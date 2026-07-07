import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib


data = pd.read_csv("data/disaster_dataset.csv")

X = data[["Temperature", "Humidity", "Rainfall"]]

y = data["Risk"]

model = DecisionTreeClassifier()

model.fit(X, y)

joblib.dump(model, "models/disaster_model.pkl")

print("Model Trained Successfully")
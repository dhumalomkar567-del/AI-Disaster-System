<<<<<<< HEAD
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib


data = pd.read_csv("data/disaster_dataset.csv")

X = data[["Temperature", "Humidity", "Rainfall"]]

y = data["Risk"]

model = DecisionTreeClassifier()

model.fit(X, y)

joblib.dump(model, "models/disaster_model.pkl")

=======
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib


data = pd.read_csv("data/disaster_dataset.csv")

X = data[["Temperature", "Humidity", "Rainfall"]]

y = data["Risk"]

model = DecisionTreeClassifier()

model.fit(X, y)

joblib.dump(model, "models/disaster_model.pkl")

>>>>>>> 8bf753ab96844de6f412956b5129f8d13d0c50c5
print("Model Trained Successfully")
import matplotlib.pyplot as plt

risk = ["Low", "Medium", "High"]
count = [5, 3, 7]

plt.bar(risk, count)

plt.title("Disaster Prediction")

plt.xlabel("Risk")

plt.ylabel("Count")

plt.show()
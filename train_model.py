# train_model.py
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
import os

# Dummy dataset
data = {
    "math": [90, 45, 78, 88, 56, 34, 90],
    "science": [85, 42, 80, 70, 50, 30, 95],
    "english": [75, 40, 72, 85, 60, 33, 80],
    "pass": [1, 0, 1, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

X = df[["math", "science", "english"]]
y = df["pass"]

model = LogisticRegression()
model.fit(X, y)

os.makedirs("model", exist_ok=True)
with open("model/student_model.pkl", "wb") as f:
    pickle.dump(model, f)

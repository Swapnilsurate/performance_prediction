# predictor/predict_model.py
import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Dummy dataset
X = np.array([
    [60, 70, 80],
    [30, 40, 50],
    [90, 88, 92],
    [20, 35, 45],
    [75, 65, 60],
])
y = [1, 0, 1, 0, 1]  # 1 = Pass, 0 = Fail

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model
with open("student_model.pkl", "wb") as f:
    pickle.dump(model, f)
# predictor/predict_model.py (add below existing code)
def predict_pass_status(math, science, english):
    with open("student_model.pkl", "rb") as f:
        model = pickle.load(f)
    data = [[math, science, english]]
    result = model.predict(data)
    return "Pass" if result[0] == 1 else "Fail"

import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

def test_model_accuracy():
    model = joblib.load("diabetes_model.pkl")
    df = pd.read_csv("diabetes.csv")
    X = df[["Pregnancies", "Glucose", "BloodPressure", "BMI", "Age"]]
    y = df["Outcome"]
    y_pred = model.predict(X)
    assert accuracy_score(y, y_pred) > 0.7  # Ensure reasonable accuracy

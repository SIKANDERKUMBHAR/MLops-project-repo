import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import mlflow
import mlflow.sklearn

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv")
X = df[["Pregnancies", "Glucose", "BloodPressure", "BMI", "Age"]]
y = df["Outcome"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and log to MLflow
with mlflow.start_run():
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_param("model_type", "RandomForestClassifier")
    mlflow.sklearn.log_model(model, "diabetes_model")
    print(f"✅ Accuracy: {accuracy}")
    print("✅ Classification Report:\n", classification_report(y_test, y_pred))
    joblib.dump(model, "diabetes_model.pkl")  # For compatibility
    print("✅ Model saved as diabetes_model.pkl")

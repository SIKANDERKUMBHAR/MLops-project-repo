from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={
        "Pregnancies": 2,
        "Glucose": 130,
        "BloodPressure": 70,
        "BMI": 28.5,
        "Age": 45
    })
    assert response.status_code == 200
    assert "diabetic" in response.json()

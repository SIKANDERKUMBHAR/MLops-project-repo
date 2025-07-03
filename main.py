from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
import joblib
import numpy as np

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

try:
    model = joblib.load("diabetes_model.pkl")
except Exception as e:
    raise Exception(f"Failed to load model: {str(e)}")

class DiabetesInput(BaseModel):
    Pregnancies: int = Field(ge=0)
    Glucose: float = Field(ge=0)
    BloodPressure: float = Field(ge=0)
    BMI: float = Field(ge=0)
    Age: int = Field(ge=0)

@app.get("/")
def read_root():
    return {"message": "Diabetes Prediction API is live"}

@app.post("/predict")
def predict(data: DiabetesInput):
    try:
        input_data = np.array([[data.Pregnancies, data.Glucose, data.BloodPressure, data.BMI, data.Age]])
        prediction = model.predict(input_data)[0]
        return {"diabetic": bool(prediction)}
    except Exception as e:


@app.get("/health")
def health():
    return {"status": "healthy"}

raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

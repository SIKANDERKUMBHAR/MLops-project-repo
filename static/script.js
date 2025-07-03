document.getElementById('prediction-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {
        Pregnancies: parseInt(document.getElementById('pregnancies').value),
        Glucose: parseFloat(document.getElementById('glucose').value),
        BloodPressure: parseFloat(document.getElementById('bloodpressure').value),
        BMI: parseFloat(document.getElementById('bmi').value),
        Age: parseInt(document.getElementById('age').value)
    };
    try {
        const response = await fetch('http://localhost:8000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        document.getElementById('result').innerText = result.diabetic
            ? 'Prediction: Diabetic'
            : 'Prediction: Not Diabetic';
    } catch (error) {
        document.getElementById('result').innerText = 'Error: Could not get prediction';
    }
});

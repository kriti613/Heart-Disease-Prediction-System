from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the model
model_filename = 'rf_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    form_data = request.form
    input_features = [
        int(form_data['age']),
        int(form_data['sex']),
        int(form_data['cp']),
        int(form_data['trestbps']),
        int(form_data['chol']),
        int(form_data['fbs']),
        int(form_data['restecg']),
        int(form_data['thalach']),
        int(form_data['exang']),
        float(form_data['oldpeak']),
        int(form_data['slope']),
        int(form_data['ca']),
        int(form_data['thal'])
    ]

    # Make prediction and calculate probability
    input_features = np.array(input_features).reshape(1, -1)
    prediction = model.predict(input_features)[0]
    probabilities = model.predict_proba(input_features)[0]  # Get probabilities for classes

    # Extract probabilities
    prob_heart_disease = probabilities[1] * 100  # Probability for class "1" (Heart Disease)
    prob_no_disease = probabilities[0] * 100    # Probability for class "0" (No Disease)

    # Determine result message
    result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease Detected"

    return render_template(
        'result.html', 
        result=result, 
        prob_heart_disease=prob_heart_disease, 
        prob_no_disease=prob_no_disease
    )

if __name__ == '__main__':
    app.run(debug=True)

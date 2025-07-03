from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

model = joblib.load("income_model.pkl")
label_encoders = joblib.load("encoders.pkl")

occupation_le = label_encoders['Occupation']
housetype_le = label_encoders['HouseType']
education_le = label_encoders['Education']
area_le = label_encoders['Area']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        family_size = int(request.form['Family_size'])
        occupation = request.form['Occupation']
        house_type = request.form['HouseType']
        vehicles = int(request.form['Vehicles'])
        electricity = int(request.form['ElectricityBill'])
        education = request.form['Education']
        area = request.form['Area']

        occupation_enc = occupation_le.transform([occupation])[0]
        housetype_enc = housetype_le.transform([house_type])[0]
        education_enc = education_le.transform([education])[0]
        area_enc = area_le.transform([area])[0]

        features = np.array([[family_size, occupation_enc, housetype_enc, vehicles, electricity, education_enc, area_enc]])
        prediction_enc = model.predict(features)[0]

        bracket_le = label_encoders['Bracket']
        prediction_label = bracket_le.inverse_transform([prediction_enc])[0]

        return render_template('result.html', prediction=prediction_label)

    except Exception as e:
        return f"Error: {str(e)}"

# ✅ This must be outside the predict() function
if __name__ == "__main__":
    app.run(debug=True)

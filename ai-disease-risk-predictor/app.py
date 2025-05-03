from flask import Flask, render_template, request

app = Flask(__name__)

def predict_disease_risk(data):
    risk_score = 0
    age = int(data.get('age', 0))
    glucose = float(data.get('glucose', 0))
    bp = float(data.get('blood_pressure', 0))
    weight = float(data.get('weight', 0))

    if age > 50:
        risk_score += 2
    if glucose > 140:
        risk_score += 3
    if bp > 130:
        risk_score += 2
    if weight > 80:
        risk_score += 1

    if risk_score >= 6:
        risk_level = 'High'
    elif risk_score >= 3:
        risk_level = 'Moderate'
    else:
        risk_level = 'Low'

    explanation = f"Based on your inputs, your risk score is {risk_score}. Factors contributing include age, glucose, blood pressure, and weight."

    suggestions = [
        "Maintain a balanced diet",
        "Exercise regularly",
        "Monitor your blood pressure and glucose levels",
        "Consult a healthcare professional for personalized advice"
    ]

    return {
        'risk_level': risk_level,
        'explanation': explanation,
        'suggestions': suggestions
    }

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    result = predict_disease_risk(data)
    return render_template('result.html', data=data, result=result)

if __name__ == '__main__':
    app.run(debug=True)

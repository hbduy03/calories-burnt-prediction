from flask import Flask, request, jsonify, render_template
from calories.calories_burnt import CaloriesBurnt_Predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_calories():
    try:
        input_data = {
            'User_ID': 123455,
            'Gender': request.form['Gender'],
            'Age': int(request.form['Age']),
            'Height': int(request.form['Height']),
            'Weight': int(request.form['Weight']),
            'Duration': int(request.form['Duration']),
            'Heart_Rate': int(request.form['Heart_Rate']),
            'Body_Temp': float(request.form['Body_Temp'])
        }
        calo = CaloriesBurnt_Predict(input_data)
        return render_template('index.html', result=round(calo, 2))
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)

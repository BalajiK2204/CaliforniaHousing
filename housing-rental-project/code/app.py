from flask import Flask, request, jsonify
import mlflow
import mlflow.sklearn
import pandas as pd

app = Flask(__name__)
model = mlflow.sklearn.load_model("mlruns/0/models/m-4ed7519c98034ff9ad5a795b69484180/artifacts")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
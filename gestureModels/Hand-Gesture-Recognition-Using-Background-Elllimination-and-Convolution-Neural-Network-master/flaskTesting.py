from flask import Flask, request, jsonify
from ContinuousGesturePredictor import TestingModel

app = Flask(__name__)

# Load the model trained in ContinuousGesturePredictor.py
model = TestingModel()

# Checking if Flask server is running
@app.route('/')
def home():
    return "Flask server is running"

# Predicting using the pre-trained model
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Make sure the POST key is 'file'
        if 'file' not in request.files:
            return jsonify("Make sure you have uploaded a file and the file name is 'file'"), 400
        file = request.files['file']

        # Perform prediction
        prediction = model.predict(file)

        # Return prediction
        response = {
            "predicted_class": prediction,
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

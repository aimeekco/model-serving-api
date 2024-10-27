from flask import Flask, request, jsonify
import json
import train
import test

app = Flask(__name__)

# Load the model once at the start
train.train('data/NOTEEVENTS.csv')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # POST request
        input_data = request.get_json()

        # Save the input data to a file
        input_data_path = 'data/input.json'
        with open(input_data_path, 'w') as f:
            json.dump(input_data, f)
        
        # Make predictions
        results = test(input_data_path)
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
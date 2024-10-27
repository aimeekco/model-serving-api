from flask import Flask, request, jsonify
import torch
from my_model_module import load_model, preprocess_data, make_prediction  # Customize imports

app = Flask(__name__)

# Load the model once at the start
model = load_model()  # Make sure to define a load_model function to initialize your model
model.eval()  # Set the model to evaluation mode

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from POST request
        input_data = request.get_json()
        
        # Preprocess input data
        preprocessed_data = preprocess_data(input_data)  # Define this function based on repo

        # Convert data to a tensor if required by the model
        input_tensor = torch.tensor(preprocessed_data).float()
        
        # Make predictions
        with torch.no_grad():
            output = model(input_tensor)
        
        # Convert the model output to a response format
        prediction = output.numpy().tolist()  # Example: Convert to JSON-serializable format
        
        return jsonify({'prediction': prediction})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(debug=True)
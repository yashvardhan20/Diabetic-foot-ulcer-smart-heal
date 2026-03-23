from flask import Flask, request, jsonify, render_template
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load the trained model (ensure the path is correct)
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'wound_classification_cnn.h5')
model = load_model(MODEL_PATH)

# Define label mapping (class names to wound types and treatment options)
label_map = {
    0: {"wound_type": "Stage 1", "treatment": "Hydrocolloid Dressing"},
    1: {"wound_type": "Stage 2", "treatment": "Alginate Dressing"},
    2: {"wound_type": "Stage 3", "treatment": "Foam Dressing"},
    3: {"wound_type": "Infected", "treatment": "Antimicrobial Dressing"}
}

# Ensure upload directory exists
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads/')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Serve the main page (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Define the route to handle image uploads
@app.route('/predict', methods=['POST'])
def predict_wound_stage():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    # Get the file from the request
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the file temporarily
    img_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(img_path)

    try:
        # Load the image and preprocess it
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array = img_array / 255.0  # Rescale as was done during training

        # Make prediction
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction)

        # Map prediction to wound type and treatment options
        result = label_map[predicted_class]

        # Return the result as JSON (wound type and treatment recommendation)
        return jsonify({'wound_type': result['wound_type'], 'treatment': result['treatment']})

    except Exception as e:
        return jsonify({'error': 'Failed to process image', 'details': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

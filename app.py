from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import cv2

app = Flask(__name__)

# Load the trained model
MODEL_PATH = "Driver_Drowsiness_Detection.h5"
IMG_SIZE = (128, 128)  # Match this to your model's expected input size

try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


def preprocess_image(image):
    """
    Preprocess the input image for the model.
    :param image: Input image as a NumPy array.
    :return: Preprocessed image ready for inference.
    """
    try:
        # Resize the image to the model's expected dimensions
        image = cv2.resize(image, IMG_SIZE)
        # Normalize pixel values
        image = image / 255.0
        # Add a batch dimension
        return np.expand_dims(image, axis=0)
    except Exception as e:
        raise ValueError(f"Error during preprocessing: {e}")


@app.route('/')
def home():
    """
    Serve the HTML file for the home page.
    """
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict_drowsiness():
    """
    Endpoint to predict drowsiness.
    Accepts an image file and returns the prediction.
    """
    if model is None:
        return jsonify({"error": "Model not loaded. Please check the server logs."}), 500

    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image']
    try:
        # Convert the file to an OpenCV image
        file_bytes = np.frombuffer(file.read(), np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if image is None:
            return jsonify({"error": "Invalid image file"}), 400

        # Preprocess the image
        processed_image = preprocess_image(image)

        # Perform prediction
        prediction = model.predict(processed_image)
        print(f"Prediction: {prediction}")  # Debugging output

        # Get class label and confidence
        class_label = "Drowsy" if prediction[0][0] > 0.5 else "Not Sleeping"
        confidence = prediction[0][0] if class_label == "Drowsy" else 1 - prediction[0][0]

        return jsonify({
            "class": class_label,
            "confidence": float(confidence)
        })

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
    
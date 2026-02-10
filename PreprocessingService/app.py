from flask import Flask, request, jsonify
from pipeline import preprocess_image
import cv2
import numpy as np
app = Flask(__name__)
# purpose : This code sets up a Flask web server that listens for POST requests at the /preprocess endpoint. When an image is received, it decodes the image from the request, applies the preprocessing pipeline defined in pipeline.py, and returns the processed image as a response. This allows for easy integration with other components of the 3D scanning system, enabling efficient preprocessing of captured images before they are used for 3D reconstruction.

# Dummy camera params
camera_matrix = np.eye(3)
dist_coeffs = np.zeros((5,1))

# demonstration purposes only, in a real application these would be obtained from camera calibration


@app.route("/preprocess", methods=["POST"])
def preprocess():
    file = request.files.get("image")
    if not file:
        return jsonify({"error": "No image provided"}), 400

    img_array = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

# Apply the preprocessing pipeline to the image
#byte steam --- > numpy array --- > processed image (numpy array) --- > byte stream

    processed_img = preprocess_image(img, camera_matrix, dist_coeffs)
# core pipeline !!
    _, encoded_img = cv2.imencode('.png', processed_img)
    return encoded_img.tobytes(), 200, {'Content-Type':'image/png'}
#processed image -- png byte --- httpps response 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# local docker conteiner you can access the Flask app using http://localhost:5000/preprocess.

    # purpose : The Flask app is configured to run on all available network interfaces (
    # if there is no image provided in the request, it returns a 400 error with a message indicating that no image was provided. If an image is provided, it reads the image data, applies the preprocessing pipeline, and returns the processed image as a PNG byte stream with the appropriate content type header. This allows clients to easily receive and display the processed images.
from regression import train, predict
from flask import Flask, jsonify

import base64

app = Flask(__name__)


@app.route("/train/<path:document_filename_b64>", methods=["GET"])
def train_endpoint(document_filename_b64):
    document_folder = base64.b64decode(document_filename_b64).decode("utf-8")
    result = train(document_folder)
    return jsonify(result)


@app.route("/predict/<path:document_filename_b64>", methods=["GET"])
def predict_endpoint(document_filename_b64):
    document_filename = base64.b64decode(document_filename_b64).decode("utf-8")

    result = predict(document_filename)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)

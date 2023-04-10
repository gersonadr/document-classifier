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

# regression.train("/mnt/c/Users/Gerson/Projects/bookkeeper_tool/Documents")

# regression.predict(
#     "/mnt/c/Users/Gerson/Projects/bookkeeper_tool/Documents/Invoice/Aboriculture - 220825 - 20444.pdf",
#     "/mnt/c/Users/Gerson/Projects/bookkeeper_tool/",
# )

# %2Fmnt%2Fc%2FUsers%2FGerson%2FProjects%2Fbookkeeper_tool%2FDocuments

#%2Fmnt%2Fc%2FUsers%2FGerson%2FProjects%2Fbookkeeper_tool%2FDocuments%2FInvoice%2FAboriculture%20-%20220825%20-%2020444.pdf
#%2Fmnt%2Fc%2FUsers%2FGerson%2FProjects%2Fbookkeeper_tool%2F

# L21udC9jL1VzZXJzL0dlcnNvbi9Qcm9qZWN0cy9ib29ra2VlcGVyX3Rvb2wvRG9jdW1lbnRzL0ludm9pY2UvQWJvcmljdWx0dXJlIC0gMjIwODI1IC0gMjA0NDQucGRm
# L21udC9jL1VzZXJzL0dlcnNvbi9Qcm9qZWN0cy9ib29ra2VlcGVyX3Rvb2wv

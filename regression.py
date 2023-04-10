from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import data_loader
import random
import joblib
import os


def train(docs_folder):

    # load all data
    all_data = data_loader.load(docs_folder, extract_images=True, document_level=True)

    # assign id
    for i, datapoint in enumerate(all_data):
        datapoint["id"] = i

    # randomize the order before splitting into training and test
    random.shuffle(all_data)

    print(" - Step 5 - splitting training and test data (80/20)")
    # training data
    train_data = all_data[: int(len(all_data) * 0.8)]
    # train_data = all_data

    # test data
    test_data = all_data[int(len(all_data) * 0.2) :]

    # convert training data to text
    train_text = [data["text"] for data in train_data]

    # convert training labels to target values
    train_target = [data["type"] for data in train_data]

    # create vectorizer
    vectorizer = TfidfVectorizer()

    print(" - Step 6 - vectorizing")
    # fit vectorizer to training data
    vectorizer.fit(train_text)

    # transform training data to feature vectors
    train_features = vectorizer.transform(train_text)

    # create classifier
    classifier = LogisticRegression()

    print(" - Step 7 - classifing")
    # fit classifier to training data
    classifier.fit(train_features, train_target)

    # transform test data to feature vectors
    test_text = [data["text"] for data in test_data]
    test_features = vectorizer.transform(test_text)

    # make predictions on test data
    test_predictions = classifier.predict(test_features)

    # Predicting the probabilities for each document type
    test_probabilities = classifier.predict_proba(test_features)

    print(" - Done! Results: ")

    result = []
    # print predictions
    for i, data in enumerate(test_data):
        filename = data["filename"]
        doc_type_original = data["type"]
        doc_type_predicted = test_predictions[i]
        confidence = test_probabilities[i][
            classifier.classes_.tolist().index(doc_type_predicted)
        ]

        result.append(
            f"Document {filename} ({doc_type_original}) is classified as {doc_type_predicted} with confidence level {confidence:.2f}"
        )

    joblib.dump(classifier, "classifier.joblib")
    joblib.dump(vectorizer, "vectorizer.joblib")
    print(" - Model saved in files classifier.joblib and vectorizer.joblib")
    return result


def predict(input_file):
    if os.path.exists("classifier.joblib") and os.path.exists("vectorizer.joblib"):
        classifier = joblib.load("classifier.joblib")
        vectorizer = joblib.load("vectorizer.joblib")
    else:
        print("Model files not found: classifier.joblib and vectorizer.joblib")
        exit(1)

    data = data_loader.load_one(input_file)

    # transform test data to feature vectors
    test_text = [i["text"] for i in data]
    test_features = vectorizer.transform(test_text)

    # make predictions on test data
    test_predictions = classifier.predict(test_features)

    # Predicting the probabilities for each document type
    test_probabilities = classifier.predict_proba(test_features)

    # print predictions
    for i, data in enumerate(data):
        doc_type_predicted = test_predictions[i]
        confidence = test_probabilities[i][
            classifier.classes_.tolist().index(doc_type_predicted)
        ]
        result = {}
        result["type"] = doc_type_predicted
        result["confidence"] = confidence
        return result

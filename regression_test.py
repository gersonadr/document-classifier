from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# training data
train_data = [
    {"id": 1, "text": "this is an invoice", "type": "invoice"},
    {"id": 2, "text": "bank statement from abc bank", "type": "bank statement"},
    {"id": 3, "text": "remittance from xyz company", "type": "remittance"},
    {"id": 4, "text": "invoice for services rendered", "type": "invoice"},
    {"id": 5, "text": "bank statement for checking account", "type": "bank statement"},
]

# test data
test_data = [
    {"id": 6, "text": "invoice for consulting services"},
    {"id": 7, "text": "remittance from acme corp"},
    {"id": 8, "text": "bank statement for savings account"},
]

# convert training data to text
train_text = [data["text"] for data in train_data]

# convert training labels to target values
train_target = [data["type"] for data in train_data]

# create vectorizer
vectorizer = TfidfVectorizer()

# fit vectorizer to training data
vectorizer.fit(train_text)

# transform training data to feature vectors
train_features = vectorizer.transform(train_text)

# create classifier
classifier = LogisticRegression()

# fit classifier to training data
classifier.fit(train_features, train_target)

# transform test data to feature vectors
test_text = [data["text"] for data in test_data]
test_features = vectorizer.transform(test_text)

# make predictions on test data
test_predictions = classifier.predict(test_features)

# print predictions
for i, data in enumerate(test_data):
    print(f"Data point {data['id']} has been classified as {test_predictions[i]}")

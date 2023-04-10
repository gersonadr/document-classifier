from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# Define the list of input fields and the target variable field
fields = ["s1", "s2", "s3", "text"]
target = "type"

# Load the data from a file or database
data = [
    {
        "id": 1,
        "s1": 200,
        "s2": 300,
        "s3": 11,
        "text": "invoice",
        "type": "receipt",
    },
    {
        "id": 2,
        "s1": 150,
        "s2": 350,
        "s3": 15,
        "text": "invoice",
        "type": "receipt",
    },
    {
        "id": 3,
        "s1": 100,
        "s2": 250,
        "s3": 10,
        "text": "statement",
        "type": "bank statement",
    },
    {
        "id": 4,
        "s1": 50,
        "s2": 150,
        "s3": 5,
        "text": "remittance",
        "type": "remittance",
    },
    {
        "id": 5,
        "s1": 75,
        "s2": 200,
        "s3": 7,
        "text": "receipt",
        "type": "receipt",
    },
    # Add more datapoints here
]

# Create the input feature matrix X and the target variable y
X = []
y = []
for datapoint in data:
    x_i = [str(datapoint[field]) for field in fields]
    X.append(" ".join(x_i))
    y.append(datapoint[target])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert the text data to numeric using TF-IDF encoding
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train a Multinomial Naive Bayes classifier on the training set
clf = MultinomialNB()
clf.fit(X_train_tfidf, y_train)

# Predict the 'type' of the documents in the testing set
y_pred = clf.predict(X_test_tfidf)

# Evaluate the performance of the classifier
print(classification_report(y_test, y_pred))

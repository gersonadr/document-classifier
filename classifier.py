from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import data_loader

# Define the list of input fields and the target variable field
fields = ["x", "y", "w", "h", "confidence", "text"]
target = "type"

# {'x': 19, 'y': 17, 'w': 166, 'h': 26, 'confidence': 0.45, 'text': 'ConmonwealthBank', 'type': 'Bank statement'}

print(" - Load the data from a file or database")
data = data_loader.load()

print(" - Create the input feature matrix X and the target variable y")
X = []
y = []
for datapoint in data:
    x_i = [str(datapoint[field]) for field in fields]
    X.append(" ".join(x_i))
    y.append(datapoint[target])

print(" - Split the data into training and testing sets")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(" - Convert the text data to numeric using TF-IDF encoding")
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print(" - Train a Multinomial Naive Bayes classifier on the training set")
clf = MultinomialNB()
clf.fit(X_train_tfidf, y_train)

print(" - Predict the 'type' of the documents in the testing set")
y_pred = clf.predict(X_test_tfidf)

print(" - Evaluate the performance of the classifier")
print(classification_report(y_test, y_pred))

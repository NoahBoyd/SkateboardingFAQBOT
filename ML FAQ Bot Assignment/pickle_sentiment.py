### Load docs and labels
filenames = ["amazon_cells_labelled.txt", "imdb_labelled.txt", "yelp_labelled.txt"]
docs = []
labels = []
for filename in filenames:
    with open("sentiment/"+filename) as file:
        for line in file:
            line = line.strip()
            labels.append(int(line[-1]))
            docs.append(line[:-2].strip())

print("Documents Loaded",len(docs))

import spacy
nlp = spacy.load("en_core_web_lg")
vectors = [doc.vector for doc in nlp.pipe(docs)]
print("Vectors Created")

from joblib import dump
# Dump the vectors and labels
dump(vectors, "sentiment_vectors.joblib")
dump(labels, "sentiment_labels.joblib")
print("vectors dumped")

from sklearn.model_selection import train_test_split
train_data, test_data, train_labels, test_labels = train_test_split(vectors, labels)
print("train/test split done")
# print(test_data)


from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(max_iter=1000)
clf.fit(train_data, train_labels)
print("Training done")
# Dump the Classifier
dump(clf, 'sentiment_classifier.pkl')
# from joblib import load
# clf = load('sentiment_classifier.pkl')
# doc1 = ["This is a great bot"]
# newTest = [doc.vector for doc in nlp.pipe(doc1)]
# print(newTest)
# newP = clf.predict(newTest)
# print("Prediction is: ")
# print(newP)

# predictions = clf.predict(test_data)
# from sklearn.metrics import accuracy_score, precision_score, recall_score

# a = accuracy_score(test_labels, predictions)
# p = precision_score(test_labels, predictions, average="macro")
# r = recall_score(test_labels, predictions, average="macro")

# print("Accuracy Score:", a, "Precision Score:", p, "Recall Score:", r)

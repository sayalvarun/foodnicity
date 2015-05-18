from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np

text_clf = Pipeline([('vect', CountVectorizer()),
                      ('tfidf', TfidfTransformer()), #Replaces commented code below
                      ('clf', MultinomialNB()),
])

data = []

labels = []


categories = ['east', 'west']

eastFile = open("East.txt")

eastContents = eastFile.read()

splitEastContents = eastContents.split("\n")

for line in splitEastContents:
	splitLine = line.split(",",1)
	data.append(splitLine[1])
	labels.append(int(splitLine[0]))

eastFile.close()

npData = np.array(data)
npLabels = np.array(labels)

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(npData)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

print npLabels

clf = MultinomialNB().fit(X_train_tfidf, npLabels)



#clf = text_clf.fit(data, labels) #Vectorizer + transformer + classifier

'''docs_new = ['Candied Apple', 'Cucumber']

predicted = clf.predict(docs_new)

print predicted'''

'''for doc, category in zip(docs_new, predicted):
	print('%r => %s' % (doc, twenty_train.target_names[category]))'''



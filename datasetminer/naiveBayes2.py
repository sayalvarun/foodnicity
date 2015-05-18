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

arr = []
arr2 = []

#data = np.array(arr)
data = []
#labels = np.array(arr2)
labels = []

categories = ['east', 'west']

eastFile = open("East.txt")

for line in eastFile:

	line = line.rstrip()
	l,d = line.split(",",1)
	#np.append(data, splitLine[1])
	#np.append(labels, int(splitLine[0]))
	data.append(d)
	labels.append(l)

eastFile.close()

print "--Data--"
print data
print "--labels--"
print labels

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf = MultinomialNB().fit(X_train_tfidf, labels)



#clf = text_clf.fit(data, labels) #Vectorizer + transformer + classifier

'''docs_new = ['Candied Apple', 'Cucumber']

predicted = clf.predict(docs_new)

print predicted'''

'''for doc, category in zip(docs_new, predicted):
	print('%r => %s' % (doc, twenty_train.target_names[category]))'''



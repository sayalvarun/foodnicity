from sklearn.datasets import fetch_20newsgroups
from sklearn.datasets import load_files
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


cats = ['East', 'West']

dset = load_files("Data",categories=cats, load_content=True, shuffle=True, encoding=None, decode_error='strict', random_state=0)

clf = text_clf.fit(dset.data, dset.target) #Vecotorizer + transformer + classifier

docs_new = ['ground beef,chopped onion,chopped celery,chopped carrots,garlic,peeled and diced tomatoes,tomato sauce,kidney beans,water,beef bouillon granules,dried parsley,dried oregano,dried basil,chopped cabbage,whole kernel corn,green beans,macaroni', 
			'canola oil,onion,garlic,beef stew meat,water,tomatoes,fresh green beans,bok choy,fresh broccoli,tamarind soup base']

predicted = clf.predict(docs_new)

print predicted



'''eastFile = open("East.txt")

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

clf = MultinomialNB().fit(X_train_tfidf, npLabels)'''



#clf = text_clf.fit(data, labels) #Vectorizer + transformer + classifier

'''docs_new = ['Candied Apple', 'Cucumber']

predicted = clf.predict(docs_new)

print predicted'''

'''for doc, category in zip(docs_new, predicted):
	print('%r => %s' % (doc, twenty_train.target_names[category]))'''



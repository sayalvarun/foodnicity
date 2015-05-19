from sklearn.datasets import fetch_20newsgroups
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.linear_model import SGDClassifier

def getClass(val):
	if val == 0:
		return "East"
	elif val == 1:
		return "West"
	else:
		return "N/A"

text_clf = Pipeline([('vect', CountVectorizer()),
                      ('tfidf', TfidfTransformer()), #Replaces commented code below
                      ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                            alpha=1e-3, n_iter=5, random_state=42)),
])

data = []

labels = []

cats = ['East', 'West']

dset = load_files("Data",categories=cats, load_content=True, shuffle=True, encoding=None, decode_error='strict', random_state=0)

#testSet = load_files("Test",categories=cats, load_content=True, shuffle=True, encoding=None, decode_error='strict', random_state=0)

clf = text_clf.fit(dset.data, dset.target) #Vectorizer + transformer + classifier

docs_new = []

labels = []

testFile = open("Holdout.txt","r")

testDocs = testFile.read().split("\n")

for line in testDocs:
	docs_new.append(line.split(",",1)[1])
	labels.append(int(line.split(",",1)[0]))

predicted = clf.predict(docs_new)

for doc, category in zip(docs_new, predicted):
	print('%r => %s' % (doc, getClass(category)))

print np.mean(predicted == labels)

#print np.mean(predicted == testSet.target)

'''docs_new = ['refrigerated pie crust,butter,leeks,salt and black pepper to taste,light cream,shredded Gruyere cheese',
'vegetable oil,potatoes,onions,garlic,minced fresh ginger root,chili powder,ground black pepper,ground turmeric,ground cumin,salt,medium tomatoes,plain yogurt,chopped fresh mint leaves,ground cardamom,cinnamon stick,boneless,vegetable oil,onion,powdered saffron,cardamom,whole cloves,cinnamon stick,ground ginger,basmati rice,chicken stock,salt']

predicted = clf.predict(docs_new)'''


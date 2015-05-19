#############################################################################################################
# This script uses the scipy multinomial naive bayes classification library to do							#
# classification on the 7 category data								   										#
#############################################################################################################

from sklearn.datasets import fetch_20newsgroups
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np

#Function to get the name of the class given the integer
#label
def getClass(val):
	if val == 0:
		return "Africa"
	elif val == 1:
		return "Asian"
	elif val == 2:
		return "Australian-and-New-Zealander"
	elif val == 3:
		return "Canadian"
	elif val == 4:
		return "European"
	elif val == 5:
		return "Latin-American"
	elif val == 6:
		return "Middle-Eastern"	
	else:
		return "N/A"

#Pipeline object used to the following
#Vectorize = Count occurrences of ingredients (Bag of words)
#Transform = Normalize for differences in number of recipes for a particular country
#MultinomialNB = Classifier used for Naive Bayes
text_clf = Pipeline([('vect', CountVectorizer()),
                      ('tfidf', TfidfTransformer()), #Replaces commented code below
                      ('clf', MultinomialNB()),
])

cats = ['African', 'Asian', 'Australian-and-New-Zealander', 'Canadian', 'European', 'Latin-American', 'Middle-Eastern']

dset = load_files("7CatData",categories=cats, load_content=True, shuffle=True, encoding=None, decode_error='strict', random_state=0)
#Dataset loaded into a scikit bunch object

clf = text_clf.fit(dset.data, dset.target) #Vectorizer + transformer + classifier
#Classifier fitted to the training data

docs_new = []
#Test recipes stored in list

labels = []
#Labels associated to each test recipes

testFile = open("multiHoldout.txt","r")
#File used to contain the holdout examples

testDocs = testFile.read().split("\n")
#Read test contents into an array

#Populate the test arrays (docs_new, labels)
for line in testDocs:
	docs_new.append(line.split(",",1)[1])
	labels.append(int(line.split(",",1)[0]))

#Array of predictions for the test data
predicted = clf.predict(docs_new)

#Printouts for each test example
for doc, category in zip(docs_new, predicted):
	print('%r => %s' % (doc, getClass(category)))

#Final classification rate
print np.mean(predicted == labels)



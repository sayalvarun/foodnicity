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

categories = ['alt.atheism', 'soc.religion.christian',
		'comp.graphics', 'sci.med']

twenty_train = fetch_20newsgroups(subset='train',
	categories=categories, shuffle=True, random_state=42)

#count_vect = CountVectorizer()
#X_train_counts = count_vect.fit_transform(twenty_train.data)

#tfidf_transformer = TfidfTransformer()
#X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

#clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

clf = text_clf.fit(twenty_train.data, twenty_train.target) #Vecotorizer + transformer + classifier

print twenty_train.data[0]
print(twenty_train.target_names[twenty_train.target[0]])

docs_new = ['God is love', 'OpenGL on the GPU is fast',]
#X_new_counts = count_vect.transform(docs_new)
#X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(docs_new)



#print twenty_train.target_names
#print X_train_counts.shape
#print count_vect.vocabulary_.get(u'algorithm')
#print X_train_tfidf.shape
#print X_new_counts
print predicted

for doc, category in zip(docs_new, predicted):
	print('%r => %s' % (doc, twenty_train.target_names[category]))



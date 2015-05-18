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

categories = ['east', 'west']

twenty_train = fetch_20newsgroups(subset='train',
	categories=categories, shuffle=True, random_state=42)


clf = text_clf.fit(twenty_train.data, twenty_train.target) #Vecotorizer + transformer + classifier

docs_new = ['God is love', 'OpenGL on the GPU is fast']

predicted = clf.predict(docs_new)

twenty_test = fetch_20newsgroups(subset='test',
     categories=categories, shuffle=True, random_state=42)
docs_test = twenty_test.data
predicted = text_clf.predict(docs_test)

#print twenty_train.target_names
#print X_train_counts.shape
#print count_vect.vocabulary_.get(u'algorithm')
#print X_train_tfidf.shape
#print X_new_counts
print predicted
print np.mean(predicted == twenty_test.target)

for doc, category in zip(docs_new, predicted):
	print('%r => %s' % (doc, twenty_train.target_names[category]))

#print twenty_train.data
#print twenty_test.data
for t in twenty_test.target[:10]:
	print(twenty_test.target_names[t])



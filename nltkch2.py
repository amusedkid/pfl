import nltk

"""NLTK Chapter2, Exercise 8"""


"""
names = nltk.corpus.names
cfd = nltk.ConditionalFreqDist(
			(fileid, name[0])
			for fileid in names.fileids()
			for name in names.words(fileid))

cfd.tabulate()
"""

"""NLTK Chapter2, Exercise 15"""

"""Returns all the words that occur at least three times in the Brown Corpus"""

"""
from nltk.corpus import brown
text = brown.words()
fdist = nltk.FreqDist(w.lower() for w in text)
greater_than3x = set(w for w in text if fdist[w] >= 3)

print(greater_than3x)
"""

"""NLTK Chapter2 Exercise 16"""
"""generates a table of lexical diversity scores (ie. token/type ratios). Includes the full set of Brown Corpus genres."""

"""
from nltk.corpus import brown
brown.categories

print("%-15s %10s %10s 	%15s" % ("Category", "Tokens", "Types", "Lexical Diversity"))
for category in brown.categories():
	tokens = len(brown.words(categories=category))
	types = len(set(brown.words(categories=category)))
	diversity = types/tokens
	print("%-15s %10d %10d %10.3f" % (category, tokens, types, diversity))
"""


"""NLTK Chapter2, Exercise 17"""
"""A function that finds the 50 most frequently occuring words of a text that are not stopwords"""

"""
import nltk
from nltk.book import *

def top50words(text):
	stop_words = nltk.corpus.stopwords.words('english')
	content = [w for w in text if w.lower() not in stop_words]
	fdist = nltk.FreqDist(content)
	
	return fdist.most_common(50)

print(top50words(text1))
"""

"""NLTK Chapter2, Exercise 18"""
"""A function that finds the 50 most frequently occuring bigrams of a text, that do not contain any stopwords"""

"""
def top50bigrams(text):
	stop_words = nltk.corpus.stopwords.words('english')
	bigrams = tuple(nltk.bigrams([w for w in text if w.lower() not in stop_words]))
	fdist = nltk.FreqDist(bigrams)
	
	return fdist.most_common(50)

print(top50bigrams(text1))
"""
	

"""NLTK Chapter2 Exercise 20"""
"""A function wordfreq() takes a word and the name of a section of
the Brown corpus as arguments, computes the frequency of the word in that section of the corpus"""
# what do we mean by 'section'? do we mean category??? slice???
# is it overkill to make a conditional frequency distribution here?
# it seems like a bit of overkill


from nltk.corpus import brown
def wordfreq(word, section):
	cfd = nltk.ConditionalFreqDist(
		(genre, word)
		for genre in brown.categories()
		for word in brown.words(categories = genre))
	
	return cfd[section][word]

print(wordfreq('of', 'hobbies'))
	
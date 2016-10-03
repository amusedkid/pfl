"""
Jose Ramirez, jramirez@brandeis.edu
LING 131A, Programming for Linguistics, Fall 2015
Assignment #4
10/16/2015
"""
#!/usr/bin/python

import nltk
import sys, os
from collections import Counter


class myCorpus:
	""" a simple corpus class"""

	def __init__(self,corpus_dir):
		self.corpus_dir = corpus_dir
		self.fdist = self.freq_dist()

	def freq_dist(self):
		c = Counter()
		for directory,subdir,files in os.walk(self.corpus_dir):
			for f in files:
				fh = open(directory + '/' + f, 'r')
				text = fh.read().split()
				c.update(text)
		return c

	def get_tokenizedwords(self, filename):
		"""taking a filename as input, returns a list of tokenized words"""
		file = open(filename)
		text = file.read()
		
		#use nltk.tokenize to tokenize words in file
		tokens = nltk.tokenize.word_tokenize(text)
		return tokens
		
	def get_sentences(self, filename):
		""" taking a file name as input, returns a list of sentences"""
		file = open(filename)
		text = file.read()
		
		# use nltk's sent_tokenize function to split into sentences
		sentences = nltk.tokenize.sent_tokenize(text)
	
		return sentences
	
	def wordtokenized_sents(self, filename):
		"""taking a file name as input, returns a list of word-tokenized
		sentences"""
		
		#use get_sentences function above to split the text into sentences
		sentences = self.get_sentences(filename)
		
		# split the sentence into tokens
		# each sentence becomes a list of tokens
		sentences2 = []
		for sentence in sentences:
			words = nltk.tokenize.word_tokenize(sentence)
			sentences2.append(words)
	
		return sentences2
		
	def mostfreq_content(self, filename):
		"""taking a file name as input, returns the most frequent content words (ie. no stop words)"""
		file = open(filename)
		text = file.read()
		list = text.split()
		
		# iterate over the text to create a new list without stopwords
		
		list2 = []
		
		#check the words in our text against nltk's stopwords list
		stop_words = nltk.corpus.stopwords.words('english')
		for item in list:
			if item not in stop_words and item.isalnum():
				list2.append(item)
				
		#get frequency distribution of our list of content words
		fdist = nltk.FreqDist(list2)
		
		#get the most frequent word
		mostfreq = fdist.max()

		return mostfreq
		
	def mostfreq_bigrams(self, filename):
		"""taking a file name, finds the most frequent bigrams that do not contain a stop word"""
		file = open(filename)
		text = file.read()
		list = text.split()
		
		#iterate over text to create a new list without stopwords
		list2 = []
		
		#check the words in our text against nltk's stopwords list
		stop_words = nltk.corpus.stopwords.words('english')
		
		#add content words to new lsit
		for item in list:
				if item not in stop_words and item.isalnum():
					list2.append(item)

		# create bigrams as tuples in order for us to be able to
		# use freqdist on them
		bigrams = tuple(nltk.bigrams(list2))
		
		# get freqdist of bigrams
		freqdist = nltk.FreqDist(bigrams)
		
		# get the most frequent bigram
		mostfreq = freqdist.max()

		return mostfreq

		
#test our functions with 'wsj_001.mrg' file in my_corpus/my_text_corpus

corpus1 = myCorpus(sys.argv[1])
#corpus1=myCorpus(r'/Users/nianwen1/teaching/ling131/ling131-fall-2015/my_text_corpus')
#corpus1 = myCorpus('my_corpus//my_text_corpus')
print (max(corpus1.freq_dist().keys()))

tokens = corpus1.get_tokenizedwords('my_corpus//my_text_corpus//wsj_0001.mrg')
print(tokens)

sentences = corpus1.get_sentences('my_corpus//my_text_corpus//wsj_0001.mrg')
print(sentences)

word_token_sents = corpus1.wordtokenized_sents('my_corpus//my_text_corpus//wsj_0001.mrg')
print(word_token_sents)

most_frequent_content = corpus1.mostfreq_content('my_corpus//my_text_corpus//wsj_0001.mrg')
print(most_frequent_content)

# for wsj_0001.mrg, all bigrams occur only once
most_frequent_bigrams = corpus1.mostfreq_bigrams('my_corpus//my_text_corpus//wsj_0001.mrg')
print(most_frequent_bigrams)



"""NLTK Chapter 2 Exercises"""

"""NLTK Chapter2, Exercise 8"""
"""A conditional frequency distribution over Names corpus to see
which initial letters are more frequent for males vs. females"""

# access Names corpus
names = nltk.corpus.names

# create conditonal frequency distribution. Condition is file, target is initial letter in each name
cfd = nltk.ConditionalFreqDist(
			(fileid, name[0])
			for fileid in names.fileids()
			for name in names.words(fileid))

# creates a table of the frequency distribution for each initial letter
# for each file
cfd.tabulate()


"""NLTK Chapter2, Exercise 15"""
"""Returns all the words that occur at least three times in the Brown Corpus"""
# import brown corpus and store all the words in the corpus to 'text'
from nltk.corpus import brown
text = brown.words()

# remove capitalization for words, and create a frequency distribution
fdist = nltk.FreqDist(w.lower() for w in text)

# create a set of words that appear more than 3 times
greater_than3x = set(w for w in text if fdist[w] >= 3)

# print those words
print(greater_than3x)


"""NLTK Chapter2 Exercise 16"""
"""generates a table of lexical diversity scores (ie. token/type ratios). Includes the full set of Brown Corpus genres."""

from nltk.corpus import brown

print("%-15s %10s %10s 	%15s" % ("Category", "Tokens", "Types", "Lexical Diversity"))
for category in brown.categories():
	tokens = len(brown.words(categories=category))
	types = len(set(brown.words(categories=category)))
	diversity = types/tokens 
	print("%-15s %10d %10d %10.3f" % (category, tokens, types, diversity))

	
"""NLTK Chapter2, Exercise 17"""
"""A function that finds the 50 most frequently occuring words of a text that are not stopwords"""

# I'll be using 'Moby Dick' to test the function
from nltk.book import *

def top50words(text):
	# create a list of content words by checking words in text against
	#stop words
	stop_words = nltk.corpus.stopwords.words('english')
	content = [w for w in text if w.lower() not in stop_words]
	
	# create frequency distribution of content words
	fdist = nltk.FreqDist(content)
	
	# use most_common function from FreqDist to return 50 most common
	#content words
	return fdist.most_common(50)

# print top 50 content words from 'Moby Dick'
print(top50words(text1))


"""NLTK Chapter2, Exercise 18"""
"""A function that finds the 50 most frequently occuring bigrams of a text, that do not contain any stopwords"""

def top50bigrams(text):
	stop_words = nltk.corpus.stopwords.words('english')
	
	# first, elminates capitalization and stop words, and puts in new list
	# list is turned to bigrams (in tuple form so we can use FreqDist on them)
	bigrams = tuple(nltk.bigrams([w for w in text if w.lower() not in stop_words]))
	
	# create frequency distribution of bigrams
	fdist = nltk.FreqDist(bigrams)
	
	# return 50 most common bigrams
	return fdist.most_common(50)

# find top 50 bigrams of content words in 'Moby Dick'
print(top50bigrams(text1))



"""NLTK Chapter2 Exercise 20"""
"""A function wordfreq() takes a word and the name of a section of
the Brown corpus as arguments, computes the frequency of the word in that section of the corpus"""
# I interpreted 'section' to mean 'Category' in the Brown Corpus

def wordfreq(word, section):
	# create a conditional frequency distribution for each category 
	#and word in Brown Corpus.
	cfd = nltk.ConditionalFreqDist(
		(genre, word)
		for genre in brown.categories()
		for word in brown.words(categories = genre))
	
	# access the conditions to get the frequency of the word
	return cfd[section][word]

# use wordfreq() to see how often 'of' appears in the 'hobbies' category
print(wordfreq('of', 'hobbies'))



"""Modified generate_model function"""
"""A new version of the 'generate_model' from NLTK Ch 2, Sec. 2.4.
It generates the most likely next word based on two previous words
rather than one."""

def generate_model2(cfdist, bigram, num=15):
	# instead of a word, it takes a bigram
	# the conditional frequency distribution should be one where
	#the condition is a bigram
	for i in range(num):
		#prints the first word in bigram
		print(bigram[0], end = ' ') 
		
		# next bigram is the bigram that most frequently comes after the current one. First word in the next bigram should be the second word in the current one.
		bigram = cfdist[bigram].max() 

# use the Book of Genesis, King James Version for sample text
text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text) # get bigrams of text
bigramsofbigrams = nltk.bigrams(bigrams) # get bigrams of bigrams

#create a conditonal frequency distribution from the bigrams of bigrams
#the condition is a bigram, and the targets are also bigrams
cfd = nltk.ConditionalFreqDist(bigramsofbigrams)

# test generate_model2 with bigram ('in', 'the')
generate_model2(cfd, ('in', 'the'))
print('\n')

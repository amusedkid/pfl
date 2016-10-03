"""
Jose Ramirez, jramirez@brandeis.edu
LING 131A, Programming for Linguistics, Fall 2015
Assignment #3
10/8/2015
"""

import os
from operator import itemgetter

class corpus:
	def __init__(self, directory):
		"""Instantiates the corpus object"""
		self.directory = directory
		
	def listofdocs(self):
		"""Returns a list of all documents in the corpus"""
		paths = os.walk(self.directory)
		for directory, subdirectory, files in paths:
			return files

	def num_sentences(self):
		"""Returns a sentence count for the corpus"""

		paths = os.walk(self.directory)
		for directory, subdirectory, files in paths:
			num_sentences = 0 # store the number of sentences
			
			# open each file and read through the text
			for i in files:
				file = open(os.path.join(self.directory, i))
				text = file.read()
				
				# assume that the number of sentence-ending punctuation marks
				# equals the number of sentences
				for character in text:
					if character == "." or character == "?" or character == "!":
						num_sentences += 1
			return num_sentences

	def wordtoken_count(self):
		"""Returns number of word tokens in corpus"""
		paths = os.walk(self.directory)
		for directory, subdirectory, files in paths:
			num_tokens = 0 # total number of tokens in corpus
			for i in files:
				file = open(os.path.join(self.directory, i))
				text = file.read()
				
				# split text into a list in order to iterate
				# through each token
				list = text.split()
				
				# count number of tokens
				for token in list:
					num_tokens += 1
			return num_tokens
	
	def wordtype_count(self):
		"""Returns number of word types in corpus"""
		paths = os.walk(self.directory)
		for directory, subdirectory, files in paths:
			num_wordtypes = 0 # total number of word types in corpus
			list2 = [] # a list of words in the entire corpus
			
			# for loop will eliminate punctuation and add word tokens to list2
			for i in files:
				file = open(os.path.join(self.directory, i))
				text = file.read()
				
				# split text into a list in order to iterate
				# through each token
				list = text.split()
				
				#strip words of any punctuation at end to avoid duplicate types in list2
				for word in list:
					# skip punctuation
					if word == "," or word == "?" or word == "." or word == "!" or word == " ":
						continue
					word = word.lower()
					word = word.strip("?")
					word = word.strip(".")
					word = word.strip('"')
					word = word.strip(",")
					list2.append(word)
			
			# make a set out of the words in list2 to get word types
			wordset = set(list2)
			# count the number of wordtypes
			for element in wordset:
				num_wordtypes += 1
			
			return num_wordtypes
	
	def words_by_freq(self):
		"""Returns a list of words sorted by their frequency"""

		# get the frequencies of word types, and put the word and frequency in a dict
		
		paths = os.walk(self.directory)
		for directory, subdirectory, files in paths:
			# make a list of word tokens
			list2 = []
			for i in files:
				# make a list of wordtypes
				file = open(os.path.join(self.directory, i))
				text = file.read()
				list = text.split()
				for word in list:
					# skip punctuation
					if word == "," or word == "?" or word == "." or word == "!" or word == " ":
						continue
					#strip words of any punctuation at end to avoid duplicate types
					word = word.lower()
					word = word.strip("?")
					word = word.strip(".")
					word = word.strip('"')
					word = word.strip(",")
					list2.append(word)
			
			# get a dictionary of words and their frequencies
			wordfreq = {}
			for word in list2:
				if word in wordfreq:
					wordfreq[word] += 1
				else:
					wordfreq[word] = 1
			
			# use itemgetter to create a dictionary of words sorted by their frequency
			sortedwordfreq = sorted(wordfreq.items(), key = itemgetter(1), reverse = True)
			
			return sortedwordfreq
	
	def bigrams_by_freq(self):
		"""Returns a list of bigrams, sorted by frequency"""
		
		#create a list of bigrams
		paths = os.walk(self.directory)
		for directory, subdirectory, files in paths:
			newlist = []
			for i in files:
				file = open(os.path.join(self.directory, i))
				text = file.read()
				list = text.split()
				for j in range(0, len(list)):
					if j <= len(list) - 2:
						newlist.append(list[j : j + 2])
					else:
						break
			
			# create a dictionary of bigrams and their frequencies
			# from the previous list of bigrams
			gramsdict = {}
			for element in newlist:
				element = ' '.join(element)
				if element in gramsdict:
					gramsdict[element] += 1
				else:
					gramsdict[element] = 1
			
			# use itemgetter to create a dictionary of bigrams sorted by their frequency
			sortedgramsdict = sorted(gramsdict.items(), key = itemgetter(1), reverse = True)
			
			return sortedgramsdict
	
	def longest_word(self):
		"""Returns the longest word(s) in this corpus""" 
		
		paths = os.walk(self.directory)
		for directory, subdirectory, files in paths:
			max_length = 0 # store the length of the longest words in the corpus
			wordslendict = {} # a dictionary of words and their lengths
			for i in files:
				file = open(os.path.join(self.directory, i))
				text = file.read()
				list = text.split()
				
				#create a dictionary of words and their lengths
				list2 = []
				# strip words of any extraneous punctuation and add them to a new list
				for word in list:
					# skip punctuation
					if word == "," or word == "?" or word == "." or word == "!" or word == " ":
						continue
					#strip words of any punctuation at end to avoid duplicate types
					word = word.lower()
					word = word.strip("?")
					word = word.strip(".")
					word = word.strip('"')
					word = word.strip(",")
					list2.append(word)
				
				# add words and length to wordslendict from list2
				# see if any of the words in this list are longer than max
				# length. If yes, change the value of max_length.
				for word in list2:
					if len(word) > max_length:
						max_length = len(word)
					wordslendict[word] = len(word)
					
			# create a list of the longest words, in case there is more than
			# one word at the maximum length. Return that list.
			longest_words = []
			for word in wordslendict:
				if wordslendict[word] == max_length:
					longest_words.append(word)
			
			return longest_words
		

# create an object from corpus class, and test each method

mycorpus = corpus("my_corpus\\my_text_corpus")

print(mycorpus.listofdocs())

totalsentences = mycorpus.num_sentences()
print("There are %d sentences in this corpus." % totalsentences)

totaltokens = mycorpus.wordtoken_count()
print("There are %d tokens in this corpus." % totaltokens)

totaltypes = mycorpus.wordtype_count()
print("There are %d word types in this corpus." % totaltypes)

wordsbyfreq = mycorpus.words_by_freq()
print(wordsbyfreq)

bigramsfreq = mycorpus.bigrams_by_freq()
print(bigramsfreq)

longestword = mycorpus.longest_word()
print(longestword)
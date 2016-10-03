import os

def longest_word():
	"""Returns the longest word(s) in this corpus""" 
	paths = os.walk('my_corpus\\my_text_corpus')
	for directory, subdirectory, files in paths:
		max_length = 0 # store the length of the longest words in the corpus
		wordslendict = {} # a dictionary of words and their lengths
		for i in files:
			file = open(os.path.join('my_corpus\\my_text_corpus', i))
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
		
print(longest_word())
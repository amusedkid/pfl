import os

"""
paths = os.walk('my_corpus\\my_text_corpus')
for directory, subdirectory, files in paths:
	for i in files:
		print(i)
"""

"""prints a list of all documents in corpus"""
paths = os.walk('my_corpus\\my_text_corpus')
for directory, subdirectory, files in paths:
	print(files)


"""print number of sentences in corpus"""	
paths = os.walk('my_corpus\\my_text_corpus')
for directory, subdirectory, files in paths:
	num_sentences = 0
	for i in files:
		file = open(os.path.join('my_corpus\\my_text_corpus', i))
		text = file.read()
		for character in text:
			if character == "." or character == "?" or character == "!":
				num_sentences += 1
	print(num_sentences)

"""print number of word tokens in corpus"""	
paths = os.walk('my_corpus\\my_text_corpus')
for directory, subdirectory, files in paths:
	num_tokens = 0
	for i in files:
		file = open(os.path.join('my_corpus\\my_text_corpus', i))
		text = file.read()
		list = text.split()
		num_ind_tokens = 0
		for token in list:
			num_tokens += 1
	print(num_tokens)
	


"""print number of word types in corpus"""
paths = os.walk('my_corpus\\my_text_corpus')
for directory, subdirectory, files in paths:
	num_wordtypes = 0
	list2 = [] # a list of words in the entire corpus
	
	# for loop will eliminate punctuation and add word tokens to list2
	for i in files:
		file = open(os.path.join('my_corpus\\my_text_corpus', i))
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
	# make a set out of the words in list2 to get word types
	wordset = set(list2)
	# count the number of wordtypes
	for element in wordset:
		num_wordtypes += 1
	print(num_wordtypes)
	
	"""returns a list of words sorted by their frequency"""
	
	# get the frequencies of words, and put the word and frequency in a dict
	
	# create a new list
		
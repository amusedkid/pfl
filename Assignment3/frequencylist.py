import os
from operator import itemgetter

def words_by_freq():
	paths = os.walk('my_corpus\\my_text_corpus')

	"""returns a list of words sorted by their frequency"""

		# get the frequencies of word types, and put the word and frequency in a dict
	for directory, subdirectory, files in paths:
		# make a list of word tokens
		list2 = []
		for i in files:
			# make a list of wordtypes
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
		
		
		wordfreq = {}
		for word in list2:
			if word in wordfreq:
				wordfreq[word] += 1
			else:
				wordfreq[word] = 1
		
		sortedwordfreq = sorted(wordfreq.items(), key = itemgetter(1), reverse = True)
		
		return(sortedwordfreq)
	
print(words_by_freq())

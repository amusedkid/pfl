
import os
from operator import itemgetter

def bigrams_by_freq():
	"""Return a list of bigrams, sorted by frequency"""
	#create a list of bigrams
	paths = os.walk('my_corpus\\my_text_corpus')
	for directory, subdirectory, files in paths:
		newlist = []
		for i in files:
			file = open(os.path.join('my_corpus\\my_text_corpus', i))
			text = file.read()
			list = text.split()
			for j in range(0, len(list)):
				if j <= len(list) - 2:
					newlist.append(list[j : j + 2])
				else:
					break
		
	# create a dictionary of bigrams and their frequencies
		gramsdict = {}
		for element in newlist:
			element = ' '.join(element)
			
			if element in gramsdict:
				gramsdict[element] += 1
			else:
				gramsdict[element] = 1
		
		sortedgramsdict = sorted(gramsdict.items(), key = itemgetter(1), reverse = True)
		
		return sortedgramsdict
		
print(bigrams_by_freq())
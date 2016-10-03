def get_sentences(filename):
	""" taking a file name as input, returns a list of sentences"""
	import nltk
	
	file = open(filename)
	text = file.read()
	sentences = nltk.tokenize.sent_tokenize(text)
	
	return sentences

sentences = get_sentences('C://Users//owner//desktop//clma//fall2015//pfl//assignments//assignment4//my_corpus//my_text_corpus//wsj_0001.mrg')
print(sentences)
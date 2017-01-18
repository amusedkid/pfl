
def get_tokenizedwords(filename):
	"""taking a filename as input, returns a list of tokenized words"""
	import nltk

	file = open(filename)
	text = file.read()
	tokens = nltk.tokenize.word_tokenize(text)

	return tokens
	
tokens = get_tokenizedwords('C://Users//owner//desktop//clma//fall2015//pfl//assignments//assignment4//my_corpus//my_text_corpus//wsj_0001.mrg')
print(tokens)

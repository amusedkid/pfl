import nltk

def get_sentences(filename):
	""" taking a file name as input, returns a list of sentences"""
	import nltk
	
	file = open(filename)
	text = file.read()
	sentences = nltk.tokenize.sent_tokenize(text)
	
	return sentences
	
def wordtokenized_sents(filename):
	sentences = get_sentences(filename)
	sentences2 = []
	for sentence in sentences:
		words = nltk.tokenize.word_tokenize(sentence)
		sentences2.append(words)
	
	return sentences2

word_token_sents = wordtokenized_sents('C://Users//owner//desktop//clma//fall2015//pfl//assignments//assignment4//my_corpus//my_text_corpus//wsj_0001.mrg')
print(word_token_sents)

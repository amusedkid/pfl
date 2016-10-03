"""modify this by generating the most likely next word based on two previous words rather than one. Demonstrate how it works with a corresponding conditional frequency distribution"""

import nltk

"""essentially, this function takes a conditional frequency distribution of bigrams and a word and makes a sentence. 
Each time, a loop prints the current word, then looks for the next word by finding the most frequent word that appears in texts after it.
It then prints that word, and the process repeats again, generating the random sentence"""
def generate_model(cfdist, word, num=15):
	for i in range(num):
		print(word, end = ' ')
		word = cfdist[word].max()
	
def generate_model2(cfdist, bigram, num=15):
	for i in range(num):
		print(bigram[0], end = ' ')
		bigram = cfdist[bigram].max()
		
		
text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
bigramsofbigrams = nltk.bigrams(bigrams)
cfd = nltk.ConditionalFreqDist(bigramsofbigrams)

bigrams = nltk.bigrams(text)
cfd2 = nltk.ConditionalFreqDist(bigrams)

generate_model(cfd2, 'in')
print('\n')
generate_model2(cfd, ('in', 'the'))
#print(cfd[('in', 'the')].max())
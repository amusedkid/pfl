def mostfreq_bigrams(filename):
	import nltk

	file = open(filename)
	text = file.read()
	print(text)
	list = text.split()
	list2 = []
	stop_words = nltk.corpus.stopwords.words('english')
	for item in list:
			if item not in stop_words and item.isalnum():
				list2.append(item)

	bigrams = tuple(nltk.bigrams(list2))
	freqdist = nltk.FreqDist(bigrams)

	mostfreq = freqdist.max()
	most_common = freqdist.most_common(15)
	
	print(most_common)
	
	return mostfreq
	
print(mostfreq_bigrams('my_corpus//my_text_corpus//wsj_0001.mrg'))

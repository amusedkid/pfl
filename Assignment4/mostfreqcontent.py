def mostfreq_content(filename):
	import nltk
	file = open(filename)
	text = file.read()
	list = text.split()
	list2 = []
	stop_words = nltk.corpus.stopwords.words('english')
	for item in list:
		if item not in stop_words and item.isalnum():
			list2.append(item)
	fdist = nltk.FreqDist(list2)

	mostfreq = fdist.max()

	return mostfreq

print(mostfreq_content('my_corpus//my_text_corpus//wsj_0001.mrg'))

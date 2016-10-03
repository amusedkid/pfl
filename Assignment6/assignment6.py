"""
Jose Ramirez, jramirez@brandeis.edu
LING 131A, Programming for Linguistics, Fall 2015
Assignment #6
11/10/2015
"""


import nltk
from nltk.corpus import brown

brown_words = brown.words()
brown_tagged_words = brown.tagged_words()
cfd2 = nltk.ConditionalFreqDist(brown_tagged_words)

"""
Chapter 5, Exercise 15

Write programs to process the Brown Corpus and find answers to the following questions:

1. Which nouns are more common in their plural form, rather than their singular form? (Only consider regular plurals, formed with the -s suffix.)
2. Which word has the greatest number of distinct tags. What are they, and what do they represent?
3. List tags in order of decreasing frequency. What do the 20 most frequent tags represent?
4. Which tags are nouns most commonly found after? What do these tags represent?
"""

# For Question 1:
def plurals_more_common(tagged_words_list):
# returns a list of words that are more common in their plural form
# assumes Brown corpus tag names
	cfd1 = nltk.ConditionalFreqDist(tagged_words_list)
	more_common_plurals = []
	for w in cfd1.conditions():
		# check that word is a noun and that it has a plural noun form
		if 'NN' in cfd1[w] and 'NNS' in cfd1[w+'s']:
			if cfd1[w]['NN'] < cfd1[w+'s']['NNS']: # check frequencies of singular word+tag pair vs plural word+tag pair
				more_common_plurals.append(w+'s')
	
	return sorted(more_common_plurals)

print('\n')
print("Exercise 15, Question 1: The following words in Brown are more common in their plural form:\n")
print(plurals_more_common(brown_tagged_words))
print('\n')

# For Question 2:

max_tags = 0
max_word = ""

# this for loop gives us the maximum number of tags for a word
# it also gives the word that has the maximum number of tags
for w in cfd2.conditions():
	if len(cfd2[w]) > max_tags: # compares the number of tags for each word with the maximum
		max_tags = len(cfd2[w])
		max_word = w

print("Exercise 15, Question 2:")
print("The word with the most tags is \'%s\'. It has %d tags." %(max_word, max_tags))
print("Its tags are the following:")
print(list(cfd2[max_word]))
print('\n')

"""The tags have the following meanings:
DT-NC -- determiner, emphasized word
WPS -- nominative wh-pronoun
WPO -- objective wh-pronoun
WPO-NC -- objective wh-pronoun, emphasized word
CS -- subordinating conjunction (ie. complementizer)
QL -- qualifier
CS-HL -- subordinating conjunction, headline
WPS-HL -- nominative wh-pronoun, headline
DT -- determiner
WPS-NC -- nominative wh-pronoun, emphasized word
CS-NC -- subordinating conjunction, emphasized word
NIL -- (I'm not sure about this. Neither Wikipedia nor help-tagset
explain this, though it probably means they couldn't find a tag for these tokens)

Sources:

nltk.help.brown_tagset() 

Wikipedia
https://en.wikipedia.org/wiki/Brown_Corpus#Part-of-speech_tags_used
"""


#For Question 3:

tag_fd = nltk.FreqDist(tag for (word, tag) in brown_tagged_words)
print("Exercise 15, 3: The most commmon tags in Brown\n")
print(tag_fd.most_common(20))
print('\n')


# For Question 4:

tags_after_nouns = [b[1] for (a, b) in nltk.bigrams(brown_tagged_words) if a[1] == 'NN']
fd_tags_after_nouns = nltk.FreqDist(tags_after_nouns)

print("Exercise 15, 4: The most frequently found tags after nouns:\n")
print(fd_tags_after_nouns.most_common())
print('\n')

# the most commonly found tags after are 'IN', '.', ',', 'NN', and 'CC'.
# these stand for prepositions, periods, commas, other nouns, and
# coordinating conjunctions ('and', etc)


"""
Chapter 5, Exercise 17

What is the upper limit of performance for a lookup tagger, assuming no limit to the size of its table? 
(Hint: write a program to work out what percentage of tokens of a word are assigned the most likely tag for that word, on average.)
"""

def avg_prc_likely_tags(tagged_corpus):
	# prints the average percentage in a corpus
	# of tokens of a word assigned the most likely tag in that word
	words = tagged_corpus.words()
	tagged_words = tagged_corpus.tagged_words()
	fd17 = nltk.FreqDist(words) # frequency distribution for words
	cfd17 = nltk.ConditionalFreqDist(tagged_words) # frequency of word+tag pair
	sum_percentages = 0
	for word in fd17:
		# get the frequency of words tagged with the most likely tag
		most_freq_tag_num = cfd17[word][cfd17[word].max()]
		
		# get the percentage of each word -- the number of the words
		# with the most likely tag divided by the total number of words
		percentage = most_freq_tag_num / fd17[word]
		
		# add that to our sum of percentages
		sum_percentages += percentage
	
	#divide the sum of percentages by the total number of words
	return sum_percentages/len(fd17)


brown_corpus = nltk.corpus.brown
print("Exercise 17: Average percent of tokens assigned the most likely tag of a word in Brown:\n")
print(avg_prc_likely_tags(brown_corpus))
print('\n')

"""
Chapter 5, Exercise 18

Generate some statistics for tagged data to answer the following questions:
1. What proportion of word types are always assigned the same part-of-speech tag?
2. How many words are ambiguous, in the sense that they appear with at least two tags?
3. What percentage of word tokens in the Brown Corpus involve these ambiguous words?
"""
# 1. to find the percentage of word types assigned one POS tag
# and 2. to find the number of word that are ambiguous
#brown_words = brown.words()
#brown_tagged_words = brown.tagged_words()
#cfd18 = nltk.ConditionalFreqDist(brown_tagged_words)
num_onetags = 0
num_ambiguous = 0
# check to see if a word has one, or more than one tag
for word in cfd2.conditions():
	if len(cfd2[word]) == 1:
		num_onetags += 1
	elif len(cfd2[word]) > 1:
		num_ambiguous += 1

print("Exercise 18, 1: Proportion of word types with only one POS tag:\n")
print(num_onetags / len(cfd2)) # measures the number of word with one tag divided by the total number of word types
print('\n')

print("Exercise 18, 2: Number of ambiguous words in Brown:\n")
print(num_ambiguous)
print('\n')

# 3. To find the percentage of tokens whose word type is ambiguous
num_onetagtokens = 0
num_ambtokens = 0
for token in brown_words: # this time we are looking through each word token
	if len(cfd2[token]) == 1:
		num_onetagtokens += 1
	elif len(cfd2[token]) > 1:
		num_ambtokens += 1
		
print("Exercise 18, 3: Percentage of ambiguous word tokens in Brown Corpus:\n")
# divide the number of ambiguous words by the total number of word tokens in the corpus
print(num_ambtokens/len(brown_words))
print('\n')

"""
Chapter 5, Exercise 22
We defined the regexp_tagger that can be used as a fall-back tagger for unknown words. 

This tagger only checks for cardinal numbers. 

By testing for particular prefix or suffix strings, it should be possible to guess other tags. 

For example, we could tag any word that ends with -s as a plural noun. Define a regular expression tagger (using RegexpTagger()) that tests for at least five other patterns in the spelling of words. (Use inline documentation to explain the rules.)
"""

patterns = [
	(r'.*ing$', 'VBG'),					# gerunds
	(r'.*ify$', 'VB'),					# bare form verbs
	(r'.*ize$', 'VB'),
	(r'.*ise$', 'VB'),
	(r'.*ed$', 'VBD'), 					# simple past
	(r'.*es$', 'VBZ'),					# 3rd singular present
	(r'.*ould$', 'MD'),					# modals
	(r'.*\'s$', 'NN$'),					# possessive nouns
	(r'.*s\'$', 'NNS$'),				# possessive nouns, plural
	(r'.*s$', 'NNS'),					# plural nouns
	(r'.*ly$', 'RB'),					# adverbs
	(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),		# cardinal numbers
	(r'^[1-9]+?[^1]?[1]st$', 'OD'),			# ordinal numbers
	(r'^[1-9]+?[^1]?[2]nd$', 'OD'),
	(r'^[1-9]+?[^1]?[3]rd$', 'OD'),
	(r'^[0-9]+?1[1-3]th$', 'OD'),
	(r'^[1-9]+?[4-9]th$', 'OD'),
	(r'.*', 'NN')						# nouns (default)
	]
	
regexp_tagger = nltk.RegexpTagger(patterns)

#test our regexp tagger
print("Testing the regexp_tagger for Exercise 22:\n")
print(regexp_tagger.tag("I terrify visited globalize globalise glorifying would Paul's orioles' robins wonderfully -9.9 101st 22nd 33rd 111th 212th 313th 523rd 19th 1011th".split()))
print('\n')
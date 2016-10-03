"""
Jose Ramirez, jramirez@brandeis.edu
LING 131A, Programming for Linguistics, Fall 2015
Assignment #2
10/1/2015

"""

from nltk.book import *
"""
Ch1, Exercise 23: 
Prints all of the uppercase words in the script for 
'Monty Python and the Holy Grail' (text6), one per line
"""

for word in text6:
	if word.isupper():
		print(word)
print("\n")


"""
Ch1, Exercise 24:
Prints a list of all the words in text6 that meet one of the following
conditions:
1. Ends in 'ize'
2. Contains the letter 'z'
3. Contains the sequence of letters 'pt'
4. Has all lowercase letters except for an initial capital
"""
newlist = []
for word in text6:
	if 'z' in word or 'pt' in word or word[-3:] == 'ize' or word.istitle() == True:
		newlist.append(word)
print(newlist)

print("\n")

"""Ch1, Exercise 25:
Prints all the words in the list of words 'sent' that 
1. begin with 'sh'
2. are longer than four characters.
"""
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
for word in sent:
	if word[:2] == 'sh':
		print(word)

for word in sent:
	if len(word) > 4:
		print(word)

print("\n")

"""Ch1, Exercise 27:
The function vocab_size(text) returns the vocabulary size of a text
"""

# I assume the term 'vocabulary size' refers to the number of word types
# in a text. I also assume that the text is in the form of a list.
def vocab_size(text):
# returns vocabulary size of a text
	return len(set(text))

# call function to test it	
print(vocab_size(sent))

print("\n")
	
"""Ch1, Exercise 28:
The function percent(word, text) calculates how often a given word
occurs in a text and returns the result as a percentage.
"""
# assume text is in the form of a list
def percent(word, text):
# returns the amount of times a word appears in a text as a percentage

	# count the number of times the word token appears
	count = 0
	for i in text:
		if i == word:
			count +=1
	# divide that number by the total number of word tokens in the text
	percent = (count / len(text)) * 100
	return percent
	
#call function to test it
print(percent('sea', sent))

print("\n")
	
"""
This function takes a string as input and returns a dictionary of 
ngrams and their frequencies.
"""


def ngram_freq(string, n): 
	# takes a string as input, returns a dictionary of n-grams and their
	# frequencies
	
	# 'n' parameter allows user to determine if they want bigrams,
	# trigrams, etc.
	#creates our ngrams
	
	list = string.split()
	newlist = []
	# loop by index
	for i in range(0, len(list)):
		# if statement here to make sure it knows when
		# to stop counting
		if i <= len(list) - n:
			newlist.append(list[i: i + n])
		else:
			break
	
	# creates a dictionary of ngrams as key and their frequency as value
	gramsdict = {}
	for element in newlist:
		# turn the ngrams (which are in list form) into strings in 
		# order for the dictionary to be able to work with them
		element = ' '.join(element) 
		# set the ngram as the key, and its frequency as the value
		if element in gramsdict:
			gramsdict[element] += 1
		else:
			gramsdict[element] = 1
	return gramsdict

# call our function to test it with a test string
columbus = "columbus sailed the ocean blue he discovered america columbus sailed the ocean blue consonant"
print(ngram_freq(columbus, 3))

print("\n")


"""This function takes a string as input and return the
word(s) that has the largest number of consonants in it."""

def most_consonants(string):
# returns the words in a string that have the largest number of
# consonants, as a list

	# a list of consonants -- I have included 'y' as a consonant
	consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

	#take a string as input
	list = string.split()
	
	# creates a dictionary with words as key, and number of consonants
	# as value
	word_consonants = {}
	for word in list:
		num_consonants = 0
		for letter in word:
			if letter in consonants:
				num_consonants += 1
		word_consonants[word] = num_consonants

	# finds the largest number in our dictionary
	largest_num = 0
	for key in word_consonants:
		if word_consonants[key] > largest_num:
			largest_num = word_consonants[key]
		else:
			continue
	
	# create a list of words with the largest number of consonants
	# by checking which words in our dictionary have the desired number
	# if the word has the desired number, it is added to our list of 
	# words with largest number of consonants
	most_consonant_words = []
	for key in word_consonants:
		if word_consonants[key] == largest_num:
			most_consonant_words.append(key)
		else:
			continue
	
	# return the list of words with most consonants
	return most_consonant_words

# call function to test it
print(most_consonants(columbus))

print("\n")


"""
We create a function called ‘is_determiner’ that takes a word as
input and decides if it is a determiner. 
We then use it as the argument to the built-in ‘filter’ function to eliminate all determiners in a piece of a text
"""

# A list of determiners 
# I decided to exclude numbers and fractions, possessive " 's ", 
# 'whose', 'which'
determiners = ['the', 'this', 'that', 'these', 'those', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'a', 'an', 'some', 'all', 'any', 'both', 'much', 'many', 'little', 'few', 'several', 'such', 'most', 'each', 'every', 'either', 'neither', 'another', 'no']


def is_determiner(word):
# our function has a string as its parameter, checks if the string
# matches one of our words in the determiner list. If it does, the
# function returns False. This will allow us to use it with filter to
# eliminate determiners

	if word in determiners:
		return False
	else:
		return True

# we split our string into a list so is_determiner can examine each
# word token one by one
columbus2 = columbus.split()

# use filter with is_determiner() to eliminate all determiners from our list.
# we create a new list with the remaining words in the text
newlist = list(filter(is_determiner, columbus2))

# print the modified text as a string
newstring = ' '.join(newlist)
print(newstring)

print("\n")
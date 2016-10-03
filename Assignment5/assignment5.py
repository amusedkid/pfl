"""
Jose Ramirez, jramirez@brandeis.edu
LING 131A, Programming for Linguistics, Fall 2015
Assignment #5
11/5/2015
"""

import nltk
import re
import random
from urllib import request
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.corpus import brown


"""Ch. 3 Exercise 7"""
"""Write regular expressions to match the
following classes of strings:

1. A single determiner (assume that a, an, the are the only determiners.)
2. An arithmetic expression using integers, addition and multiplication,
such as 2*3+8
"""
# Answers:
# 1. '\b([Aa]|[Aa]n|[Tt]he)\b'
# 2. '\d(?:[\+\-\*\/]\d)+'


"""Ch. 3, Exercise 8"""
"""Write a utility function that takes a URL as its argument, and
returns the contents of the URL, with all HTML markup removed.
Use from urllib import request and then request.urlopen('http: //nltk.org/').read.decode('utf-8') to access the contents of the URL"""

def clean_markup(url):
	html = request.urlopen(url).read().decode('utf8')
	raw = BeautifulSoup(html, "html.parser").get_text()
	
	return raw.encode('utf8')

text = clean_markup('http://news.bbc.co.uk/2/hi/health/2284783.stm')
print(text)
print()


"""Ch.3, Exercise 21"""
"""Write a function unknown() that takes a URL as its argument, and
returns a list of unknown words that occur on that webpage. In order
to do this, extract all substrings consisting of lowercase letters
(using re.findall()) and remove any items from this set that occur
in the Words Corpus (nltk.corpus.words)

Try to categorize these words manually and discuss your findings."""

#function takes URL as argument

def unknown(url):
	# extract all substrings consisting of lowercase letters (use re.findall)
	html = request.urlopen(url).read().decode('utf8')
	raw = BeautifulSoup(html, "html.parser").get_text()
	lowercase = re.findall(r'\b[a-z]+\b', raw)

	# remove any items from list that occur in WordsCopus
	for word in lowercase:
		if word in nltk.corpus.words.words():
			lowercase.remove(word)
			
	#returns a list of unknown words on that page
	return set(lowercase)
	
print(unknown('http://news.bbc.co.uk/2/hi/health/2284783.stm'))
print()

"""Ch.3, Exercise 23
Question: Are you able to write a regular expression to tokenize text in such a way that the word don't is tokenized into do and n't? Explain why this regular expression won't work: «n't|\w+».
"""
"""
Answer: Regular expression «n't|\w+» will not work because \w+ is greedy. 

Assuming that «n't» is written as «n\'t», when you use re.findall() on that expression, it first looks for any instances of "n't". Failing that, it will then look for any sequence of word characters. The problem
is that at the beginning, it will look for a sequence of word characters
as far as it can go. If the first word in the string is "don't", the 
first sequence of word characters is "don". After that, the next sequence it encounters is " 'nt ". It ignores the apostrophe, and finds
the sequence of word characters, "t". The same occurs with any other words of a similar type.

Using re.split will not work because there is nothing to between "do" and "n't" that you can use as a dividing line.

Unfortunately, I was unable to find a regular expression that could
tokenize text into "do" and "n't"
"""

"""Ch 3, Exercise 25
Question:
Pig Latin is a simple transformation of English text. Each word of the text is converted as follows: move any consonant (or consonant cluster) that appears at the start of the word to the end, then append ay, e.g. string → ingstray, idle → idleay. 
http://en.wikipedia.org/wiki/Pig_Latin

Write a function to convert a word to Pig Latin.
Write code that converts text, instead of individual words.
Extend it further to preserve capitalization, to keep qu together (i.e. so that quiet becomes ietquay), and to detect when y is used as a consonant (e.g. yellow) vs a vowel (e.g. style).
"""

def pig_latin(word):
	word = re.sub(r'(([^aeiou]+)?)(\w+)', r'\3\1ay', word)
	return word

print(pig_latin("string"))
print(pig_latin("idle"))
print()

# problem: for capitalization, this only works if the string is one sentence
def pig_latin_string(text):
	text = text.lower()
	text = re.sub(r'(([^aeiouyq]+)?)(\w+)\s*', r'\3\1ay ', text)
	text = re.sub(r'(y)([aeiou]+)(\w+)(ay)\s*', r'\2\3\1\4 ', text)
	text = re.sub(r'(qu)([aeiou]+)(\w+)(ay)\s*', r'\2\3\1\4 ', text)
	
	# capitalize the first character in the string
	text = text.split()
	text[0] = text[0].title()
	text = ' '.join(text)
	
	return text

s = "Yvonne was a kid once too you know she had style"
print(pig_latin_string(s))
print()


"""Chapter 3, Exercise 27"""
"""Python's random module includes a function choice() which randomly chooses an item from a sequence, e.g. choice("aehh ") will produce one of four possible characters, with the letter h being twice as frequent as the others. Write a generator expression that produces a sequence of 500 randomly chosen letters drawn from the string "aehh ", and put this expression inside a call to the ''.join() function, to concatenate them into one long string. You should get a result that looks like uncontrolled sneezing or maniacal laughter: he haha ee heheeh eha. Use split() and join() again to normalize the whitespace in this string."""

laugh = list(random.choice("aehh ") for i in range(500))
laugh = ''.join(laugh)
laugh = laugh.split()
laugh = ' '.join(laugh)
print(laugh)


"""Chapter 3, Exercise 29"""
""" Readability measures are used to score the reading difficulty of a text, for the purposes of selecting texts of appropriate difficulty for language learners. 

Let us define μw to be the average number of letters per word, and 
μs to be the average number of words per sentence, in a given text. 

The Automated Readability Index (ARI) of the text is defined to be: 4.71 μw + 0.5 μs - 21.43. 

Compute the ARI score for various sections of the Brown Corpus, including section f (lore) and j (learned). Make use of the fact that nltk.corpus.brown.words() produces a sequence of words, while nltk.corpus.brown.sents() produces a sequence of sentences.
"""

lore_words = brown.words(categories='lore')
lore_sentences = brown.sents(categories='lore')
learned_words = brown.words(categories='learned')
learned_sentences = brown.sents(categories='learned')

def get_ari(words_corpus, sentence_corpus):
	# gets Automated Readability Index of a text
	
	#get average number of letters per word
	sum_letters = 0
	for word in words_corpus:
		sum_letters += len(word)
	mw = sum_letters/len(words_corpus)

	# get average number of words per sentence
	ms = len(words_corpus)/len(sentence_corpus)

	# get ARI
	ari = (4.71 * mw) + (0.5 * ms) - 21.43
	return(ari)
	
ari_lore = get_ari(lore_words, lore_sentences)
ari_learned = get_ari(learned_words, learned_sentences)

print("\nThe ARI of section f (lore) is %f." %(ari_lore))
print("The ARI of section j (learned) is %f.\n" %(ari_learned))

 
"""Chapter 3, Exercise 34"""
"""Write code to convert nationality adjectives like Canadian and Australian to their corresponding nouns Canada and Australia (see http://en.wikipedia.org/wiki/List_of_adjectival_forms_of_place_names)
"""

# this function covers the cases "Canada"/"Australia" and several other cases
# However, it doesn't cover many exceptions including
# countries whose names end in '-ico' or '-aco': Mexico, Morocco, Monaco
# as well as China, Burma, France, and other
def nationality_to_country(nationality):
	if nationality[-5:] == "adian": #include Canada but not India
		country = re.sub(r'(\w+)(i)(a)(n)', r'\1\3', nationality)
	elif nationality[-5:] == "arian" or nationality[-6:] == "talian":
		#Hungary, Italy
		country = re.sub(r'(\w+)(ian)', r'\1y', nationality)
	elif nationality[-1:] == "i":
		country = re.sub(r'(\w+)(i)', r'\1', nationality)
	elif nationality[-4:] == "guan": # for Nicaragua
		country = re.sub(r'(\w+)(n)', r'\1', nationality)
	elif nationality[-3:] == "uan": # for Tuvalu, Vanuatu
		country = re.sub(r'(\w+)(u)(an)', r'\1\2', nationality)
	elif nationality[-3:] == "ean": # Singapore, etc.
		country = re.sub(r'(\w+)(an)', r'\1', nationality)
		
	# this set covers "-ese" However, it does not cover "Chinese"
	# or "Burmese"
	elif nationality[-4:] == "lese": # Congo, Togo
		country = re.sub(r'(\w+)(lese)', r'\1', nationality)
	elif nationality[-3:] == "ese": # Japan, Taiwan, etc.
		country = re.sub(r'(\w+)(ese)', r'\1', nationality)
		
	# this set covers some "-ish" adjectives. However, it doesn't 
	# cover cases like Swedish, Danish, or Irish
	elif nationality[-5:] == "ttish" or nationality[-5:] == "nnish":
		country = re.sub(r'(\w+)([nt])([nt])(ish)', r'\1\2land', nationality)
	elif nationality[-4:] == "tish":
		country = re.sub(r'(\w)([ia])([nt])(ish)', r'\1\2\3ain', nationality)
	elif nationality[-4:] == "nish":
		country = re.sub(r'(\w)([ia])([nt])(ish)', r'\1ain', nationality)
	else:
		country = re.sub(r'(\w+)(an)', r'\1a', nationality)
	
	return country

# testing function
nationalities = ["Australian", "Austrian", "Canadian", "Tuvaluan", "Nicaraguan", "Croatian", "Mongolian", "Pakistani", "Iraqi",
"Israeli", "Romanian", "American", "Samoan", "Mexican", "Vanuatuan",
"Singaporean", "Sierra Leonean", "Indonesian", "Indian", "Jordanian", "Russian", "Congolese", "Togolese", "Japanese", "Taiwanese", "Bhutanese", "Italian", "Hungarian", "Surinamese", "Syrian", "Palauan", "Bolivian", "Latvian", "Finnish", "Scottish", "Spanish", "British"]

for nationality in nationalities:
	print(nationality_to_country(nationality))
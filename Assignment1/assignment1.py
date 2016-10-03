"""
Jose Ramirez, jramirez@brandeis.edu
LING 131A, Programming for Linguistics, Fall 2015
Assignment #1
9/24/2015

Description: This program takes a file as input and:
1. Outputs the total number of sentences, word tokens, and word types
in the file.
2. Prints a list of word types and their frequencies.
3. Prints a list of lengths for word types and their frequencies
4. Prints a list of word frequencies and how many words occur at each
frequency.
"""

# Take a file as input
input_file = open("hw1.txt")

# turn the text in the file into a string
# and store string in 'text'
text = input_file.read()

"""Output total number of sentences"""
# assume total number of sentences equals the number of periods, question marks, and exclamation points

# count each punctuation mark as a sentence, count the number of 
# punctuation marks
num_sentences = 0
for character in text:
	if character == "." or character == "?" or character == "!":
		num_sentences += 1

print("There are %d sentences in this text." % num_sentences)

"""Output the total number of word tokens"""
# to count the number of tokens, we turn our string into a list
# and loop through it
list = text.split()
num_tokens = 0
for i in list:
	num_tokens += 1

print("There are %d word tokens." % num_tokens)


"""Output the number of word types"""
# create a new list where we strip the word tokens of all punctuation and quotes, and make all the words lowercase
# this is done to avoid repeating word types from being repeated 
# because of differences in punctuation, ie. ("romney" vs. "romney.")
list2 = []
for word in list:
	word = word.lower()
	word = word.strip("?")
	word = word.strip(".")
	word = word.strip('"')
	word = word.strip(",")
	list2.append(word)

# Create a set of word types
# creating a set will allow us to get only one of each word type
wordset = set(list2)

# Count the number of word types and print out result
num_wordtypes = 0
for element in wordset:
	num_wordtypes += 1
print("There are %d word types.\n" % num_wordtypes)


"""Print a list of word types and their frequency"""
# create a dictionary to store each word type with its frequency
# we get the frequency by counting how many times a word type appears
# in list2, which stored our word tokens
wordtypes_dict = {}
for word in list2:
	if word in wordtypes_dict:
		wordtypes_dict[word] += 1
	else:
		wordtypes_dict[word] = 1

# use a for loop to print word types and their frequency line by line
print("The following is a list of word types and their frequencies:")
for key in wordtypes_dict:
	print(key, wordtypes_dict[key])

print("\n\n\n")

"""Print a list of word lengths and their frequency"""
# create a dictionary to store the lengths of our word types and the
# frequency of each length
type_lengths = {}
for word in wordset:
	if len(word) in type_lengths:
		type_lengths[len(word)] += 1
	else:
		type_lengths[len(word)] = 1

print("The following is a list of word lengths and their frequencies:")
for length in type_lengths:
	print(length, type_lengths[length])
print("\n\n\n")

"""Print a list of word frequencies and how many words occur at each frequency"""
# create a dictionary to store word frequencies as keys, and for 
# values, the number of words that occur at each frequency
# we get our frequencies from the wordtypes_dict dictionary
frequency_list = {}
for key in wordtypes_dict:
	if wordtypes_dict[key] in frequency_list:
		frequency_list[wordtypes_dict[key]] += 1
	else:
		frequency_list[wordtypes_dict[key]] = 1

print(frequency_list)
print("The following is a list of word frequencies and how many words occur at each frequency:")
for frequency in frequency_list:
	print (frequency, frequency_list[frequency])


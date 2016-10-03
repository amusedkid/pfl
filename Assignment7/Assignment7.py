"""
Jose Ramirez, jramirez@brandeis.edu
LING 131A, Programming for Linguistics, Fall 2015
Assignment #7
11/21/2015
"""

import nltk
from nltk.corpus import treebank

# this function traverses a tree and prints it in a string format

# Note: I was unable to find a way to properly indent the subtrees
# to reflect their level in the tree. 


def treeprint3(t, spaces = 0):
	if isinstance(t, nltk.Tree):
		print(" "*spaces + "(" + t.label() + " ", end='')
	for c in t:
		if not isinstance(c, nltk.Tree):
			print(c, end= "")
		else:
			print()
			treeprint3(c, spaces + 2)
	print(")", end="")

treeprint3(treebank.parsed_sents()[0])
print('\n')
treeprint3(treebank.parsed_sents()[1])
print('\n')
treeprint3(treebank.parsed_sents()[2])
print('\n')
treeprint3(treebank.parsed_sents()[3])
print('\n')


# This function finds all the subtrees where a PP is attached to 
# an NP in the treebank corpus.
# This function only finds subtrees where the NP is labeled solely 
# as 'NP' and PPs are labeled solely as 'PP'. It does not account for
# trees where either the NP or PP are further labeled with a hyphen
# and a role

# I adapted the filter function from the NLTK book, 
# Chapter 8, Example 6.1 to look for trees with an NP label which has 
# a child with label 'PP'

# I also used the code for the subtrees function in nltk.Tree
#(http://www.nltk.org/_modules/nltk/tree.html)
# to get the subtrees.
def find_np_pp(parsed_sent_corpus):
	def subtrees(t, filter=None):
	# here I adapted the code in the nltk.Tree subtrees method
		l = []
		if not filter or filter(t):
			yield t
		for c in t:
			if isinstance(c, nltk.Tree):
				for s in subtrees(c, filter):
						yield s
	def np_pp(t): 
	# filter function for subtrees function, to return only subtrees where NP is parent and PP is child
	# adapted from the filter function in NLTK book, Chapter 8, Example 6.1
		child_nodes = [c.label() for c in t
							if isinstance(c, nltk.Tree)]
		return (t.label() == 'NP') and ('PP' in child_nodes)
	
	
	subtrees = [subtree for tree in parsed_sent_corpus
				for subtree in subtrees(tree, np_pp)]
	return subtrees

#testing out the function
print(find_np_pp(treebank.parsed_sents()[:5]))


# This function returns the subject of a sentence under two 
#conditions:
# 1. The tree entered is a matrix clause (ie. a full sentence)
#-- if the tree entered isn't a matrix clause, the function will
#return None
# 2. The sentence does in fact have a subject.
# -- if the sentence has no subject, the function will also return 
# None
def get_subject(sentence_tree):
	if sentence_tree.label() != 'S':
		return None
	else:
		for child in sentence_tree:
			if child.label() == 'NP-SBJ': 
			# I used the treebank label 'NP-SBJ', so this might not work as well with non-treebank trees
				return child
			else:
				return None
	
print(get_subject(treebank.parsed_sents()[0]))
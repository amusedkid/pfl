"""
Jose Ramirez, jramirez@brandeis.edu
LING 131A, Programming for Linguistics, Fall 2015
Assignment #8
12/1/2015
"""

import nltk, re
import os
from operator import itemgetter

"""The corpus reader class is below the mytree class"""

"""I directly added the mytree class given to us to my program.

I also added a subtrees method based on the ones we used
in class to use in some of my tree_corpus_reader methods"""

class mytree(list):

	def __init__(self, n, children=None):
		list.__init__(self, children)
		self.node = n

	def __repr__(self):
		childstr = ", ".join(repr(c) for c in self)
		return '%s(%r, [%s])' % (self.__class__.__name__, self.node, childstr)

	@classmethod
	def from_string(cls, s):
		# cls is used in place of 'self' in class methods. 'cls' for class methods
		# 'self' for instance methods
	
		#these are just a way to prevent having to write '\(', '\)' each time
		open_b = re.escape('(')
		close_b = re.escape(')')
		
		#one or more of anything but whitespace, or parentheses
		node_pattern = "[^\s%s%s]+" % (open_b, close_b)
		
		#same as above
		leaf_pattern = "[^\s%s%s]+" % (open_b, close_b)
		
		#find either a ( followed by 0 or more whitespaces, then 0 or 1 node characters (actually the ? here could be making everything to its left non-greedy
		#or a close parenthesis
		#or a leaf pattern
		token_pattern = re.compile('%s\s*(%s)?|%s|(%s)' %(open_b, node_pattern, close_b, leaf_pattern))
		
		stack = [(None,[])] # a list consisting of one tuple, which itself consists of None and a list
		for match in token_pattern.finditer(s): #if it finds a match for the pattern (ie. either an open parenthesis followed by a space, followed by a node pattern; or a close parenthesis; or a leaf
			token = match.group()
			#print(token)
			if token[0] == '(': # if the first character of the match is an open parenthesis (ie. if token is the first case in our regexp)
				node = token[1:].lstrip() #lstrip returns a copy of string with leading whitespace removed
				
				#all that's left is the node pattern (ie. 'S', 'NP', etc), which
				# becomes the left side of a tuple within of a list (similar to stack), followed by an empty list 
				# this new list is appended to stack
				stack.append((node,[]))
				#print ("push: ", stack)
			elif token == ')': # if the match is the second case, a close parenthesis
				node,children = stack.pop() #node is left element of tuple, children is list in right element. That is what is popped
				#print ("pop: ", stack)
				stack[-1][1].append(cls(node,children))#cls is class name 'mytree'
				#what is appended is 'mytree('N', ['Amy'])'
				
				#print ("push: ", stack)
			else: #ie, if it encounters the third case -- a leaf pattern
				
				# appends the leaf to the second element of the last list-element in stack
				stack[-1][1].append(token)
				#print ("push: ", stack)
	

		tree = stack[0][1][0] # removes the part in stack with None, and returns only the list on the right side
		#print(tree)
		return tree
		
	
	def subtrees(self):
		"""This was added by me"""
		l = []
		l.append(self)
		for c in self:
			if isinstance(c, mytree):
				l.extend(c.subtrees())
		return l
			


class tree_corpus_reader:
	"""The methods for the assignment are the 
	3rd, 4th, and 5th ones:
	
	corpus_word_count()
	corpus_pp_word_count()
	corpus_basenp_count()
	"""
	
	def __init__(self, directory):
		"""Instantiate the corpus object"""
		self.directory = directory
		
	def parsed_sents(self):
		"""Returns sentences in tree form
		
		Note: I use this method to turn the information in the files
		into trees that other methods can work with.
		
		This method uses the mytree class's from_string method
		
		There are a few problems with this method:
		
		I was not able to account for sentences that are quotations,
		so those are not split correctly.
		
		Also, the from_string method throws an error after the 81st file.
		
		I was unable to find the reason why, though I suspect
		it might have to do with the fact that the sentences were
		not correctly split by my regular expression due to the
		reason stated above having to do with quotations."""

		paths = os.walk(self.directory)
		parsed_sents = []
		for directory, subdirectory, files in paths:
			for i in files: #the method throws an error at the 81st file (see above)
				file = open(os.path.join(self.directory, i))
				text = file.read()
				
				# I tried using a regular expression to separate sentences
				# before applying the from_string method, in order to
				# get trees for all the sentences in the files
				# As mentioned before, it fails to account for quotations
				
				pattern = re.compile(r'\( \(S.+?\(\. \.\) (?:\(\'\' \'\'\) )\)\)', re.DOTALL)
				
				l = re.findall(pattern, text)
				
				for s in l:
					tree = mytree.from_string(s)
					parsed_sents.append(tree)
				
		return parsed_sents
			
	def corpus_word_count(self):
		"""Returns the total number of words (ie. word tokens), excluding empty 
		categories, but including punctuation, in the corpus"""
		return len(self.all_words()) #all_words method makes a list of all the words in corpus
		
	def corpus_pp_word_count(self):
		"""Returns the number of prepositions in the corpus"""
		def pp_words(t):
			"""Returns the number of prepositions in a single tree"""
			count = 0
			for s in t.subtrees():
				if 'PP' in s.node: #ensures that it doesn't get INs from subordinating conjunctions
					for c in s:
						if c.node == 'IN' or c.node == 'TO': #I included 'to' when it is a preposition
							for d in c:
								count += 1
			return count
		
		# add the numbers of words in each tree together
		corpus_pp_count = 0
		for t in self.parsed_sents():
			corpus_pp_count += pp_words(t)
		
		return corpus_pp_count
		
	def corpus_basenp_count(self):
		"""Returns the number of Base NPs in the corpus
		
		Note: I wasn't sure what exactly was meant by 'Base NP chunks',
		so I assumed it would be equivalent to Base NPs"""
		def check_np(t):
			"""Check whether a given tree has any NPs among its subtrees
			This function will be used by corpus_basenp_count"""
			np_possible = False
			for c in t:
				if not isinstance(c, mytree):
					continue
				else:
					if re.search(r'^NP(-\S)*', c.node):
						return True
					else:
						# this should allow the True values
						# if they exist, to move up the tree
						np_possible = check_np(c)
			return np_possible
		
		counter = 0
		for t in self.parsed_sents():
			for s in t.subtrees():
				np_present = check_np(s)
				#check that a subtree is an NP and that no NPs are inside
				if re.search(r'^NP(-\S)*', s.node) and np_present == False:
					counter += 1
		return counter
	
	def all_words(self):
		"""Returns all words in the corpus (ie. word tokens), excluding
		empty categories, but including punctuation
		
		Note: I used this method to help count the number of words
		in 'corpus_word_count'"""
		def words(t):
			"""This function returns the words in a single tree, which
			is then used by the all_words() method"""
			tokens = []
			if not isinstance(t, mytree):
				tokens.append(t)
			else:
				if t.node != '-NONE-':
					for c in t:
						tokens.extend(words(c))
			return tokens
		all_tokens = []
		for sent in self.parsed_sents():
			all_tokens.extend(words(sent))
		return all_tokens
		
	def fileids(self):
		"""Return a list of all documents in the corpus
		
		Note: I just threw this in there at the beginning
		to make sure my corpus reader was working properly"""
		paths = os.walk(self.directory)
		for directory, subdirectory, files in paths:
			return files
			
	
# print information using the files we were given
# because of the problems in separating sentences mentioned
# above in the parsed_sents method, the numbers will be inaccurate

treecorpus = tree_corpus_reader('treebank\\my_annotated_corpus')
parsed_sents = treecorpus.parsed_sents()
print(parsed_sents)

"""
f = open('treebank\\my_annotated_corpus\\wsj_0082.mrg')
parsed_sents = []
text = f.read()
#print(text)
#(?:\(\'\' \'\'\) )
pattern = re.compile(r'\( \(S.+?\(\. \.\) (?:\(\'\' \'\'\) )?\)\)', re.DOTALL)
l = re.findall(pattern, text)
for sent in l:
	print(sent)
	print('--------')
"""

"""
file = open('treebank\\my_annotated_corpus\\wsj_0082.mrg')
text = file.read()
#print(text)
print('\n')

# I tried using a regular expression to separate sentences
# before applying the from_string method, in order to
# get trees for all the sentences in the files
# As mentioned before, it fails to account for quotations
pattern = re.compile(r'\( \(S.+?\(\. \.\) \)\)', re.DOTALL)
l = re.findall(pattern, text)

for s in l:
	tree = mytree.from_string(s)
	print(tree)
"""
"""
tree = mytree.from_string(text)
parsed_sents.append(tree)


print("Number of words in corpus: ")
print(treecorpus.corpus_word_count())
print("Number of prepositions in corpus: ")
print(treecorpus.corpus_pp_word_count())
print("Number of Base NPs in corpus: ")
print(treecorpus.corpus_basenp_count())
"""
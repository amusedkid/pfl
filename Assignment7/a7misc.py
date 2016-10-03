"""
def treeprint(t):
	def treestring(t):
		tree = []
		if isinstance(t, nltk.Tree):
			tree.append("(" + t.label())
		for c in t:
			if not isinstance(c, nltk.Tree):
				tree.append(" " + c)
			else:
				tree.append(" ")
				tree.extend(treestring(c))
		tree.append(")")
				
		return ''.join(tree)
	print(treestring(t))
"""
"""
def treeprint2(t):
	print("(" + t.label(), end="")
	for c in t:
		if not isinstance(c, nltk.Tree):
			print(" " + c, end = "")
		else:
			print(" ", end="")
			treeprint2(c)
	print(")", end="")
"""

"""
def treeprint(t):
	def treestring(t):
		tree = []
		if isinstance(t, nltk.Tree):
			tree.append("(" + t.label())
		for c in t:
			if not isinstance(c, nltk.Tree):
				tree.append(" " + c)
			else:
				tree.append(" ")
				tree.extend(treestring(c))
		tree.append(")")
				
		return ''.join(tree)
	print(treestring(t))
	
treeprint(tree4)
print()
treeprint(treebank.parsed_sents()[0])
"""
"""
def treeprint2(t):
	print("(" + t.label(), end="")
	for c in t:
		if not isinstance(c, nltk.Tree):
			print(" " + c, end = "")
		else:
			print(" ", end="")
			treeprint2(c)
	print(")", end="")

treeprint2(tree4)
print("\n")
treeprint2(treebank.parsed_sents()[0])


"""

"""
# I applied the filter function from Chapter 8, Example 6.1
# to look for trees with an NP label which has a child with label 'PP'
def find_np_pp(tree_corpus_parsed_sents):	
	def filter(tree):
		child_nodes = [child.label() for child in tree
					if isinstance(child, nltk.Tree)]
		return (tree.label() == 'NP') and ('PP' in child_nodes)
	
	#for tree in tree_corpus_parsed_sents:
	#	for subtree in tree.subtrees(filter):
	#		print(subtree)
	
	return [subtree for tree in tree_corpus_parsed_sents
		for subtree in tree.subtrees(filter)]
		
find_np_pp(treebank.parsed_sents()[:5])
"""
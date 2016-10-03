#!/usr/bin/python

import nltk, re
from operator import itemgetter


class mytree(list):

    def __init__(self, n, children=None):
        list.__init__(self, children)
        self.node = n

    def __repr__(self):
        childstr = ", ".join(repr(c) for c in self)
        return '%s(%r, [%s])' % (self.__class__.__name__, self.node, childstr)

    @classmethod
    def from_string(cls, s):
        open_b = re.escape('(')
        close_b = re.escape(')')
        node_pattern = "[^\s%s%s]+" % (open_b, close_b)
        leaf_pattern = "[^\s%s%s]+" % (open_b, close_b)
        token_pattern = re.compile('%s\s*(%s)?|%s|(%s)' %(open_b, node_pattern, close_b, leaf_pattern))
        stack = [(None,[])]
        for match in token_pattern.finditer(s):
            token = match.group()
            #print(token)
            if token[0] == '(':
                node = token[1:].lstrip()
                stack.append((node,[]))
                print ("push: ", stack)
            elif token == ')':
                node,children = stack.pop()
                print ("pop: ", stack)
                stack[-1][1].append(cls(node,children))
                print ("push: ", stack)
            else:
                stack[-1][1].append(token)
                print ("push: ", stack)
            

        tree = stack[0][1][0]
        #print(tree)
        return tree # as 'mytree('S', [mytree('NP', ...])'

#from_string = classmethod(from_string)

tree1 = mytree.from_string("(S (NP (N Bark))(VP (V saw)(NP (NP (DT the)(N man))(PP (P in)(NP (DT the)(N park))))))")

#print(tree1)
#print(tree1[0])
        
    
        
    
        
    



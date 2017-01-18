#!/usr/bin/python

import sys, os
from collections import Counter

class myCorpus:
    """ a simple corpus class"""

    def __init__(self,corpus_dir):
        self.corpus_dir = corpus_dir
        self.fdist = self.freq_dist()

    def freq_dist(self):
        c = Counter()
        for directory,subdir,files in os.walk(self.corpus_dir):
            for f in files:
                fh = open(directory + '/' + f, 'r')
                text = fh.read().split()
                c.update(text)
        return c

        

#corpus1 = myCorpus(sys.argv[1])
#corpus1=myCorpus(r'/Users/nianwen1/teaching/ling131/ling131-fall-2015/my_text_corpus')
corpus1 = myCorpus('my_corpus//my_text_corpus')
print (max(corpus1.freq_dist().keys()))



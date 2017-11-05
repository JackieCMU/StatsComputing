import sys
from autocomplete import *
from readFile import *
from Trie import *

searchWord = sys.argv[1]
txt = sys.argv[2]
words = readFile(txt)
t  = Trie()
t.insert(words)
K = int(sys.argv[3])


print(autocomplete(searchWord, t, K))

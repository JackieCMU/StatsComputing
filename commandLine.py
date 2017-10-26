import sys
from autocomplete import *
from readFile import *
from Trie import *

searchWord = sys.argv[1]
url = sys.argv[2]
words = readFile(url)
t  = Trie()
t.insert(words, t.head)
K = int(sys.argv[3])


print(autocomplete(searchWord, t, K))
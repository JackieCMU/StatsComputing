from autocomplete import *
from Trie import *

def testComplexity(txt):
    import pandas as pd
    import time
    data = pd.read_csv(txt, sep='delimiter')
    colname = data.columns[0]
    data['number'], data['word'] = data[colname].str.split("\t").str
    data.number = data.number.astype(float)

    end = data.shape[0]*99//100
    step = data.shape[0]//100
    words, times = [], []
    for i in range(0, end//step):
        dic = list(zip(data.number[0:(i+1)*step], data.word[0:(i+1)*step]))
        start_time = time.time()
        trie = Trie()
        trie.insert(dic)
        end_time = time.time() - start_time
        words.append((i+1)*step)
        times.append(end_time)
    return words, times

words, times = testComplexity("movies.txt")
import matplotlib.pyplot as plt
plt.plot(words, times)
plt.xlabel("Number of words")
plt.ylabel("Running times")
plt.title("Performance of Trie on Movies Dataset")
plt.show()

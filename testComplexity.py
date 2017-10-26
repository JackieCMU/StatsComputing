from autocomplete import *
from Trie import *

def testComplexity(url):
    import pandas as pd
    import time
    data = pd.read_csv(url,sep='delimiter')
    colname = data.columns[0]
    data['number'], data['word'] = data[colname].str.split("\t").str
    data.number = data.number.astype(float)

    end = data.shape[0]*199//200
    step = data.shape[0]//200
    words, times = [], []
    for i in range(0, end//step):
        dic = {}
        for word, number in zip(data.word[0:(i+1)*step], data.number[0:(i+1)*step]):
            dic[word] = number
        start_time = time.time()
        trie = Trie()
        trie.insert(dic, trie.head)
        end_time = time.time() - start_time
        words.append((i+1)*step)
        times.append(end_time)
    return words, times


words, times = testComplexity("https://raw.githubusercontent.com/36-750/problem-bank/master/Data/autocomplete-me/movies.txt?token=ARUJAJaKiYC6TeiJn-KqZUWT4lX9XG3Lks5Z-NKZwA%3D%3D")

import matplotlib.pyplot as plt
plt.plot(words, times)
plt.xlabel("Number of words")
plt.ylabel("Running times")
plt.title("Performance of Trie on Movies Dataset")
plt.show()

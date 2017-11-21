import collections as cl

def makeBoW(wordList, lexicon):
    '''
    wordList: a list of all words in the documents
    lexicon: a list of words
    return: an ordered dictionary with word as key
    list of count as value
    '''
    bagWords = cl.OrderedDict()
    for subwordList in wordList:
        if bagWords:
            for item in lexicon:
                bagWords[item] = [subwordList.count(item)]
        else:
            for item in lexicon:
                bagWords[item].append(subwordList.count(item))
    return bagWords

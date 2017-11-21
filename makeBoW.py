import collections as cl

def makeBoW(wordList, lexicon):
    '''
    wordList: a list of all words in the documents
    lexicon: a list of words
    return: an ordered dictionary with word as key
    list of count as value
    '''
    bagWords = cl.OrderedDict()
    first = True
    for subwordList in wordList:
        if first:
            for item in lexicon:
                bagWords[item] = [subwordList.count(item)]
            first = False
        else:
            for item in lexicon:
                bagWords[item].append(subwordList.count(item))
    return bagWords

import collections as cl

def makeBoW(wordList, lexicon):
    '''
    wordList: a list of all the world in the documents
    lexicon: a list of words
    return: an ordered dictionary con
    '''
    bagWords = cl.OrderedDict()
    count = 0
    for subwordList in wordList:
        if count == 0:
            for item in lexicon:
                bagWords[item] = [subwordList.count(item)]
            count += 1
        else:
            for item in lexicon:
                bagWords[item].append(subwordList.count(item))
    return bagWords

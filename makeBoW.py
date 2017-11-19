def makeBoW(wordList, lexicon):
    bagWords = {}
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
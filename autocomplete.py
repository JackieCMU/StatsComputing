# 1. Use PriorityQueue to find the node with the minimum of negative maxWeight
# 2. First check whether the word we want to search exists or not
# 3. get item
    # 4. if it is a word and having children
        # 5. if its weight is max, add it to result
        # 6. add its children
    # 7. if it is a word without children
        # 8. add it to result
    # 9. if it is not a word
        # 10. add its children
# 6. when PriorityQueue is empty or finding K words, return the result

def autocomplete(character, trie, K):
    '''
    character: the character, should be string
    trie: Trie
    K: number, should be int
    return: a List with tuple paired by weight and word
    '''

    # if node.word is a word and having children, add maxWeight, word, node
    # if node.word is a word and not having children, add weight, word
    # else add maxWeight, node
    def help(dic, q):
        '''
        dic: should be node.child
        q: PriorityQueue
        '''
        for word in dic:
            if dic[word].weight >= 0 and len(dic[word].children) != 0:
                q.put((-dic[word].maxWeight, word, dic[word]))
            elif dic[word].weight >= 0:
                q.put((-dic[word].weight, word))
            else:
                q.put((-dic[word].maxWeight, dic[word]))

    count = 0
    import queue
    q = queue.PriorityQueue()
    result = []
    node = trie.search(character)
    if node is None:                            # add the first node
        return "This word does not exist"
    elif node.weight >= 0:
        q.put((-node.weight, node.word))
    else:
        q.put((-node.maxWeight, node))
    help(node.children, q)
    while count < K:
        item = q.get()
        if len(item) == 3:                      # if node.word is word and having children
            if -item[0] == item[2].weight:      # if its weight is max, add weight and word
                result.append((int(-item[0]), item[1]))
                count += 1
            help(item[2].children, q)           # add its children
        elif type(item[1]) == str:              # if it's a word and without children
            result.append((int(-item[0]), item[1]))
            count += 1
        else:
            help(item[1].children, q)
        if q.empty():
            print("Only have " + str(len(result)) + " words")
            return result
    return result
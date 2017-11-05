# 1. Use PriorityQueue to find the node with the minimum of negative maxWeight
# 2. First check whether the word we want to search exists or not
# 3. Check whether it is a word:
    # 4. if word, return its weight, word and node into a PriorityQueue, repeat 3
    # 5. Else add all its children's maxWeight, word and node into PriorityQueue
# 6. when PriorityQueue is empty or finding K words, return the result

def autocomplete(character, trie, K):
    '''
    character: the character, should be string
    tire: Tire
    K: number, should be int
    return: a List with tuple paired by weight and word
    '''

    # add node's all children into PriorityQueue
    def help(dic, q):
        '''
        dic: should be node.child
        q: PriorityQueue
        return: PriorityQueue added by new items
        '''
        for word in dic:
            if dic[word].weight >= 0:
                q.put((-dic[word].weight, word, dic[word]))
                help(dic[word].children, q)
            else:
                q.put((-dic[word].maxWeight, word, dic[word]))

    # reset all visited node's visited as False for reuse
    def restore(nodeList):
        '''
        nodeList: nodes of output
        '''
        for item in nodeList:
            item.visited = False

    count = 0
    import queue
    q = queue.PriorityQueue()
    result, outputNodes = [], []            # result: the autocomplete result, outputNodes: restore visited Node
    node = trie.search(character)
    if node is None:
        return "This word does not exist"
    elif node.weight >= 0:
        q.put((-node.weight, node.word, node))
    else:
        q.put((-node.maxWeight, node.word, node))
    help(node.children, q)
    while count < K:
        node = q.get()[2]
        if node.weight < 0:         # if node.word is not a word
            help(node.children, q)
        elif not node.visited and node.weight >= 0:         # if node.word is a non-visited word
            result.append((int(node.weight), node.word))
            outputNodes.append(node)
            node.visited = True
            help(node.children, q)
            count += 1
        if q.empty():
            print("Only have " + str(len(result)) + " words")
            restore(outputNodes)
            return result
    restore(outputNodes)
    return result
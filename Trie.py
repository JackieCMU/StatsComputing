# initial a Node
class Node:
    def __init__(self, word = None, ownWeight = -float("inf"), maxWeight = -float("inf")):
        '''
        word: a character as 'A', 'apple'
        ownWeight: -inf if not a word else its weight
        child: dictionary, key is character, value is node
        maxWeight: its maxWeight
        isWord: False if it is not a word else True
        visited: function in autocomplete.py
        '''
        self.word = word
        self.ownWeight = ownWeight
        self.child = {}
        self.maxWeight = maxWeight
        self.isWord = False
        self.visited = False

    def wordExist(self, letter, ownWeight):
        '''
        if the sliced character is the existed letter
        node's ownWeight would be input ownWeight
        node's isWord would be True
        add maxWeight every time, convenient for comparing with existed nodes' maxWeight
        '''
        if self.word == letter:
            self.ownWeight = ownWeight
            self.isWord = True
        self.maxWeight = ownWeight

    def isWords(self):
        '''
        check whether type of input word is string
        return: True or False
        '''
        return isinstance(self.word, str)

    def isDigits(self):
        '''
        check whether type of node's ownWeight and maxWeight is float
        return: True or False
        '''
        return isinstance(self.ownWeight, float) & isinstance(self.maxWeight, float)


# Initial a node every time
# If the node is new, add it into the dictionary
    # renew the currentNode
# If the node exists, compare its weight with the existed ones'
    # update the existed node, renew the currentNode
# Return to the head if completing the certain word
class Trie:
    def __init__(self, head=None):
        self.head = Node(head)

    def insert(self, dic, currentNode):
        '''
        dic: dictionary of inputs, key is word, value is weight
        currentNode: should be tire.head
        return: Trie
        '''
        while len(dic) > 0:
            pair = dic.popitem()
            weight, letter = pair[1], pair[0]
            for i in range(len(letter)):
                node = Node(letter[:i + 1])
                node.wordExist(letter, weight)
                if node.word not in currentNode.child:
                    currentNode.child[node.word] = node
                    currentNode = node
                else:
                    nodeExist = currentNode.child[node.word]
                    if node.ownWeight != -float("inf"):
                        nodeExist.ownWeight = node.ownWeight
                        nodeExist.isWord = True
                    if node.maxWeight > nodeExist.maxWeight:
                        nodeExist.maxWeight = node.maxWeight
                    currentNode = nodeExist
            currentNode = self.head

    # find the node with the word as what we want to search
    def search(self, trie, character):
        '''
        tire: should be tire.head
        character: the character we want to search, should be a string
        return: node with word as character
        '''
        count = 1
        while count <= len(character):
            trie = [trie.child[word] for word in trie.child if word == character[:count]]
            if len(trie) == 0:
                return None     # if character doesn't exist, return None
            trie = trie[0]
            count += 1
        return trie

    def randomInsert(self, dic, currentNode):
        '''
        almost same as insert except for random pop
        '''
        import random
        while len(dic) > 0:
            letter = random.choice(list(dic.keys()))
            weight = dic.pop(letter)
            for i in range(len(letter)):
                node = Node(letter[:i + 1])
                node.wordExist(letter, weight)
                if node.word not in currentNode.child:
                    currentNode.child[node.word] = node
                    currentNode = node
                else:
                    nodeExist = currentNode.child[node.word]
                    if node.ownWeight != -float("inf"):
                        nodeExist.ownWeight = node.ownWeight
                        nodeExist.isWord = True
                    if node.maxWeight > nodeExist.maxWeight:
                        nodeExist.maxWeight = node.maxWeight
                    currentNode = nodeExist
            currentNode = self.head
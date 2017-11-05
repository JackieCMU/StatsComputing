class Node:
    def __init__(self, word = None, maxWeight = -float("inf"), weight = -float("inf")):
        '''
        word: a character as 'A', 'apple'
        child: dictionary, key is character, value is node
        maxWeight: its maxWeight
        weight: its weight if it is a word
        visited: function in autocomplete.py
        '''
        self.word = word
        self.children = {}
        self.maxWeight = maxWeight
        self.weight = weight
        self.visited = False

    def isWords(self):
        '''
        check whether type of input word is string
        return: True or False
        '''
        return isinstance(self.word, str)

    def isDigits(self):
        '''
        check whether type of node's maxWeight is float
        return: True or False
        '''
        return isinstance(self.weight, float) & isinstance(self.maxWeight, float)

class Trie:
    def __init__(self):
        self.head = Node()

    # insert all words from a dictionary
    def insert(self, wordPairs):
        '''
        dic: dictionary of inputs, key is word, value is weight
        '''
        for i in range(len(wordPairs)):
            wordPair = wordPairs[i]
            self.__insert(wordPair, self.head)

    # Initial a node every time
    # If the node is new, add it into the dictionary
    # renew the currentNode
    # If the node exists, compare its maxWeight with the existed ones'
    # update the existed node, renew the currentNode
    # if it is a word, update the existed node's weight
    def __insert(self, wordPair, currentNode):
        '''
        wordPair: word and its weight
        tire: built Tire
        '''
        weight, word = wordPair[0], wordPair[1]
        for i in range(len(word)):
            node = Node(word[:i + 1], weight)
            if i == len(word) - 1:
                node.weight = weight
            if node.word not in currentNode.children:
                currentNode.children[node.word] = node
                currentNode = node
            else:
                nodeExist = currentNode.children[node.word]
                if node.maxWeight > nodeExist.maxWeight:
                    nodeExist.maxWeight = node.maxWeight
                if node.weight >= 0:
                    nodeExist.weight = node.weight
                currentNode = nodeExist
                
    # find the node with the word as what we want to search
    def search(self, character):
        '''
        tire: should be tire.head
        character: the character we want to search, should be a string
        return: node with word as character
        '''
        node = self.head
        for i in range(len(character)):
            if character[:i+1] in node.children.keys():
                node = node.children[character[:i+1]]
            else:
                return None     # if character doesn't exist, return None
        return node

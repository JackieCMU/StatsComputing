class Node:
    # make a node with value, left child and right child
    
    def __init__(self, value = None, left = None, right = None):
        self.left = left
        self.value = value
        self.right = right

class binary_tree:
    
    # root can be regarded as a node
    def __init__(self, root = None):
        self.root = root
    
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.__insert(self.root, value)

    # use recursive to make a tree to make sure small value is on the left and large value is on the right
    def __insert(self, currentNode, value):
        if value <= currentNode.value:
            if currentNode.left == None:
                currentNode.left = Node(value)
            else:
                self.__insert(currentNode.left, value)
        else:
            if currentNode.right == None:
                currentNode.right = Node(value)
            else:
                self.__insert(currentNode.right, value)

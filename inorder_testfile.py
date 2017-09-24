from inorder import inorderTraversal
from inorder import visitfn
from binary_tree import Node
from binary_tree import binary_tree
import unittest

tree1 = binary_tree()

tree1.insert('D')
tree1.insert('A')
tree1.insert('E')
tree1.insert('B')
tree1.insert('G')

tree2 = binary_tree()

tree2.insert(8)
tree2.insert(3)
tree2.insert(10)
tree2.insert(14)
tree2.insert(13)
tree2.insert(1)
tree2.insert(6)

tree3 = binary_tree()

tree3.insert(9)
tree3.insert(4)
tree3.insert(6)
tree3.insert(2)
tree3.insert(1)
tree3.insert(10)
tree3.insert(18)


class TestStringMethods(unittest.TestCase):
    def test_equal(self):
        self.assertTrue(inorderTraversal(tree1.root, visitfn) == ['A', 'B', 'D', 'E', 'G'])
        self.assertTrue(inorderTraversal(tree2.root, visitfn) == [1, 3, 6, 8, 10, 13, 14])
        self.assertTrue(inorderTraversal(tree3.root, visitfn) == [1, 2, 4, 6, 9, 10, 18])

if __name__ == '__main__':
    unittest.main()




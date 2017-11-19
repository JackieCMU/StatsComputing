from tokenize import *
from makeBoW import *
import unittest

class TestStringMethods(unittest.TestCase):

    def test_makeBoW(self):
        path = 'testfile'
        wordList = tokenize(path)
        self.assertEquals(makeBoW(wordList, ['my', 's', 'is']),
                          {'my':[1, 1, 0], 's':[0, 0, 2], 'is':[1, 2, 0]})
        self.assertEquals(makeBoW(wordList, ['j']), {'j':[0, 0, 0]})

if __name__ == '__main__':
    print(unittest.main())

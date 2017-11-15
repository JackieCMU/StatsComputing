from tokenize import *
import unittest

class TestStringMethods(unittest.TestCase):

    def test_wordList(self):
        path = 'testfile'
        wordList = tokenize(path)
        self.assertEquals(wordList[0], ['Hi', 'my', 'name', 'is', 'Jacky', 'I',
                                         'am', 'from', 'Shanghai', 'China'])
        self.assertEquals(wordList[1], ['Oh', 'my', 'favorite', 'basketball',
                                         'player', 'is', 'Lebron', 'James',
                                        'As', 'his', 'fans', 'I', 'still',
                                        'think', 'his', 'chosen', 'one', 'is','stupid'])
        self.assertEquals(wordList[2], ['s', 's', 'wow'])

if __name__ == '__main__':
    print(unittest.main())
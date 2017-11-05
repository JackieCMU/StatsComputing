from autocomplete import *
from readFile import *
from Trie import *
import unittest


class TestStringMethods(unittest.TestCase):
    def test_Node(self):
        node1, node2  = Node(), Node()
        node1.weight, node2.maxWeight = 1.0, 3000.0
        self.assertTrue(Node(1).isWords() == False)         # word is not a string: return False
        self.assertTrue(Node("apple").isWords() == True)    # word is a string: return True
        self.assertTrue(node1.isDigits() == True)          # word's weight is a digit: return True
        self.assertTrue(node2.isDigits() == True)          # word's maxWeight is a digit: return True

    def test_Trie(self):
        trie1 = Trie()
        trie2 = Trie()
        trie2.insert([(2, 'a')])
        trie2.insert([(12, "a"), (10, "apt")])
        self.assertTrue(trie1.head is not None)                 # trie1.head is not None: return False
        self.assertTrue(len(trie2.head.children) == 1)         # trie2.head.child has only a, the length should be 1
        self.assertTrue(trie2.head.children["a"].weight == 12)  # the maxWeight of word "a" should be its weight
        self.assertTrue(trie2.head.children["a"].weight == 12)  # the ownWeight of "a" is 12
        self.assertTrue(trie2.head.children["a"].children["ap"].weight == -float("inf")) # "ap" is not a word, thus it has no ownWeight

    def test_autocomplete(self):
        '''
        For testing autocomplete with 3 text file
        I use pandas to extract the expected result
        method: data[data.word.map(lambda x : x.startswith(character)]
        '''
        # wiki
        word1 = readFile('wiktionary.txt')
        trie1 = Trie()
        trie1.insert(word1)

        self.assertTrue(autocomplete("the", trie1, 5) == [(5627187200, "the"),
                                                       (334039800, "they"),
                                                       (282026500, "their"),
                                                       (250991700, "them"),
                                                       (196120000, "there")])
        self.assertTrue(autocomplete("T", trie1, 1) == "This word does not exist")
        self.assertTrue(autocomplete(" ", trie1, 1) == "This word does not exist")
        self.assertTrue(autocomplete('it', trie1, 5) == [(805811000, 'it'),
                                                      (137327000, 'its'),
                                                      (25125200, 'itself'),
                                                      (5532790, 'italy'),
                                                      (4702180, 'italian')])

        word2 = [(2, "a"), (19, "apple"), (10, "age"), (1, "action")]
        trie2 = Trie()
        trie2.insert(word2)

        self.assertTrue(autocomplete("a", trie2, 2) == [(19, "apple"), (10, "age")])
        self.assertTrue(autocomplete("a", trie2, 3) == [(19, "apple"), (10, "age"), (2, "a")])
        self.assertTrue(autocomplete("d", trie2, 1) == "This word does not exist")
        # pokemon
        word3 = readFile('pokemon.txt')
        trie3 = Trie()
        trie3.insert(word3)

        self.assertTrue(autocomplete("Tyrunt", trie3, 1) == [(0, "Tyrunt")])

        # movie
        word4 = readFile('movies.txt')
        trie4 = Trie()
        trie4.insert(word4)

        self.assertTrue(autocomplete('Iron Man (2008)', trie4, 5) == [(318412101, 'Iron Man (2008)'),
                                                                    (0, 'Iron Man (2008) (VG)')])

        word5 = [(5, "i"), (10, "in"), (8, "inn")]
        trie5 = Trie()
        trie5.insert(word5)
        word6 = [(5, "i"), (8, "inn")]
        trie6 = Trie()
        trie6.insert(word6)

        self.assertTrue(autocomplete("i", trie5, 1) == [(10, "in")])
        self.assertTrue(autocomplete("i", trie6, 1) == [(8, "inn")])

    def randomized_Test(self):

        # compare result of sort method with result of autocomplete method
        def testEqual(letter, count, character, K):
            '''
            letter: like a,b c
            count: number, should be int, produce the number of words
            character: the character we want to search
            K: number, should be int
            return: True or False
            '''
            from random_words import RandomWords
            import random
            w = RandomWords()
            words = w.random_words(letter, count)           # random words
            words = list(set(words))            # use set to make sure the word is unique
            weights = random.sample(range(1, 5*len(words)), len(words))         # random weights
            wordPairs = list(zip(weights, words))      # build a list of word with weights
            extractWord = [wordPair for wordPair in wordPairs if wordPair[1].startswith(character)]
            sortWord = sorted(extractWord, key = lambda x : x[0], reverse = True)
            trie = Trie()
            trie.insert(wordPairs)
            return(autocomplete(character, trie, K) == sortWord[:K])

        self.assertTrue(testEqual('r', 100, 're', 5))
        self.assertTrue(testEqual('a', 100, 'au', 3))

if __name__ == '__main__':
    print(unittest.main())


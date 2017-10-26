from autocomplete import *
from readFile import *
from Trie import *
import unittest


class TestStringMethods(unittest.TestCase):
    def test_Node(self):
        node1, node2, node3 = Node(), Node(), Node()
        node1.ownWeight = "pineapple"
        node2.maxWeight = "pineapple"
        node3.ownWeight, node3.maxWeight = 1.0, 3000.0
        self.assertTrue(Node(1).isWords() == False)         # word is not a string: return False
        self.assertTrue(Node("apple").isWords() == True)    # word is a string: return True
        self.assertTrue(node1.isDigits() == False)          # word's ownWeight is not digit: return False
        self.assertTrue(node2.isDigits() == False)          # word's maxWeight is not digit: return False
        self.assertTrue(node3.isDigits() == True)           # word's ownWeight and maxWeight are digit: return True

    def test_Trie(self):
        trie1 = Trie('a')
        trie2 = Trie()
        trie2.insert({"a":12, "apt":10}, trie2.head)
        self.assertTrue(trie1.head != None)                 # trie1.head is not None: return False
        self.assertTrue(len(trie2.head.child) == 1)         # trie2.head.child has only a, the length should be 1
        self.assertTrue(trie2.head.child["a"].maxWeight == 12)  # the maxWeight of word "a" should be its weight
        self.assertTrue(trie2.head.child["a"].ownWeight == 12)  # the ownWeight of "a" is 12
        self.assertTrue(trie2.head.child["a"].child["ap"].ownWeight == -float("inf")) # "ap" is not a word, thus it has no ownWeight


    def test_autocomplete(self):
        '''
        For testing autocomplete with 3 text file
        I use pandas to extract the expected result
        method: data[data.word.map(lambda x : x.startswith(character)]
        '''
        # wik
        url1 = "https://raw.githubusercontent.com/36-750/problem-bank/master/Data/autocomplete-me/wiktionary.txt?token=ARUJAJICT79w7UYdyPkOwkLc051I6m58ks5Z-NWdwA%3D%3D"
        word1 = readFile(url1)
        trie1 = Trie()
        trie1.insert(word1, trie1.head)

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

        word2 = {"a": 2, "apple": 19, "age": 10, "action": 1}
        trie2 = Trie()
        trie2.insert(word2, trie2.head)

        self.assertTrue(autocomplete("a", trie2, 2) == [(19, "apple"), (10, "age")])
        self.assertTrue(autocomplete("a", trie2, 3) == [(19, "apple"), (10, "age"), (2, "a")])

        # pokemon
        url2 = "https://raw.githubusercontent.com/36-750/problem-bank/master/Data/autocomplete-me/pokemon.txt?token=ARUJAHbAMUKyu88FixNfivQV5cPHVeCtks5Z-NVswA%3D%3D"
        word3 = readFile(url2)
        trie3 = Trie()
        trie3.insert(word3, trie3.head)

        self.assertTrue(autocomplete("Tyrunt", trie3, 1) == [(0, "Tyrunt")])

        # movie
        url3 = "https://raw.githubusercontent.com/36-750/problem-bank/master/Data/autocomplete-me/movies.txt?token=ARUJAJaKiYC6TeiJn-KqZUWT4lX9XG3Lks5Z-NKZwA%3D%3D"
        word4 = readFile(url3)
        trie4 = Trie()
        trie4.insert(word4, trie4.head)

        self.assertTrue(autocomplete('Iron Man (2008)', trie4, 5) == [(318412101, 'Iron Man (2008)'),
                                                                    (0, 'Iron Man (2008) (VG)')])

        word5 = {"i":5, "in":10, "inn":8}
        trie5 = Trie()
        trie5.insert(word5, trie5.head)
        word6 = {"i":5, "inn":8}
        trie6 = Trie()
        trie6.insert(word6, trie6.head)

        self.assertTrue(autocomplete("i", trie5, 1) == [(10, "in")])
        self.assertTrue(autocomplete("i", trie6, 1) == [(8, "inn")])

        # wiki: randomized test
        wordA, wordB, wordC = readFile(url1), readFile(url1), readFile(url1)
        trieA, trieB, trieC = Trie(), Trie(), Trie()
        trieA.randomInsert(wordA, trieA.head)
        trieB.randomInsert(wordB, trieB.head)
        trieC.randomInsert(wordC, trieC.head)
        self.assertTrue(autocomplete("the", trieA, 5) == autocomplete("the", trieB, 5) == autocomplete("the", trieC, 5))



if __name__ == '__main__':
    print(unittest.main())


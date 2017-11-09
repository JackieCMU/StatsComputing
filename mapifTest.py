from mapif import *
import unittest

class TestStringMethods(unittest.TestCase):

    def mapif_test(self):
        s = [1,2,4,9]
        self.assertTrue(mapif(s, lambda x : x % 2 == 0, lambda x : x*2) == [1,4,8,18])

    def partition_test(self):
        s = [1,2,3,4,5,6,7,8]
        size = 4
        self.assertTrue(partition(s, size) == [[1,2,3,4],[5,6,7,8]])
        self.assertTrue(partition(s, size, 2) == [[1,2,3,4],[3,4,5,6],[5,6,7,8],[7,8]])
        self.assertTrue(partition(s, size, 5) == [[1,2,3,4],[6,7,8]])
        self.assertTrue(partition(s, size, 100) == [1,2,3,4])

if __name__ == '__main__':
    print(unittest.main())
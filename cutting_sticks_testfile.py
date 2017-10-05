import unittest
from cutting_sticks import *

class TestStringMethods(unittest.TestCase):
    def test_equal(self):
        self.assertTrue(best_cuts(100, [25, 50, 75]) == (200, [50, 25, 75]))
        self.assertTrue(best_cuts(10, [4, 5, 7, 8]) == (22, [4, 7, 5, 8]))
        self.assertTrue(best_cuts(10, [2, 4, 7]) == (20, [4, 2, 7]))

if __name__ == '__main__':
    unittest.main()

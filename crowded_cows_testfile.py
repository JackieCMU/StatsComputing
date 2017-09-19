import unittest


class TestStringMethods(unittest.TestCase):
    def test_equal(self):
        self.assertTrue(crowded_cows([7, 3, 4, 2, 3, 4], 3) == 4)
        self.assertTrue(crowded_cows([7, 3, 4, 2, 3, 10, 4], 3) == 3)
        self.assertTrue(crowded_cows([7, 3, 1, 0, 4, 2, 16, 28, 3, 4], 3) == -1)

if __name__ == '__main__':
    unittest.main()

from blink import blink
from blink import add

import unitest

class TestStringMethods(unittest.TestCase):
    def test_equal(self):
        self.assertTrue(blink([1, 0, 0], 4) == [1, 1, 0])
        self.assertTrue(blink([1, 0, 0, 0], 4) == [0, 0, 0, 0])
        self.assertTrue(blink([1, 0, 0, 0], 24) == [0, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()

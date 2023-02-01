import unittest
from hw3 import find_pairs_naive, find_pairs_optimized

class TestFindPair(unittest.TestCase):

    list1 = [1, 2, 3, 4]
    target1 = 4
    set1 = {()}

   

    def test_naive(self):
        self.assertEqual( find_pairs_naive([1, 3, 4, 0], 4), { (1, 3), (4, 0) } )

    def test_optimized(self):
        self.assertEqual( find_pairs_optimized([1, 3, 4, 0], 4), { (1, 3), (4, 0) } )

if __name__ == "__main__":
    unittest.main()
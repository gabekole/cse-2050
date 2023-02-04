import unittest
from hw3 import find_pairs_naive, find_pairs_optimized

class TestFindPair(unittest.TestCase):

    input_list_1 = [1, 3, 4, 0]
    input_target_1 = 4
    result_set_1 = { (1, 3), (4, 0) }

    input_list_2 = [16, 21, 31, 4]
    input_target_2 = 10
    result_set_2 = set()

    input_list_3 = []
    input_target_3 = 1
    result_set_3 = set()

    input_list_4 = [1, 3, 2, 5, 0]
    input_target_4 = 5
    result_set_4 = { (3, 2), (5, 0) }

   

    def test_naive(self):
        self.assertEqual( find_pairs_naive(TestFindPair.input_list_1, TestFindPair.input_target_1 ), TestFindPair.result_set_1 )
        self.assertEqual( find_pairs_naive(TestFindPair.input_list_2, TestFindPair.input_target_2 ), TestFindPair.result_set_2 )
        self.assertEqual( find_pairs_naive(TestFindPair.input_list_3, TestFindPair.input_target_3 ), TestFindPair.result_set_3 )
        self.assertEqual( find_pairs_naive(TestFindPair.input_list_4, TestFindPair.input_target_4 ), TestFindPair.result_set_4 )

    def test_optimized(self):
        self.assertEqual( find_pairs_optimized(TestFindPair.input_list_1, TestFindPair.input_target_1 ), TestFindPair.result_set_1 )
        self.assertEqual( find_pairs_optimized(TestFindPair.input_list_2, TestFindPair.input_target_2 ), TestFindPair.result_set_2 )
        self.assertEqual( find_pairs_optimized(TestFindPair.input_list_3, TestFindPair.input_target_3 ), TestFindPair.result_set_3 )
        self.assertEqual( find_pairs_optimized(TestFindPair.input_list_4, TestFindPair.input_target_4 ), TestFindPair.result_set_4 )

if __name__ == "__main__":
    unittest.main()
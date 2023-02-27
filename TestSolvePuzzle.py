from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""
                # self.assertTrue(puzzle([1, 0]))
                # self.assertTrue(puzzle([2, 0, 0]))
                # self.assertTrue(puzzle([1, 1, 3]))
                # self.assertTrue(puzzle([1, 2, 1, 2]))

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
                self.assertTrue(puzzle([1, 0]))
                self.assertTrue(puzzle([1, 0, 0]))
                self.assertTrue(puzzle([1, 2, 5, 1, 2, 1, 0]))

        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""
                self.assertTrue(puzzle([5, 3, 1, 2, 4, 2, 1, 0]))
                self.assertTrue(puzzle([2, 4, 1, 24, 0, 9]))
                self.assertTrue(puzzle([4, 1, 2, 3, 4]))
                self.assertTrue(puzzle([49, 1, 5, 9, 10]))
                
                
        
        def testUnsolveable(self):
                """Tests an unsolveable board"""
                self.assertFalse(puzzle([7, 1, 2, 3, 2, 9, 99]))
                self.assertFalse(puzzle([6, 0, 0, 1, 2, 5]))
                self.assertFalse(puzzle([5, 4, 1, 2, 0, 0, 0, 8, 10]))
                self.assertFalse(puzzle([0, 0]))

unittest.main()
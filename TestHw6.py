import unittest
from hw6 import find_zero, sort_halfsorted, bubble, selection, insertion
from TestHelpers import generate_halfsorted, is_sorted 

class Test_SortHalfSorted(unittest.TestCase):
   L1 = [-1, -10, -2, 0, 2, 5, 4]
   L1_sorted = [-10, -2, -1, 0, 2, 4, 5]

   L2 = [-1, 0, 1]
   L2_sorted = [-1, 0, 1]

   L3 = [0]
   L3_sorted = [0]

   L4 = [0, 1, 5, 2]
   L4_sorted = [0, 1, 2, 5]

   L5 = [-10, -1, -5, -15, 0]
   L5_sorted = [-15, -10, -5, -1, 0]

   def test_halfsorted_bubble(self):
      # use sort_halfsorted(L, bubble) to test

      self.assertEqual(bubble(L=self.L1, left=0, right=0), self.L1_sorted)
      self.assertEqual(bubble(L=self.L2, left=0, right=0), self.L2_sorted)
      self.assertEqual(bubble(L=self.L3, left=0, right=0), self.L3_sorted)
      self.assertEqual(bubble(L=self.L4, left=0, right=0), self.L4_sorted)
      self.assertEqual(bubble(L=self.L5, left=0, right=0), self.L5_sorted)

   def test_halfosrted_selection(self):
      # use sort_halfsorted(L, selection) to test

      self.assertEqual(selection(L=self.L1, left=0, right=0), self.L1_sorted)
      self.assertEqual(selection(L=self.L2, left=0, right=0), self.L2_sorted)
      self.assertEqual(selection(L=self.L3, left=0, right=0), self.L3_sorted)
      self.assertEqual(selection(L=self.L4, left=0, right=0), self.L4_sorted)
      self.assertEqual(selection(L=self.L5, left=0, right=0), self.L5_sorted)

   def test_halfsorted_insertion(self):
      # use sort_halfsorted(L, insertion) to test

      self.assertEqual(insertion(L=self.L1, left=0, right=0), self.L1_sorted)
      self.assertEqual(insertion(L=self.L2, left=0, right=0), self.L2_sorted)
      self.assertEqual(insertion(L=self.L3, left=0, right=0), self.L3_sorted)
      self.assertEqual(insertion(L=self.L4, left=0, right=0), self.L4_sorted)
      self.assertEqual(insertion(L=self.L5, left=0, right=0), self.L5_sorted)

# Test provided for you
class Test_FindZero(unittest.TestCase):
   def test1_allLengthsAllIndices(self):
      '''Tests find_zero for every possible index, for lists from 1 to 100 items

         Lists
         -----
            '-' and '+' denote negative and positive ingeters, respectively
                                 idx_zero
            n = 1                
               L = [0]           0

            n = 2
               L = [0, +]        0
               L = [-, 0]        1

            n = 3                
               L = [0, +, +]     0
               L = [-, 0, +]     1  
               L = [-, -, 0]     2

            n = 4
               L = [0, +, +, +]  0
               L = [-, 0, +, +]  1
               L = [-, -, 0, +]  2
               L = [-, -, -, 0]  3
            ...
            n = 100
               L = [0, ..., +]   0
               ...
               L = [-, ..., 0]   99
      '''

      # note the use of `subTest`. These all count as 1 unittest if they pass,
      # but all that fail will be displayed independently
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        L, idx_zero = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                        self.assertEqual(find_zero(L), idx_zero)

unittest.main()


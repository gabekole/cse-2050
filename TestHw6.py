import unittest
from hw6 import find_zero, sort_halfsorted, bubble, selection, insertion
from TestHelpers import generate_halfsorted, is_sorted 
from random import randint

class Test_SortHalfSorted(unittest.TestCase):

   n = 200

   def test_halfsorted_bubble(self):
      # Test sort method for lists of various lengths

      L1 = [-1, 0, 3] # Initialize a test list
      L1_sorted = [-1, 0, 3] # Initialize a test result list 

      sort_halfsorted(L1, bubble) # Sort the test list
      self.assertEqual(L1, L1_sorted, " started1: " + str(L1)) # Check that the result is as expected


      for length in range(1, self.n): # Loop to create list of lengths ranging from 1 to self.n
         L = generate_halfsorted(length)[0] # Generate a random list

         L_sorted = L.copy()
         sort_halfsorted(L_sorted, bubble) # Sort the list
         self.assertEqual(L_sorted, sorted(L), "start: " + str(L)) # Check that the list is sorted correctly


   def test_half_sorted_selection(self):
      # Test sort method for lists of various lengths

      for length in range(1, self.n):
         L = generate_halfsorted(length)[0]

         L_sorted = L.copy()
         sort_halfsorted(L_sorted, selection)
         self.assertEqual(L_sorted, sorted(L))

   def test_halfsorted_insertion(self):
      # Test sort method for lists of various lengths
      for length in range(1, self.n):
         L = generate_halfsorted(length)[0]

         L_sorted = L.copy()
         sort_halfsorted(L_sorted, insertion)
         self.assertEqual(L_sorted, sorted(L))

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
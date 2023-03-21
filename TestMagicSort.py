import unittest
from MagicSort import linear_scan, reverse_list, insertionsort, quicksort, mergesort,  magic_sort


list1 = [i for i in range(0, 50)]
list2 = list1.copy().reverse()

list3 = [i for i in range(0, 50)]
list3[5] = 0
list3[10] = 0
list3[20] = 0

list4 = [10, 5, 15, 9, 8, 10, 5, 20, 16, 21, 12, 20, -5, 5, 0, 20, 10, 15, 13, 14, 11, 16, 14, 19, 12, 18, 14, 20]



class Test_linear_scan(unittest.TestCase):
    
    def test_linear_scan(self):
        self.assertEqual(linear_scan(list1), 0)
        self.assertEqual(linear_scan(list2), 1)
        self.assertEqual(linear_scan(list3), 2)
        self.assertEqual(linear_scan(list4), -1)

    
class Test_reverse_list(unittest.TestCase):

    def test_reverse(self):



class Test_insertionsort(unittest.TestCase): pass

class Test_quicksort(unittest.TestCase): pass

class Test_mergesort(unittest.TestCase): pass

class Test_magicsort(unittest.TestCase): pass


unittest.main()
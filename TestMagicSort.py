import unittest
from math import log2

from MagicSort import linear_scan, reverse_list, insertionsort, quicksort, mergesort,  magic_sort


list1 = [i for i in range(0, 50)]
list2 = list1.copy()
list2.reverse()

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
    list5 = [1, 2, 3]
    list6 = [5, 1, 4, 3]
    list7 = [0]
    list8 = []

    def test_reverse(self):
        reverse_list(Test_reverse_list.list5, set())
        reverse_list(Test_reverse_list.list6, set())
        reverse_list(Test_reverse_list.list7, set())
        reverse_list(Test_reverse_list.list8, set())

        self.assertEqual(Test_reverse_list.list5, [3, 2, 1])
        self.assertEqual(Test_reverse_list.list6, [3, 4, 1, 5])
        self.assertEqual(Test_reverse_list.list7, [0])
        self.assertEqual(Test_reverse_list.list8, [])

class Test_insertionsort(unittest.TestCase):
    list5 = [1, 2, 3]
    list6 = [5, 1, 4, 3]
    list7 = [0]
    list8 = []
    list9 = [5, 1, 3, 100, -5, -7]

    def test_insertion_sort(self):
        insertionsort(Test_insertionsort.list5, set())
        insertionsort(Test_insertionsort.list6, set())
        insertionsort(Test_insertionsort.list7, set())
        insertionsort(Test_insertionsort.list8, set())
        insertionsort(Test_insertionsort.list9, set())

        self.assertEqual(Test_insertionsort.list5, [1, 2, 3])
        self.assertEqual(Test_insertionsort.list6, [1, 3, 4, 5])
        self.assertEqual(Test_insertionsort.list7, [0])
        self.assertEqual(Test_insertionsort.list8, [])
        self.assertEqual(Test_insertionsort.list9, [-7, -5, 1, 3, 5, 100])

class Test_quicksort(unittest.TestCase):
    list5 = [1, 2, 3]
    list6 = [5, 1, 4, 3]
    list7 = [0]
    list8 = []
    list9 = [5, 1, 3, 100, -5, -7]

    def test_quicksort(self):
        quicksort(Test_quicksort.list5, 0, log2(3)+1, set())
        quicksort(Test_quicksort.list6, 0, log2(4)+1, set())
        quicksort(Test_quicksort.list7, 0, log2(1)+1, set())
        quicksort(Test_quicksort.list8, 0, 1, set())
        quicksort(Test_quicksort.list9, 0, log2(6)+1, set())

        self.assertEqual(Test_quicksort.list5, [1, 2, 3])
        self.assertEqual(Test_quicksort.list6, [1, 3, 4, 5])
        self.assertEqual(Test_quicksort.list7, [0])
        self.assertEqual(Test_quicksort.list8, [])
        self.assertEqual(Test_quicksort.list9, [-7, -5, 1, 3, 5, 100])

class Test_mergesort(unittest.TestCase):
    list5 = [1, 2, 3]
    list6 = [5, 1, 4, 3]
    list7 = [0]
    list8 = []
    list9 = [5, 1, 3, 100, -5, -7]

    def test_mergesort(self):
        mergesort(Test_mergesort.list5, set())
        mergesort(Test_mergesort.list6, set())
        mergesort(Test_mergesort.list7, set())
        mergesort(Test_mergesort.list8, set())
        mergesort(Test_mergesort.list9, set())

        self.assertEqual(Test_mergesort.list5, [1, 2, 3])
        self.assertEqual(Test_mergesort.list6, [1, 3, 4, 5])
        self.assertEqual(Test_mergesort.list7, [0])
        self.assertEqual(Test_mergesort.list8, [])
        self.assertEqual(Test_mergesort.list9, [-7, -5, 1, 3, 5, 100])

class Test_magicsort(unittest.TestCase):
    list5 = [1, 2, 3]
    list6 = [5, 1, 4, 3]
    list7 = [0]
    list8 = []
    list9 = [5, 1, 3, 100, -5, -7]
    list10 = [(-1)**i for i in range(0, 100)]
    list11 = [(-1)**i for i in range(0, 20)]

    def test_magicsort(self):
        algorithms1 = magic_sort(Test_magicsort.list5)
        algorithms2 = magic_sort(Test_magicsort.list6)
        algorithms3 = magic_sort(Test_magicsort.list7)
        algorithms4 = magic_sort(Test_magicsort.list8)
        algorithms5 = magic_sort(Test_magicsort.list9)
        algorithms6 = magic_sort(Test_magicsort.list10)
        algorithms7 = magic_sort(Test_magicsort.list11)

        self.assertEqual(algorithms1, set())
        self.assertEqual(algorithms2, {'insertionsort'})
        self.assertEqual(algorithms3, set())
        self.assertEqual(algorithms4, set())
        self.assertEqual(algorithms5, {'insertionsort'})
        self.assertEqual(algorithms6, {'insertionsort', 'quicksort', 'mergesort'})
        self.assertEqual(algorithms7, {'insertionsort', 'quicksort'})

        self.assertEqual(Test_magicsort.list5, [1, 2, 3])
        self.assertEqual(Test_magicsort.list6, [1, 3, 4, 5])
        self.assertEqual(Test_magicsort.list7, [0])
        self.assertEqual(Test_magicsort.list8, [])
        self.assertEqual(Test_magicsort.list9, [-7, -5, 1, 3, 5, 100])


unittest.main()
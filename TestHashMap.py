import unittest

from hashmap import HashMap


class TestCustomSet(unittest.TestCase):
    def test_basic_usage(self):
        """
        Test the usage of the hashmap class through the addition and removal
        of arbitrary items of various types.
        
        Checks that the HashMap acts as described in the docstring
        """

        myMap = HashMap()

        self.assertRaises(KeyError, myMap.get, "HI")
        self.assertFalse("Hi" in myMap)
        self.assertEqual(len(myMap), 0)

        myMap.add("HI", "WORLD")
        self.assertEqual(myMap.get("HI"), "WORLD")
        self.assertTrue("HI" in myMap)
        self.assertEqual(len(myMap), 1)

        myMap.add("YO", 12)
        self.assertEqual(myMap.get("YO"), 12)
        self.assertTrue("YO" in myMap)
        self.assertEqual(len(myMap), 2)

        myMap.remove("YO")
        self.assertRaises(KeyError, myMap.get, "YO")
        self.assertFalse("YO" in myMap)
        self.assertEqual(len(myMap), 1)
        
        self.assertRaises(KeyError, myMap.remove, "YO")

        myMap.add(1234, 59)
        self.assertEqual(myMap.get(1234), 59)
        self.assertTrue(1234 in myMap)
        self.assertEqual(len(myMap), 2)

    def test_capacity(self):
        """
        Tests the behavior of the hashmap by adding a large amount of items
        and then removing a large amount of items to ensure that the length
        updates properly and rehashing does not cause any errors.
        """
        
        N = 100

        bigMap = HashMap()
        
        for i in range(0, N):
            self.assertRaises(KeyError, bigMap.get, str(i))
            self.assertFalse(str(i) in bigMap)
            currentLen = len(bigMap)

            bigMap.add(str(i), i+10)

            self.assertEqual(len(bigMap), currentLen+1)
            self.assertTrue(str(i) in bigMap)
            self.assertEqual(bigMap.get(str(i)), i+10)

        self.assertEqual(len(bigMap), N)

        for i in range(0, N):
            bigMap.remove(str(i))

        self.assertEqual(len(bigMap), 0)

    
if __name__ == "__main__":
    unittest.main()
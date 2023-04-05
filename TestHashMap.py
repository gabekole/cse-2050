import unittest

from hashmap import HashMap


class TestCustomSet(unittest.TestCase):
    def test_usage(self):
        myMap = HashMap()

        self.assertRaises(KeyError, myMap.get("HI"))
        self.assertFalse("Hi" in myMap)
        self.assertEqual(len(myMap), 0)

        myMap.add("HI", "WORLD")
        self.assertEqual(myMap.get("HI"), "WORLD")
        self.assertTrue("Hi" in myMap)
        self.assertEqual(len(myMap), 1)

        myMap.add("YO", 12)
        self.assertEqual(myMap.get("YO"), 12)
        self.assertTrue("YO" in myMap)
        self.assertEqual(len(myMap), 2)

        myMap.remove("YO")
        self.assertRaises(KeyError, myMap.get("YO"))
        self.assertFalse("YO" in myMap)
        self.assertEqual(len(myMap), 1)
        
        self.assertRaises(KeyError, myMap.remove("YO"))

        myMap.add(1234, 59)
        self.assertEqual(myMap.get(1234), 59)
        self.assertTrue(1234 in myMap)
        self.assertEqual(len(myMap), 2)
    
if __name__ == "__main__":
    unittest.main()
import unittest

from blockchain import Transaction, Block, Blockchain, Ledger


class TestTransaction(unittest.TestCase):
    def test_usage(self):
        t1 = Transaction("ABC", "XYZ", 100)

        self.assertEqual(t1.from_user, "ABC")
        self.assertEqual(t1.to_user, "XYZ")
        self.assertEqual(t1.amount, 100)

        t2 = Transaction("DEC", "XYZ", 110)

        self.assertEqual(t2.from_user, "DEC")
        self.assertEqual(t2.to_user, "XYZ")
        self.assertEqual(t2.amount, 110)

        t3 = Transaction("ABC", "XYZ", 100)

        self.assertEqual(t3.from_user, "ABC")
        self.assertEqual(t3.to_user, "XYZ")
        self.assertEqual(t3.amount, 100)

        self.assertEqual(t1, t3)
        self.assertNotEqual(t1, t2)
        self.assertNotEqual(t2, t3)

        self.assertNotEqual(hash(t1), hash(t2))
        self.assertEqual(hash(t1), hash(t3))



if __name__ == "__main__":
    unittest.main()
import unittest

from blockchain import Transaction, Block, Blockchain, Ledger


class TestTransaction(unittest.TestCase):
    def test_assignment(self):
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

    def test_equality(self):
        t1 = Transaction("ABC", "XYZ", 100)
        t2 = Transaction("DEC", "XYZ", 110)
        t3 = Transaction("ABC", "XYZ", 100)

        self.assertEqual(t1, t3)
        self.assertNotEqual(t1, t2)
        self.assertNotEqual(t2, t3)
    
    def test_hash_continuity(self):
        t1 = Transaction("ABC", "XYZ", 100)
        t2 = Transaction("DEC", "XYZ", 110)
        t3 = Transaction("ABC", "XYZ", 100)


        self.assertNotEqual(hash(t1), hash(t2))
        self.assertEqual(hash(t1), hash(t3))
        self.assertNotEqual(hash(t2), hash(t3))

class TestBlock(unittest.TestCase):
    def test_initialization(self):
        t1 = Transaction("ABC", "XYZ", 100)
        t2 = Transaction("DEC", "XYZ", 110)
        t3 = Transaction("ABC", "XYZ", 100)

        b1 = Block((t1, t2))
        b2 = Block()
        b3 = Block((t3,), previous_block_hash=12)

        self.assertEqual(b1.transactions[0], t1)
        self.assertEqual(b1.transactions[1], t2)
        self.assertEqual(b2.transactions, tuple())
        self.assertEqual(b3.transactions[0], t3)

        self.assertEqual(b1.previous_block_hash, None)
        self.assertEqual(b2.previous_block_hash, None)
        self.assertEqual(b3.previous_block_hash, 12)

    def test_hash(self):
        t1 = Transaction("ABC", "XYZ", 100)
        t2 = Transaction("DEC", "XYZ", 110)
        t3 = Transaction("ABC", "XYZ", 100)

        b1 = Block((t1, t2))
        b2 = Block((t1, t2))
        b3 = Block((t1, t2), previous_block_hash=78)
        b4 = Block(previous_block_hash=78)

        self.assertEqual(hash(b1), hash(b2))
        self.assertNotEqual(hash(b2), hash(b3))
        self.assertNotEqual(hash(b3), hash(b4))
        self.assertNotEqual(hash(b2), hash(b4))

    def test_transaction_addition(self):
        t1 = Transaction("ABC", "XYZ", 100)
        t2 = Transaction("DEC", "XYZ", 110)

        b1 = Block()

        self.assertEqual(b1.transactions, tuple())
        self.assertEqual(len(b1.transactions), 0)

        b1.add_transaction(t1)
        self.assertEqual(len(b1.transactions), 1)
        self.assertEqual(b1.transactions[-1], t1)

        b1.add_transaction(t2)
        self.assertEqual(len(b1.transactions), 2)
        self.assertEqual(b1.transactions[-1], t2)

class TestLedger(unittest.TestCase):
    def test_basic_usage(self):
        l1 = Ledger()

        self.assertFalse(l1.has_funds("me", 100))
        
        l1.deposit("me", 100)
        self.assertTrue(l1.has_funds("me", 50))
        self.assertTrue(l1.has_funds("me", 100))
        self.assertFalse(l1.has_funds("me", 150))
        self.assertFalse(l1.has_funds("me", 200))

        l1.transfer("me", 50)
        self.assertTrue(l1.has_funds("me", 50))
        self.assertFalse(l1.has_funds("me", 100))
        self.assertFalse(l1.has_funds("me", 150))
        self.assertFalse(l1.has_funds("me", 200))

        l1.transfer("me", 50)
        self.assertFalse(l1.has_funds("me", 50))
        self.assertFalse(l1.has_funds("me", 100))
        self.assertFalse(l1.has_funds("me", 150))
        self.assertFalse(l1.has_funds("me", 200))


        self.assertRaises(ValueError, l1.transfer, "me", 50)

        self.assertRaises(ValueError, l1.transfer, "you", 100)

class TestBlockchain(unittest.TestCase):
    def test_usage(self):
        bc = Blockchain() # Genesis block [0]

        self.assertTrue(bc.validate_chain())

        bc.distribute_mining_reward("me") # Mining block [1]

        t1 = Transaction("me", "you", 100)
        t2 = Transaction("you", "him", 5)
        b1 = Block((t1, t2))
        bc.add_block(b1) # Transaction block [2]

        self.assertTrue(bc.validate_chain())

        theft = Transaction("me", "theif", 200)
        bc._blockchain[1].add_transaction(theft) # Attempt to modify previous blocks

        self.assertFalse(bc.validate_chain()) # Successfully detect modification


if __name__ == "__main__":
    unittest.main()
import unittest
from waitlist import Waitlist, Time

class TestWaitlist(unittest.TestCase):

    def test_add_customer(self):
        wl = Waitlist()
        wl.add_customer("John", Time(10, 30))
        self.assertEqual(len(wl._entries), 1)
        self.assertEqual(wl._entries[0].name, "John")
        self.assertEqual(wl._entries[0].time, Time(10, 30))

    def test_add_customer_invalid_priority(self):
        wl = Waitlist()
        with self.assertRaises(ValueError):
            wl.add_customer("John", 123)

    def test_peek(self):
        wl = Waitlist()
        wl.add_customer("John", Time(10, 30))
        wl.add_customer("Mary", Time(11, 0))
        self.assertEqual(wl.peek(), ("John", Time(10, 30)))

    def test_peek_empty(self):
        wl = Waitlist()
        self.assertIsNone(wl.peek())

    def test_seat_customer(self):
        wl = Waitlist()
        wl.add_customer("John", Time(10, 30))
        wl.add_customer("Mary", Time(11, 0))
        wl.add_customer("Bob", Time(10, 45))
        self.assertEqual(wl.seat_customer(), ("John", Time(10, 30)))
        self.assertEqual(wl.seat_customer(), ("Bob", Time(10, 45)))
        self.assertEqual(wl.seat_customer(), ("Mary", Time(11, 0)))
        self.assertIsNone(wl.seat_customer())

    def test_change_reservation(self):
        wl = Waitlist()
        wl.add_customer("John", Time(10, 30))
        wl.add_customer("Mary", Time(11, 0))
        wl.change_reservation("Mary", Time(12, 0))
        self.assertEqual(wl._entries[0].name, "Mary")
        self.assertEqual(wl._entries[0].time, Time(12, 0))

    def test_change_reservation_invalid_priority(self):
        wl = Waitlist()
        wl.add_customer("John", Time(10, 30))
        with self.assertRaises(ValueError):
            wl.change_reservation("John", 123)

    def test_change_reservation_nonexistent_customer(self):
        wl = Waitlist()
        with self.assertRaises(ValueError):
            wl.change_reservation("Mary", Time(12, 0))

if __name__ == '__main__':
    unittest.main()
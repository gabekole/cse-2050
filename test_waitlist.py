import unittest
from waitlist import Waitlist, Time

class TestWaitlist(unittest.TestCase):

    def test_add_customer(self):
        """
        Tests the simple addition of a single person to the waitlist
        """

        wl = Waitlist()
        wl.add_customer("John", Time(10, 30))
        self.assertEqual(len(wl._entries), 1)
        self.assertEqual(wl._entries[0].name, "John")
        self.assertEqual(wl._entries[0].time, Time(10, 30))

    def test_add_customer_invalid_priority(self):
        """
        Tests that adding a customer and attempting to use a 
        type other than `Time` raises an error
        """

        wl = Waitlist()

        with self.assertRaises(ValueError):
            wl.add_customer("John", 123)

    def test_peek(self):
        """
        Tests to ensure that when multiple people are in the 
        wait list, the `peek` method returns the person with the earliest time
        """
        wl = Waitlist()
        wl.add_customer("John", Time(10, 30))
        wl.add_customer("Mary", Time(11, 0))
        self.assertEqual(wl.peek(), ("John", Time(10, 30)))

    def test_peek_empty(self):
        """
        Calls to the peek method `peek` should return none

        this is checked here
        """

        wl = Waitlist()
        self.assertIsNone(wl.peek())

    def test_seat_customer(self):
        """
        Tests the addition and seating of multiple customers

        Checks that attempting to seat from an empty waitlist returns None
        """
        wl = Waitlist()
        wl.add_customer("John", Time(10, 30))
        wl.add_customer("Mary", Time(11, 0))
        wl.add_customer("Bob", Time(10, 45))
        self.assertEqual(wl.seat_customer(), ("John", Time(10, 30)))
        self.assertEqual(wl.seat_customer(), ("Bob", Time(10, 45)))
        self.assertEqual(wl.seat_customer(), ("Mary", Time(11, 0)))
        self.assertIsNone(wl.seat_customer())

    def test_change_reservation(self):
        """
        Checks that waitlist is able to properly update 
        a customers reservation time.
        """
        wl = Waitlist()
        wl.add_customer("John", Time(10, 30))
        wl.add_customer("Mary", Time(11, 0))
        wl.change_reservation("Mary", Time(12, 0))
        self.assertEqual(wl._entries[0].name, "Mary")
        self.assertEqual(wl._entries[0].time, Time(12, 0))

    def test_change_reservation_invalid_priority(self):
        """
        Check that attempting to change the reservation time to
        and invalid time (of type other than `Time`) raises an error
        """
        wl = Waitlist()
        wl.add_customer("John", Time(10, 30))
        with self.assertRaises(ValueError):
            wl.change_reservation("John", 123)

    def test_change_reservation_nonexistent_customer(self):
        """
        Check that an error is raised when attempting to change the
        reservation of someone not on the waitlist
        """
        wl = Waitlist()
        with self.assertRaises(ValueError):
            wl.change_reservation("Mary", Time(12, 0))

if __name__ == '__main__':
    unittest.main()
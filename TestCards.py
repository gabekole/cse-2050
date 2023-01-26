from Cards import Card, Deck, Hand
import unittest

class TestCard(unittest.TestCase)
  "Test cases specific to the Card class"
  def test_init(self):
    "Test the init method of the Card class"
    unittest.assertEqual(Card(6, 'spades').value, 6)
    unittest.assertEqual(Card(6, 'spades').suit, 'spades')
    unittest.assertEqual(Card(2, 'hearts').value, 2)
    unittest.assertEqual(Card(2, 'hearts').suit, 'hearts')
    unittest.assertEqual(Card(13, 'diamonds').value, 13)
    unittest.assertEqual(Card(13, 'diamonds').suit, 'diamonds')
    unittest.assertEqual(Card(12, 'clubs').value, 12)
    unittest.assertEqual(Card(12, 'clubs').suit, 'clubs')

def test_repr(self):
  "Test the repr method of the card class"
  unittest.assertEqual(Card(13, 'spades'), "Card(13 of spades)")
  unittest.assertEqual(Card(3, 'hearts'), "Card(3 of hearts)")
  unittest.assertEqual(Card(2, 'clubs'), "Card(2 of clubs)")
  unittest.assertEqual(Card(5, 'diamonds'), "Card(5 of diamonds)")

def test_lt(self):
  unittest.assertTrue(Card(5, 'a') < Card(3, 'b'))
  unittest.assertTrue(Card(2, 'clubs') < Card(4, 'hearts'))
  unittest.assertTrue(Card(4, 'diamonds') < Card(2, 'spades'))
  
  unittest.assertFalse(Card(6, 'z') < Card(4, 'b'))
  unittest.assertFalse(Card(5, 'hearts') < Card(2, 'clubs'))
  unittest.assertFalse(Card(3, 'spades') < Card(5, 'diamonds'))      

class TestDeck(unittest.TestCase)
  "Test cases specific to the Deck class"
  def test_init(self):
    "Test the init method"

class TestHand(unittest.TestCase)
  "Test cases specific to the Hand class"
  def test_init(self):
    "Test the init method"

if __name__ == "__main__":
  unittest.main()


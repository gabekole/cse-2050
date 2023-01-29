from Cards import Card, Deck, Hand
import unittest
import random

class TestCard(unittest.TestCase):
  "Test cases specific to the Card class"
  def test_init(self):
    "Test the init method of the Card class"
    self.assertEqual(Card(6, 'spades').value, 6)
    self.assertEqual(Card(6, 'spades').suit, 'spades')
    self.assertEqual(Card(2, 'hearts').value, 2)
    self.assertEqual(Card(2, 'hearts').suit, 'hearts')
    self.assertEqual(Card(13, 'diamonds').value, 13)
    self.assertEqual(Card(13, 'diamonds').suit, 'diamonds')
    self.assertEqual(Card(12, 'clubs').value, 12)
    self.assertEqual(Card(12, 'clubs').suit, 'clubs')

  def test_repr(self):
    "Test the repr method of the card class"
    self.assertEqual(repr(Card(13, 'spades')), "Card(13 of spades)")
    self.assertEqual(repr(Card(3, 'hearts')), "Card(3 of hearts)")
    self.assertEqual(repr(Card(2, 'clubs')), "Card(2 of clubs)")
    self.assertEqual(repr(Card(5, 'diamonds')), "Card(5 of diamonds)")

  def test_lt(self):
    self.assertTrue(Card(5, 'a') < Card(3, 'b'))
    self.assertTrue(Card(2, 'clubs') < Card(4, 'hearts'))
    self.assertTrue(Card(4, 'diamonds') < Card(2, 'spades'))
    
    self.assertFalse(Card(6, 'z') < Card(4, 'b'))
    self.assertFalse(Card(5, 'hearts') < Card(2, 'clubs'))
    self.assertFalse(Card(3, 'spades') < Card(5, 'diamonds'))

  def test_eq(self):
    self.assertTrue(Card(5, 'a') == Card(5, 'a'))
    self.assertTrue(Card(4, 'diamonds') == Card(4, 'diamonds'))

    self.assertFalse(Card(2, 'clubs') == Card(4, 'hearts'))
    self.assertFalse(Card(5, 'hearts') == Card(2, 'clubs'))

class TestDeck(unittest.TestCase):
  "Test cases specific to the Deck class"
  def test_init(self):
    "Test the init method"
    first_deck = Deck([1, 2], ['clubs', 'diamonds'])
    second_deck = Deck()

    expected_first_deck = [Card(1, 'clubs'), Card(2, 'clubs'), Card(1, 'diamonds'), Card(2, 'diamonds')]
    
    self.assertEqual(sorted(first_deck.card_list), sorted(expected_first_deck))
    self.assertTrue(len(second_deck.card_list) == 52)

  def test_len(self):
    first_deck = Deck([1, 2], ['clubs', 'diamonds'])
    self.assertEqual(len(first_deck), 2*2)
    self.assertEqual(len(first_deck.card_list), 2*2)

    second_deck = Deck()
    self.assertEqual(len(second_deck), 13*4)

    third_deck = Deck([10, 11, 12], ['triangles', 'squares', 'circles'])
    self.assertEqual(len(third_deck), 3*3)

  def test_sort(self):
    first_deck = Deck([2, 1], ['clubs', 'diamonds'])
    first_deck.sort()

    self.assertEqual(sorted(first_deck.card_list), first_deck.card_list)

    second_deck = Deck([10, 11, 12], ['triangles', 'squares', 'circles'])
    second_deck.sort()

    self.assertEqual(sorted(second_deck.card_list), second_deck.card_list)

    third_deck = Deck([10, 11, 12], ['squares', 'circles'])
    third_deck.sort()

    self.assertEqual(sorted(third_deck.card_list), third_deck.card_list)

  def test_repr(self):
    first_deck = Deck([2], ['clubs', 'diamonds'])
    self.assertEqual(repr(first_deck), "Deck: [Card(2 of clubs), Card(2 of diamonds)]")

    second_deck = Deck([10], ['triangles', 'squares', 'circles'])
    self.assertEqual(repr(second_deck), "Deck: [Card(10 of triangles), Card(10 of squares), Card(10 of circles)]")

  def test_draw_top(self):
    first_deck = Deck([1], ['spades', 'clubs'])

    expected_first_draw = first_deck.card_list[-1]
    expected_second_draw = first_deck.card_list[-2]

    self.assertEqual(first_deck.draw_top(), expected_first_draw)
    self.assertEqual(first_deck.draw_top(), expected_second_draw)

    self.assertRaises(RuntimeError, first_deck.draw_top)


    second_deck = Deck([5, 7], ['diamonds', 'hearts'])

    expected_first_draw = second_deck.card_list[-1]
    expected_second_draw = second_deck.card_list[-2]
    expected_third_draw = second_deck.card_list[-3]
    expected_fourth_draw = second_deck.card_list[-4]

    self.assertEqual(second_deck.draw_top(), expected_first_draw)
    self.assertEqual(second_deck.draw_top(), expected_second_draw)
    self.assertEqual(second_deck.draw_top(), expected_third_draw)
    self.assertEqual(second_deck.draw_top(), expected_fourth_draw)

    self.assertRaises(RuntimeError, second_deck.draw_top)

  def test_shuffle(self):
    deck = Deck([2, 3, 5, 6, 7], ['diamonds', 'hearts', 'triangles'])
    card_list = deck.card_list.copy()

    random.seed(1)
    deck.shuffle()

    self.assertNotEqual(card_list, deck.card_list)
    
    random.seed(1)
    random.shuffle(card_list)

    self.assertEqual(card_list, deck.card_list)
    


class TestHand(unittest.TestCase):
  "Test cases specific to the Hand class"

  def test_init(self):
    "Test the init method"
    first_hand = Hand([Card(value,'clubs') for value in range(5, 0,-1)])
    second_hand = Hand([Card(2, 'triangles')])

  def test_repr(self):
    first_hand = Hand([Card(value,'clubs') for value in range(5, 2,-1)])
    self.assertEqual(repr(first_hand), "Hand: [Card(5 of clubs), Card(4 of clubs), Card(3 of clubs)]")

    second_hand = Hand([Card(2, 'triangles')])
    self.assertEqual(repr(second_hand), "Hand: [Card(2 of triangles)]")

  def test_play(self):
    hand = Hand([Card(5,'clubs'), Card(4,'clubs')])

    self.assertRaises(RuntimeError, hand.play, Card(5, 'diamonds'))
    self.assertRaises(RuntimeError, hand.play, Card(2, 'clubs'))

    hand.play(Card(5, 'clubs'))
    self.assertEqual(hand.card_list, [Card(4, 'clubs')])

    hand.play(Card(4, 'clubs'))
    self.assertEqual(hand.card_list, [])

    self.assertRaises(RuntimeError, hand.play, Card(5, 'clubs'))
    self.assertRaises(RuntimeError, hand.play, Card(4, 'clubs'))



if __name__ == "__main__":
  unittest.main()


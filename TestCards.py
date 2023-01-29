from Cards import Card, Deck, Hand
import unittest

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
    self.assertEqual(Card(13, 'spades'), "Card(13 of spades)")
    self.assertEqual(Card(3, 'hearts'), "Card(3 of hearts)")
    self.assertEqual(Card(2, 'clubs'), "Card(2 of clubs)")
    self.assertEqual(Card(5, 'diamonds'), "Card(5 of diamonds)")

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
    first_hand = Hand([1, 2], ['clubs', 'diamonds'])
    second_hand = Hand()

    expected_first_hand = [Card(1, 'clubs'), Card(2, 'clubs'), Card(1, 'diamonds'), Card(2, 'diamonds')]
    
    self.assertEqual(sorted(first_hand.card_list), sorted(expected_first_hand))
    self.assertTrue(len(second_hand.card_list) == 52)

  def test_len(self):
    first_hand = Hand([1, 2], ['clubs', 'diamonds'])
    self.assertEqual(len(first_hand), 2*2)

    second_hand = Hand()
    self.assertEqual(len(second_hand), 13*4)

    third_hand = Hand([10, 11, 12], ['triangles', 'squares', 'circles'])
    self.assertEqual(len(third_hand), 3*3)

  def test_sort(self):
    first_hand = Hand([2, 1], ['clubs', 'diamonds'])
    first_hand_sorted = first_hand.sort()

    self.assertEqual(sorted(first_hand.card_list), first_hand_sorted.card_list)

    second_hand = Hand([10, 11, 12], ['triangles', 'squares', 'circles'])
    second_hand_sorted = second_hand.sort()

    self.assertEqual(sorted(second_hand.card_list), second_hand_sorted.card_list)

    third_hand = Hand([10, 11, 12], ['squares', 'circles'])
    third_hand_sorted = third_hand.sort()

    self.assertEqual(sorted(third_hand.card_list), third_hand_sorted.card_list)

  def test_repr(self):
    first_hand = Hand([2, 1], ['clubs', 'diamonds'])
    self.assertEqual(repr(first_hand.card_list), "Deck: [Card(2 of clubs), Card(1 of clubs), Card(2 of diamonds), Card(1 of clubs)]")

    second_hand = Hand([10], ['triangles', 'squares', 'circles'])
    self.assertEqual(repr(second_hand.card_list), "Deck: [Card(10 of triangles), Card(10 of squares), Card(10 of circles)]")

  def test_draw_top(self):
    first_hand = Hand([1], ['clubs', 'diamonds'])

    expected_first_draw = first_hand.card_list[-1]
    expected_second_draw = first_hand.card_list[-2]

    self.assertEqual(first_hand.draw_top(), expected_first_draw)
    self.assertEqual(first_hand.draw_top(), expected_second_draw)

    self.assertRaises(RuntimeError, first_hand.draw_top())


    second_hand = Hand([2, 1], ['clubs', 'diamonds'])

    expected_second_draw = second_hand.card_list[-1]
    expected_second_draw = second_hand.card_list[-2]
    expected_third_draw = second_hand.card_list[-3]
    expected_fourth_draw = second_hand.card_list[-4]

    self.assertEqual(second_hand.draw_top(), expected_second_draw)
    self.assertEqual(second_hand.draw_top(), expected_second_draw)
    self.assertEqual(second_hand.draw_top(), expected_third_draw)
    self.assertEqual(second_hand.draw_top(), expected_fourth_draw)

    self.assertRaises(RuntimeError, second_hand.draw_top())

  def test_shuffle(self):
    pass
    


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

    self.assertRaises(RuntimeError, hand.play(Card(5, 'diamonds')))
    self.assertRaises(RuntimeError, hand.play(Card(2, 'clubs')))

    hand.play(5, 'clubs')
    self.assertEqual(hand.card_list, [Card(4, 'clubs')])

    hand.play(4, 'clubs')
    self.assertEqual(hand.card_list, [])

    self.assertRaises(RuntimeError, hand.play(5, 'clubs'))
    self.assertRaises(RuntimeError, hand.play(4, 'clubs'))



if __name__ == "__main__":
  unittest.main()


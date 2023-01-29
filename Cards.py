import random

class Card:
    """
    Represents a playing card.
    """

    def __init__(self, value, suit):
        """
        Initialize a card with value and suit.
        
        Args:
            value (int): the value of the card.
            suit (str): the suit of the card.
        """

        self.value = value
        self.suit = suit
    
    def __repr__(self):
        """
        Returns a string representation of the card.
        """

        return f'Card({self.value} of {self.suit})'

    def __lt__(self, other):
        """
        Returns True if this card is less than `other` card.

        First compares suit alphabetically, then compares card values.
        """

        if self.suit != other.suit:
            return self.suit < other.suit
        else:
            return self.value < other.value

    def __eq__(self, other):
        """
        Returns True if this card is equal to `other` card, False otherwise.
        """

        return self.value == other.value and self.suit == other.suit
    


class Deck:
    """
    Represents a deck of playing cards.
    """

    def __init__(self, values = [i for i in range(1, 14)], suits = ['clubs', 'diamonds', 'hearts', 'spades']):
        """
        Initialize a deck with given `values` and `suits`.

        Args:
            values (list): list of int values of cards.
            suits (list): list of str suits of cards.
        """

        self.card_list = []
        self.values = values
        self.suits = suits

        for suit in suits:
            for value in values:
                self.card_list.append(Card(value, suit))

    def __len__(self):
        """
        Returns the number of cards in the deck.
        """

        return len(self.card_list)
    
    def sort(self):
        """
        Sorts the cards in the deck in place.
        """

        self.card_list = sorted(self.card_list)

    def __repr__(self):
        """
        Returns a string representation of the deck.
        """

        cards = ", ".join([repr(card) for card in self.card_list])
        
        return f'Deck: [{cards}]'

    def shuffle(self):
        """
        Shuffles the cards in the deck in place.
        """

        random.shuffle(self.card_list)

    def draw_top(self):
        """
        Draws and removes the top card from the deck.
        
        Returns:
            Card: the top card.
        
        Raises:
            RuntimeError: if the deck is empty.
        """

        if len(self.card_list) <= 0:
            raise RuntimeError

        card = self.card_list.pop()

        return card

class Hand(Deck):
    def __init__(self, cards):
        """
        Represents a hand of playing cards.
        """

        super().__init__([], [])

        self.card_list = cards

    def __repr__(self):
        """
        Returns a string representation of the Hand.
        """

        result = "Hand: ["
        result += ", ".join([repr(card) for card in self.card_list])
        result += "]"

        return result

    def play(self, card):
        """
        Draws and removes `card` from the deck.
        
        Returns:
            Card: the played card.
        
        Raises:
            RuntimeError: if `card` is not in the deck.
        """

        if card not in self.card_list:
            raise RuntimeError

        self.card_list.remove(card)

        return card

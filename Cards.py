import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return f'Card({self.value} of {self.suit})'

    def __lt__(self, other):
        if self.suit != other.suit:
            return self.suit < other.suit
        else:
            return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit
    


class Deck:
    def __init__(self, values = [i for i in range(1, 14)], suits = ['clubs', 'diamonds', 'hearts', 'spades']):
        self.card_list = []
        self.values = values
        self.suits = suits

        for suit in suits:
            for value in values:
                self.card_list.append(Card(value, suit))

    def __len__(self):
        return len(self.card_list)
    
    def sort(self):
        self.card_list = sorted(self.card_list)

    def __repr__(self):
        result = "Deck: ["
        result += ", ".join([repr(card) for card in self.card_list])
        result += "]"
        
        return result

    def shuffle(self):
        random.shuffle(self.card_list)

    def draw_top(self):
        card = self.card_list.pop()

        return card

class Hand(Deck):
    def __init__(self, cards):
        super().__init__([], [])

        self.card_list = cards

    def __repr__(self):
        result = "Hand: ["
        result += ", ".join([repr(card) for card in self.card_list])
        result += "]"

        return result

    def play(self, card):
        if card not in self.card_list:
            raise RuntimeError

        self.card_list.remove(card)

        return card

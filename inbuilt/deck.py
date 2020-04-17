
from collections import namedtuple

card = namedtuple("card", ['rank', 'suit'])

"""
This class demonstrate the power of overriding the inbuilt function.
This allow us to interact with our class in more pythonic way.
"""
class Deck:

    def __init__(self):
        ranks = [x for x in range(2, 11)] + list("JKQA")
        suits = 'spades diamonds clubs hearts'.split()
        self._cards = [card(rank, suit) for rank in ranks for suit in suits]\

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self):
        return  "This is the Deck class instance"


if __name__ == '__main__':
    deck = Deck()

    print(len(deck))
    print(card(rank=2, suit='spades') in deck)
    print(deck)

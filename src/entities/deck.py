"""Module deck.py

    This module is used to create an instance of a Deck-class.
    """

import random

from entities.card import Card
from entities.suit import Suit


class Deck:
    """Class that represent a card deck.

    Upon creating a Deck-object, 52 Card-objects are generated
    to form a single deck. Created deck will be in random order.

        Typical usage example:

        Creates a new deck with 52 cards:
        deck = Deck()
    """

    def __init__(self):
        """Constructor of the class. Creates a new deck with 52 cards.
        """
        self.generate_deck()

    def generate_deck(self):
        """Generates a deck with 52 cards.

        Returns:

            List: Containing 52 cards.
        """
        card_deck = []
        for suit in Suit:
            for card_value in range(2, 15):
                card_deck.append(Card(card_value, suit))

        random.shuffle(card_deck)
        self.card_deck = card_deck

    def draw_one_card(self) -> Card:
        """Returns one card from the top.

           If the card retrieved was the last one,
           generate new deck.

        Returns:

            Card: Card object.
        """
        if len(self.card_deck) == 0:
            self.generate_deck()

        return self.card_deck.pop(0)

    def __eq__(self, other: 'Deck'):
        if other is None:
            return False
        else:
            return self.card_deck == other.card_deck

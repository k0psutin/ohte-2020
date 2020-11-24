"""Module deck.py

    This module is used to create an instance of a Deck-class.

    Example:
        deck = Deck()
    """

import random

from entities.card import Card


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
        self.card_deck = self.generate_deck()
        self.current_card_index = 0

    def generate_deck(self):
        """Generates a deck with 52 cards.

        Returns:
            List: Containing 52 cards.
        """
        card_deck = []
        for suit in range(1, 5):
            for card_value in range(2, 15):
                card_deck.append(Card(card_value, suit))

        random.shuffle(card_deck)
        return card_deck

    def draw_one_card(self):
        """Returns one card from the top.

           If the card retrieved was the last one,
           shuffles the deck and resets the index pointing
           to a next card.

        Returns:
            Card: Card
        """
        card = self.card_deck[self.current_card_index]

        self.current_card_index += 1

        if self.current_card_index > 51:
            random.shuffle(self.card_deck)
            self.current_card_index = 0

        return card

    def __eq__(self, other: 'Deck'):
        if other is None:
            return False
        else:
            return self.card_deck == other.card_deck

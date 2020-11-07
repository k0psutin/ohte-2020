import random

from entities.card import Card


class Deck:
    def __init__(self):
        self.card_deck = self.generate_deck()
        self.current_card_index = 0

    def generate_deck(self):
        card_deck = []
        for suit in range(1, 5):
            for card_value in range(2, 15):
                card_deck.append(Card(card_value, suit))

        random.shuffle(card_deck)
        return card_deck

    def draw_one_card(self):
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

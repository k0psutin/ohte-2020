import unittest
import random
from entities.deck import Deck


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.test_card_deck = self.deck.card_deck

    def test_calling_constructor_creates_an_object(self):
        self.assertNotEqual(self.deck, None)

    def test_two_deck_objects_are_not_the_same(self):
        self.other_deck = Deck()
        self.assertNotEqual(self.deck, self.other_deck)

    def test_no_duplicate_cards_in_deck(self):
        compare_deck = []
        no_duplicates = True

        for card in self.test_card_deck:
            if card not in compare_deck:
                compare_deck.append(card)
            else:
                no_duplicates = False
                break

        self.assertTrue(no_duplicates)

    def test_get_one_card_returns_the_correct_card(self):
        card_in_queue = self.test_card_deck[self.deck.current_card_index]
        current_card = self.deck.draw_one_card()

        self.assertEqual(card_in_queue, current_card)

    def test_all_drawed_cards_are_correct(self):
        correct_draw = False

        for i in range(0, 52):
            card_in_queue = self.test_card_deck[i]
            current_card = self.deck.draw_one_card()
            correct_draw = (card_in_queue == current_card)

        self.assertTrue(correct_draw)

    def test_decks_are_different_when_it_is_shuffled(self):
        test_cards = list(self.deck.card_deck)
        random.shuffle(self.deck.card_deck)

        self.assertNotEqual(test_cards, self.deck.card_deck)

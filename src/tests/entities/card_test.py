import unittest
from entities.card import Card
from entities.suit import Suit


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card(14, Suit.hearts)

    def test_calling_constructor_creates_a_card(self):
        self.assertNotEqual(self.card, None)

    def test_created_card_rank_is_correct(self):
        self.assertEqual(self.card.rank, 14)

    def test_created_card_rank_type_is_correct(self):
        self.assertEqual(self.card.get_rank_type(), 'A')

    def test_created_card_rank_type_is_correct_if_less_than_11(self):
        self.card = Card(2, Suit.hearts)
        self.assertEqual(self.card.get_rank_type(), '2')

    def test_created_card_suit_is_correct(self):
        self.assertEqual(self.card.suit, Suit.hearts)

    def test_created_card_suit__type_is_correct(self):
        self.assertEqual(self.card.get_suit_type(), 'hearts.png')

    def test_created_red_card_color_is_correct(self):
        self.assertEqual(self.card.color, 'r')

    def test_created_card_color_code_is_correct(self):
        self.assertEqual(self.card.get_color_code(), (254, 0, 0))

    def test_created_black_card_color_is_correct(self):
        self.card = Card(2, Suit.clubs)
        self.assertEqual(self.card.color, 'b')

    def test_created_black_card_color_code_is_correct(self):
        self.card = Card(2, Suit.clubs)
        self.assertEqual(self.card.get_color_code(), (0, 0, 0))

    def test_cant_create_card_with_rank_less_than_two(self):
        with self.assertRaises(Exception):
            Card(1, Suit.hearts)

    def test_cant_create_card_with_rank_greater_than_fourteen(self):
        with self.assertRaises(Exception):
            Card(15, Suit.hearts)

    def test_cant_create_card_with_suit_that_has_no_enum(self):
        with self.assertRaises(Exception):
            Card(2, Suit.something)

    def test_cant_create_card_with_suit_value_greater_than_four(self):
        with self.assertRaises(Exception):
            Card(1, Suit.something)

    def test_cant_create_card_that_is_lower_than_min_limits(self):
        with self.assertRaises(Exception):
            Card(1, Suit.something)

    def test_cant_create_card_that_exceeds_max_limits(self):
        with self.assertRaises(Exception):
            Card(15, Suit.something)

    def test_calling_tostring_returns_correct_suite_and_rank(self):
        self.assertEqual(str(self.card), 'Rank: 14, Suit: Suit.hearts')

    def test_compare_less_than_or_equal_rank(self):
        other_card = Card(2, Suit.diamonds)
        self.assertTrue(other_card <= self.card)

    def test_compare_greater_than_rank(self):
        other_card = Card(2, Suit.diamonds)
        self.assertTrue(self.card > other_card)

    def test_compare_greater_than_or_equal_rank(self):
        other_card = Card(2, Suit.diamonds)
        self.assertTrue(self.card >= other_card)

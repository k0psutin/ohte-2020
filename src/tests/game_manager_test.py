import unittest

from services.game_manager import GameManager
from entities.card import Card
from entities.player import Player


class TestGameManager(unittest.TestCase):
    def setUp(self):
        self.game_manager = GameManager()
        self.player = Player(True)
        self.game_manager.set_player(self.player)

    def test_calling_constructor_creates_an_object(self):
        self.assertNotEqual(self.game_manager, None)

    def test_get_current_bet_returns_correct_amount(self):
        self.assertTrue(self.game_manager.current_bet, 1)

    def test_can_increase_bet(self):
        self.game_manager.increase_bet()
        self.assertTrue(self.game_manager.current_bet, 2)

    def test_can_decrease_bet(self):
        self.game_manager.increase_bet()
        self.game_manager.decrease_bet()
        self.assertTrue(self.game_manager.current_bet, 1)

    def test_decreasing_bet_doesnt_make_the_bet_negative(self):
        self.game_manager.decrease_bet()
        self.assertTrue(self.game_manager.current_bet, '5')

    def test_increasing_bet_doesnt_make_the_bet_go_over_six(self):
        for _ in range(0, 6):
            self.game_manager.increase_bet()

        self.assertTrue(self.game_manager.current_bet, '1')

    def test_when_deal_is_active_bet_cant_be_increased(self):
        self.game_manager.deal()
        self.game_manager.increase_bet()
        self.assertTrue(self.game_manager.current_bet, '1')

    def test_when_deal_is_active_bet_cant_be_decreased(self):
        self.game_manager.deal()
        self.game_manager.decrease_bet()
        self.assertTrue(self.game_manager.current_bet, '1')

    def test_return_false_when_deal_is_not_active(self):
        self.assertEqual(self.game_manager.deal_active, False)

    def test_return_true_when_deal_is_active(self):
        self.game_manager.deal()
        self.assertEqual(self.game_manager.deal_active, True)

    def test_when_deal_is_active_game_is_active(self):
        self.game_manager.deal()
        self.assertEqual(self.game_manager.game_active, True)

    def test_cards_are_not_on_hold_in_the_beginning(self):
        for hold in self.game_manager.card_on_hold:
            self.assertEqual(hold, False)

    def test_cards_can_be_put_on_hold(self):
        for i in range(0, 5):
            self.game_manager.hold_card(i)
            self.assertEqual(self.game_manager.card_on_hold[i], True)

    def test_card_hold_is_togglable(self):
        for i in range(0, 5):
            self.game_manager.hold_card(i)
            self.game_manager.hold_card(i)
            self.assertEqual(self.game_manager.card_on_hold[i], False)

    def test_get_player_hand_returns_current_player_hand(self):
        test_hand = [Card(9, 1), Card(2, 2), Card(7, 1),
                     Card(10, 3)], Card(13, 3)
        self.game_manager.player_hand = test_hand
        self.assertEqual(test_hand, self.game_manager.player_hand)

    def test_if_card_is_on_hold_it_is_not_replaced(self):
        for i in range(0, 5):
            self.game_manager.deal()
            test_player_hand = list(self.game_manager.player_hand)
            self.game_manager.hold_card(i)
            self.game_manager.deal()
            self.assertEqual(
                test_player_hand[i], self.game_manager.player_hand[i])

    def test_bad_hand_returns_zero(self):
        self.hand = [Card(14, 1), Card(8, 2), Card(7, 2),
                     Card(10, 2), Card(3, 4)]
        self.game_manager.player_hand = self.hand
        self.game_manager.check_player_hand()
        self.assertEqual(self.game_manager.current_win, 0)

    def test_one_pair_returns_correct_amount(self):
        self.hand = [Card(14, 1), Card(14, 2), Card(7, 2),
                     Card(10, 2), Card(3, 4)]
        self.game_manager.player_hand = self.hand

        test_winnings = []

        for i in range(1, 6):
            self.game_manager.current_bet = i
            self.game_manager.check_player_hand()
            test_winnings.append(self.game_manager.current_win)

        self.assertEqual(test_winnings, [1, 2, 3, 4, 5])

    def test_get_win_amount_returns_correct_string(self):
        self.hand = [Card(14, 1), Card(14, 2), Card(7, 2),
                     Card(10, 2), Card(3, 4)]
        self.game_manager.player_hand = self.hand

        self.game_manager.current_bet = 1
        self.game_manager.check_player_hand()

        self.assertTrue(self.game_manager.current_win,
                        'You won 2 credits!')

    def test_win_activates_win_status(self):
        self.hand = [Card(14, 1), Card(14, 2), Card(7, 2),
                     Card(7, 2), Card(3, 4)]
        self.game_manager.player_hand = self.hand

        self.game_manager.current_bet = 1
        self.game_manager.check_player_hand()

        self.assertEqual(self.game_manager.player_win, True)

    def test_get_winning_hand_returns_correct_hand(self):
        self.hand = [Card(14, 1), Card(14, 2), Card(7, 2),
                     Card(7, 2), Card(3, 4)]
        self.game_manager.player_hand = self.hand

        self.game_manager.current_bet = 1
        self.game_manager.check_player_hand()

        self.assertTrue(self.game_manager.winning_hand, 'Two Pairs!')

    def test_claim_win_increases_players_credits(self):
        self.hand = [Card(14, 1), Card(14, 2), Card(7, 2),
                     Card(7, 2), Card(3, 4)]
        self.game_manager.player_hand = self.hand

        self.game_manager.current_bet = 1
        self.game_manager.check_player_hand()
        self.game_manager.claim_win()

        self.assertTrue(self.game_manager.player.credits, 11)

    def test_claim_win_resets_win_status(self):
        self.hand = [Card(14, 1), Card(14, 2), Card(7, 2),
                     Card(7, 2), Card(3, 4)]
        self.game_manager.player_hand = self.hand

        self.game_manager.current_bet = 1
        self.game_manager.check_player_hand()
        self.game_manager.claim_win()

        self.assertEqual(self.game_manager.current_win, 0)
        self.assertEqual(self.game_manager.player_win, False)

    def test_two_pairs_returns_correct_amount(self):
        self.hand = [Card(14, 1), Card(14, 2), Card(7, 2),
                     Card(7, 2), Card(3, 4)]
        self.game_manager.player_hand = self.hand

        test_winnings = []

        for i in range(1, 6):
            self.game_manager.current_bet = i
            self.game_manager.check_player_hand()
            test_winnings.append(self.game_manager.current_win)

        self.assertEqual(test_winnings, [2, 4, 6, 8, 10])

    def test_three_of_a_kind_returns_correct_amount(self):
        self.hand = [Card(14, 1), Card(14, 2), Card(14, 2),
                     Card(7, 2), Card(3, 4)]
        self.game_manager.player_hand = self.hand

        test_winnings = []

        for i in range(1, 6):
            self.game_manager.current_bet = i
            self.game_manager.check_player_hand()
            test_winnings.append(self.game_manager.current_win)

        self.assertEqual(test_winnings, [3, 6, 9, 12, 15])

    def test_straight_returns_correct_amount(self):
        self.hand = [Card(2, 2), Card(3, 3),
                     Card(4, 1), Card(5, 4), Card(6, 2)]
        self.game_manager.player_hand = self.hand

        test_winnings = []

        for i in range(1, 6):
            self.game_manager.current_bet = i
            self.game_manager.check_player_hand()
            test_winnings.append(self.game_manager.current_win)

        self.assertEqual(test_winnings, [4, 8, 12, 16, 20])

    def test_straight_returns_correct_amount_if_contains_high_ace(self):
        self.hand = [Card(14, 1), Card(10, 2), Card(11, 3),
                     Card(12, 1), Card(13, 4)]
        self.game_manager.player_hand = self.hand

        test_winnings = []

        for i in range(1, 6):
            self.game_manager.current_bet = i
            self.game_manager.check_player_hand()
            test_winnings.append(self.game_manager.current_win)

        self.assertEqual(test_winnings, [4, 8, 12, 16, 20])

    def test_straight_returns_correct_amount_if_contains_low_ace(self):
        self.hand = [Card(14, 1), Card(2, 2), Card(3, 3),
                     Card(4, 1), Card(5, 4)]
        self.game_manager.player_hand = self.hand

        test_winnings = []

        for i in range(1, 6):
            self.game_manager.current_bet = i
            self.game_manager.check_player_hand()
            test_winnings.append(self.game_manager.current_win)

        self.assertEqual(test_winnings, [4, 8, 12, 16, 20])

    def test_flush_returns_correct_amount(self):
        self.hand = [Card(14, 1), Card(8, 1), Card(7, 1),
                     Card(10, 1), Card(3, 1)]
        self.game_manager.player_hand = self.hand

        test_winnings = []

        for i in range(1, 6):
            self.game_manager.current_bet = i
            self.game_manager.check_player_hand()
            test_winnings.append(self.game_manager.current_win)

        self.assertEqual(test_winnings, [6, 12, 18, 24, 30])

    def test_full_house_returns_correct_amount(self):
        self.hand = [Card(14, 1), Card(14, 2), Card(14, 3),
                     Card(13, 1), Card(13, 2)]
        self.game_manager.player_hand = self.hand

        test_winnings = []

        for i in range(1, 6):
            self.game_manager.current_bet = i
            self.game_manager.check_player_hand()
            test_winnings.append(self.game_manager.current_win)

        self.assertEqual(test_winnings, [9, 18, 27, 36, 45])

    def test_four_of_a_kind_returns_correct_amount(self):
        self.hand = [Card(14, 1), Card(14, 2), Card(14, 3),
                     Card(14, 4), Card(13, 2)]
        self.game_manager.player_hand = self.hand

        test_winnings = []

        for i in range(1, 6):
            self.game_manager.current_bet = i
            self.game_manager.check_player_hand()
            test_winnings.append(self.game_manager.current_win)

        self.assertEqual(test_winnings, [25, 50, 75, 100, 125])

    def test_straight_flush_returns_correct_amount(self):
        self.hand = [Card(6, 1), Card(7, 1), Card(8, 1),
                     Card(9, 1), Card(10, 1)]
        self.game_manager.player_hand = self.hand

        test_winnings = []

        for i in range(1, 6):
            self.game_manager.current_bet = i
            self.game_manager.check_player_hand()
            test_winnings.append(self.game_manager.current_win)

        self.assertEqual(test_winnings, [50, 100, 150, 200, 250])

    def test_royal_flush_returns_correct_amount(self):
        self.hand = [Card(10, 1), Card(11, 1), Card(12, 1),
                     Card(13, 1), Card(14, 1)]
        self.game_manager.player_hand = self.hand

        test_winnings = []

        for i in range(1, 6):
            self.game_manager.current_bet = i
            self.game_manager.check_player_hand()
            test_winnings.append(self.game_manager.current_win)

        self.assertEqual(test_winnings, [250, 500, 750, 1000, 4000])

    def test_royal_flush_returns_correct_win_amount_string(self):
        self.hand = [Card(10, 1), Card(11, 1), Card(12, 1),
                     Card(13, 1), Card(14, 1)]
        self.game_manager.player_hand = self.hand

        self.game_manager.check_player_hand()

        self.assertTrue(self.game_manager.get_win_amount(),
                        'You won 250 credits!')

    def test_gameover_is_active_if_no_credits_on_deal(self):
        self.game_manager.player.credits = 0
        self.game_manager.deal()
        self.assertEqual(self.game_manager.gameover, True)

    def test_calling_deal_when_game_is_active_and_over_returns_none(self):
        self.game_manager.game_active = True
        self.game_manager.gameover = True
        self.game_manager.player.credits = 0
        self.assertEqual(self.game_manager.deal(), None)

    def test_set_player_returns_none_if_player_has_no_credits(self):
        test_player = Player()
        test_game_manager = GameManager()
        test_player.credits = 0
        self.assertEqual(test_game_manager.set_player(test_player), None)

    def test_double_method_sets_player_win_to_false(self):
        self.game_manager.double()
        self.assertEqual(self.game_manager.player_win, False)

    def test_double_method_sets_double_active_true(self):
        self.game_manager.double()
        self.assertEqual(self.game_manager.double_active, True)

    def test_double_method_sets_deal_active_false(self):
        self.game_manager.double()
        self.assertEqual(self.game_manager.deal_active, False)

    def test_double_method_resets_player_hand(self):
        self.game_manager.double()
        for card in self.game_manager.player_hand:
            self.assertEqual(card, None)

    def test_if_low_double_is_correct_current_win_is_doubled(self):
        self.game_manager.current_win = 100
        test_card = Card(2, 1)
        self.game_manager.deck.card_deck[0] = test_card

        self.game_manager.guess_card_rank('low')

        self.assertEqual(self.game_manager.current_win, 200)

    def test_if_low_double_is_correct_if_ace_is_drawn(self):
        self.game_manager.current_win = 100
        test_card = Card(14, 1)
        self.game_manager.deck.card_deck[0] = test_card

        self.game_manager.guess_card_rank('low')

        self.assertEqual(self.game_manager.current_win, 200)

    def test_if_low_double_is_incorrect_current_win_sets_to_zero(self):
        self.game_manager.current_win = 100
        test_card = Card(9, 1)
        self.game_manager.deck.card_deck[0] = test_card

        self.game_manager.guess_card_rank('low')

        self.assertEqual(self.game_manager.current_win, 0)

    def test_if_high_double_is_correct_current_win_is_doubled(self):
        self.game_manager.current_win = 100
        test_card = Card(9, 1)
        self.game_manager.deck.card_deck[0] = test_card

        self.game_manager.guess_card_rank('high')

        self.assertEqual(self.game_manager.current_win, 200)

    def test_if_high_double_is_incorrect_current_win_is_set_to_zero(self):
        self.game_manager.current_win = 100
        test_card = Card(2, 1)
        self.game_manager.deck.card_deck[0] = test_card

        self.game_manager.guess_card_rank('high')

        self.assertEqual(self.game_manager.current_win, 0)

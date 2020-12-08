"""Module game_manager.py

    This module handles all gameplay logic.
"""

from entities.deck import Deck
from entities.player import Player


class GameManager():
    """Class that handles gameplay logic.

    Typical usage example.
        self.game_manager = GameManager()
    """

    def __init__(self):
        """Constructor of the class.

        Resets the game upon creating, and also creates an instance of
        Deck-class and Player-class.

        Deck instance is used for dealing cards and doubling.
        Player instance is used to control player credits etc.
        """
        self.current_bet = 1
        self.current_win = 0
        self.winning_hand = ''

        self.player = Player()
        self.deck = Deck()

        self.player_hand = [None, None, None, None, None]
        self.card_on_hold = [False, False, False, False, False]

        self.deal_active = False
        self.game_active = False
        self.double_active = False
        self.gameover = False
        self.bad_guess = False
        self.player_win = False
        self.new_highscore = False

    def reset_game(self):
        self.current_bet = 1
        self.current_win = 0
        self.deal_active = False
        self.game_active = False
        self.double_active = False
        self.gameover = False
        self.bad_guess = False
        self.player_win = False
        self.card_on_hold = [False, False, False, False, False]
        self.new_highscore = False

    def submit_highscore(self, name):
        self.player.submit_highscore(name)
        self.player.save_player()
        self.reset_game()

    def new_game(self):
        self.reset_game()
        self.player = Player()

    def continue_game(self):
        self.reset_game()

        if self.player is not None:
            self.player = self.player.load_player()

        if self.player is None:
            return

        if self.player.credits == 0:
            self.gameover = True

    def quit_game(self):
        self.reset_game()
        self.player.save_player()

    def increase_bet(self):
        if self.deal_active:
            return

        self.current_bet += 1

        if self.current_bet > 5:
            self.current_bet = 1

    def decrease_bet(self):
        if self.deal_active:
            return

        self.current_bet -= 1

        if self.current_bet < 1:
            self.current_bet = 5

    def hold_card(self, value):
        if self.card_on_hold[value]:
            self.card_on_hold[value] = False
        else:
            self.card_on_hold[value] = True

    def double(self):
        """Setups the game ready for doubling.
        """
        self.player_hand = [None, None, None, None, None]
        self.player_win = False
        self.double_active = True
        self.deal_active = False

    def guess_card_rank(self, guess):
        """Handles game logic for doubling game.

        Checks if player guessed next card rank correctly.

        Args:

            guess (str): Card rank value guess. 'low' if low card,
            and 'high' if high card.

        Typical usage example:

            Player guesses the next card is low.
            guess_card_rank('low')
        """
        self.player_hand[0] = self.deck.draw_one_card()
        card_rank = self.player_hand[0].rank
        win = False

        if guess == 'low' and card_rank <= 7 or card_rank == 14:
            self.winning_hand = 'Low Card!'
            win = True
        if guess == 'high' and self.player_hand[0].rank > 7:
            self.winning_hand = 'High Card!'
            win = True

        if win is False:
            self.player.successful_double(False)
            self.current_win = 0
            self.bad_guess = True

            self.gameover = (self.player.credits == 0)
            self.game_active = (self.player.credits != 0)
            if self.gameover is True:
                self.new_highscore = self.player.has_new_highscore()
        else:
            self.player_win = True
            self.current_win = self.current_win * 2
            self.player.successful_double(True)

    def end_double(self):
        self.bad_guess = False
        self.double_active = False

    def deal(self):
        if self.deal_active is not True:
            if self.player.credits == 0:
                self.new_highscore = self.player.has_new_highscore()
                self.gameover = True
                return
            self.deck = Deck()
            self.player.remove_credits(self.current_bet)

        self.game_active = True

        for i in range(0, 5):
            if self.card_on_hold[i] is False:
                self.player_hand[i] = self.deck.draw_one_card()

        if self.deal_active:
            self.check_player_hand()
            self.deal_active = False
            self.card_on_hold = [False, False, False, False, False]
        else:
            self.deal_active = True

    def check_player_hand(self):
        """Handles logic for checking the player hand for win.

           Sorts the current hand from low to high, and iterates
           trough the cards to determine what winning hand the
           player has.

        """
        player_hand = list(self.player_hand)
        player_hand.sort()
        self.player_win = True
        self.game_active = False

        count = 1
        pair_count = 0
        pair = False
        two_pairs = False
        three_of_a_kind = False
        four_of_a_kind = False
        straight = True
        low_ace_straight = False
        flush = True

        for i in range(1, 5):
            if straight and i == 4 and \
               player_hand[i-1].rank == 5 and \
               player_hand[i].rank == 14:

                low_ace_straight = True

            if player_hand[i-1].rank != player_hand[i].rank - 1:
                straight = False

            if player_hand[i-1].suit != player_hand[i].suit:
                flush = False

            if player_hand[i-1].rank == player_hand[i].rank:
                count += 1
            else:
                count = 1

            if count == 2:
                pair_count += 1

            if pair is False and pair_count == 1:
                pair = True

            if two_pairs is False and pair_count == 2:
                two_pairs = True

            if three_of_a_kind is False and count == 3:
                three_of_a_kind = True

            if four_of_a_kind is False and count == 4:
                four_of_a_kind = True

        if straight and flush:
            if player_hand[0].rank == 10 and \
                    player_hand[0].suit == 1:
                self.set_win_amount(8)
            else:
                self.set_win_amount(7)

        elif four_of_a_kind:
            self.set_win_amount(6)
        elif two_pairs and three_of_a_kind:
            self.set_win_amount(5)
        elif flush:
            self.set_win_amount(4)
        elif straight or low_ace_straight:
            self.set_win_amount(3)
        elif three_of_a_kind:
            self.set_win_amount(2)
        elif two_pairs and four_of_a_kind is not True:
            self.set_win_amount(1)
        elif pair:
            self.set_win_amount(0)
        else:
            self.player_win = False

            self.gameover = (self.player.credits == 0)
            if self.gameover is True:
                self.new_highscore = self.player.has_new_highscore()

    def get_win_amount(self):
        return 'You won ' + str(self.current_win) + ' credits!'

    def set_win_amount(self, number):
        payouts = [1, 2, 3, 4, 6, 9, 25, 50, 250]
        win_type = ['One Pair!',
                    'Two pairs!',
                    'Three of a kind!',
                    'Straight!',
                    'Flush!',
                    'Full House!',
                    'Four of a kind!',
                    'Straight Flush!',
                    'Royal Flush!']

        self.winning_hand = win_type[number]

        if self.current_bet == 5 and number == 8:
            self.current_win = 4000
        else:
            self.current_win = payouts[number] * self.current_bet

    def claim_win(self):
        self.player.add_credits(self.current_win)
        if self.double_active:
            self.player.double_win(self.current_win)
        self.current_win = 0
        self.player_win = False
        self.double_active = False

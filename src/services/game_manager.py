"""Module game_manager.py

    This module handles all gameplay logic.
"""

from entities.deck import Deck
from entities.player import Player
from entities.suit import Suit
from repositories.player_repository import PlayerRepository


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
        self.player_repository = PlayerRepository()
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

    def reset_game(self, reset_bet=True):
        if reset_bet:
            self.current_bet = 1
        self.current_win = 0
        self.deal_active = False
        self.game_active = False
        self.double_active = False
        self.gameover = False
        self.bad_guess = False
        self.player_win = False
        self.player_hand = [None, None, None, None, None]
        self.card_on_hold = [False, False, False, False, False]
        self.new_highscore = False

    def submit_highscore(self, name):
        self.player_repository.update_highscore(self.player, name)
        self.player_repository.save(self.player)
        self.reset_game()

    def new_game(self):
        self.reset_game()
        self.player = Player()
        return self.player_repository.has_savegame() is False

    def continue_game(self):
        self.reset_game()
        self.player = self.player_repository.load()
        return self.player.credits != 0

    def quit_game(self):
        self.reset_game()
        self.player_repository.save(self.player)

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
        self.card_on_hold[value] = not self.card_on_hold[value]

    def double(self):
        """Setups the game ready for doubling.
        """
        self.player_hand = [None, None, None, None, None]
        self.player_win = False
        self.double_active = True
        self.deal_active = False

    def reset_double(self):
        self.reset_game(False)

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

            self.check_if_game_over()
        else:
            self.player_win = True
            self.current_win = self.current_win * 2
            self.player.successful_double(True)

    def deal(self):
        if self.deal_active is not True:
            self.check_if_game_over()
            self.deck = Deck()

            if self.player.credits < self.current_bet:
                self.current_bet = self.player.credits

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
        combinations = {'pair': False,
                        'two_pairs': False,
                        'three_of_a_kind': False,
                        'four_of_a_kind': False,
                        'straight': True,
                        'low_ace_straight': False,
                        'flush': True,
                        'royal_flush': False}

        for i in range(1, 5):
            if combinations['straight'] and i == 4 and \
               player_hand[i-1].rank == 5 and \
               player_hand[i].rank == 14:

                combinations['low_ace_straight'] = True

            if player_hand[i-1].rank != player_hand[i].rank - 1:
                combinations['straight'] = False

            if player_hand[i-1].suit != player_hand[i].suit:
                combinations['flush'] = False

            if player_hand[i-1].rank == player_hand[i].rank:
                count += 1
            else:
                count = 1

            if count == 2:
                pair_count += 1

            if combinations['pair'] is False and pair_count == 1:
                combinations['pair'] = True

            if combinations['two_pairs'] is False and pair_count == 2:
                combinations['two_pairs'] = True

            if combinations['three_of_a_kind'] is False and count == 3:
                combinations['three_of_a_kind'] = True

            if combinations['four_of_a_kind'] is False and count == 4:
                combinations['four_of_a_kind'] = True

        combinations['royal'] = player_hand[0].rank == 10 and \
            player_hand[0].suit == Suit.hearts

        self.check_win_amount(combinations)

    def check_win_amount(self, combinations):
        if combinations['straight'] and combinations['flush']:
            if combinations['royal']:
                self.set_win_amount(8)
            else:
                self.set_win_amount(7)

        elif combinations['four_of_a_kind']:
            self.set_win_amount(6)
        elif combinations['two_pairs'] and combinations['three_of_a_kind']:
            self.set_win_amount(5)
        elif combinations['flush']:
            self.set_win_amount(4)
        elif combinations['straight'] or combinations['low_ace_straight']:
            self.set_win_amount(3)
        elif combinations['three_of_a_kind']:
            self.set_win_amount(2)
        elif combinations['two_pairs']:
            self.set_win_amount(1)
        elif combinations['pair']:
            self.set_win_amount(0)
        else:
            self.player_win = False
            self.check_if_game_over()

    def check_if_game_over(self):
        self.gameover = (self.player.credits == 0)
        if self.gameover is True:
            self.new_highscore = self.player_repository.is_new_highscore(
                self.player)

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
        self.reset_game(False)

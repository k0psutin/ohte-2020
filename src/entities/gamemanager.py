from entities.deck import Deck


class GameManager():
    def __init__(self):
        self.player_win = False
        self.credits = 10

        self.current_bet = 1
        self.current_win = 0
        self.winning_hand = ''

        self.deck = Deck()

        self.player_hand = [None, None, None, None, None]
        self.card_on_hold = [False, False, False, False, False]
        self.cards = [None, None, None, None, None]

        self.deal_active = False
        self.game_active = False
        self.double_active = False
        self.gameover = False

    def take_credits(self):
        if self.credits < self.current_bet:
            self.current_bet = self.credits
        self.credits -= self.current_bet

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
        self.player_hand = [None, None, None, None, None]
        self.player_win = False
        self.double_active = True
        self.deal_active = False

    def low(self):
        self.player_hand[0] = self.deck.draw_one_card()
        card_rank = self.player_hand[0].rank
        if card_rank == 14:
            card_rank = 1

        if card_rank <= 7:
            self.current_win = self.current_win * 2
            self.player_win = True
            self.winning_hand = 'Low Card!'
        else:
            self.current_win = 0
            self.double_active = False
            if self.credits == 0:
                self.gameover = True
                self.game_active = False

    def high(self):
        self.player_hand[0] = self.deck.draw_one_card()

        if self.player_hand[0].rank > 7:
            self.current_win = self.current_win * 2
            self.player_win = True
            self.winning_hand = 'High Card!'
        else:
            self.current_win = 0
            self.double_active = False
            if self.credits == 0:
                self.gameover = True
                self.game_active = False

    def deal(self):
        self.double_active = False

        if self.gameover:
            return

        if self.deal_active is not True:
            if self.credits == 0:
                self.gameover = True
                return
            self.take_credits()

        self.game_active = True
        self.player_hand = []

        for i in range(0, 5):
            if self.card_on_hold[i] is False:
                self.cards[i] = self.deck.draw_one_card()

            self.player_hand.append(self.cards[i])

        if self.deal_active:
            self.check_player_hand()
            self.deal_active = False
            self.card_on_hold = [False, False, False, False, False]
        else:
            self.deal_active = True

    def check_player_hand(self):
        player_hand = list(self.player_hand)
        player_hand.sort()
        self.player_win = True

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
        self.credits += self.current_win
        self.current_win = 0
        self.player_win = False

from ui.components.button import Button
from ui.components.label import Label
from ui.components.gamecard import GameCard


class Play():
    def __init__(self, gamestate):
        self.gamestate = gamestate

        self.card_offset_x = -0.37
        self.card_offset_y = -0.3

        self.hold_offset_x_increment = 0.15
        self.hold_start_offset_x = -0.3

        self.card_objects = [None, None, None, None, None]
        self.hold_objects = []
        self.play_main_objects = []
        self.play_bet_objects = []

        self.open_payout = Button('Payouts',
                                  self.gamestate.button_width,
                                  self.gamestate.button_height,
                                  0.43,
                                  -0.47,
                                  gamestate.font,
                                  gamestate.display,
                                  gamestate.payout)

        for i in range(0, 5):
            hold_button = Button('Hold',
                                 self.gamestate.button_width,
                                 self.gamestate.button_height,
                                 self.hold_start_offset_x,
                                 0.2,
                                 gamestate.font,
                                 gamestate.display,
                                 gamestate.gamemanager.hold_card,
                                 i)
            self.hold_objects.append(hold_button)
            self.hold_start_offset_x += self.hold_offset_x_increment

        self.deal_button = Button(
            'Deal',
            self.gamestate.button_width,
            self.gamestate.button_height,
            0.40,
            0.44,
            gamestate.font,
            gamestate.display,
            self.deal)

        self.credit_text = Label(
            'Credits:',
            self.gamestate.label_width,
            self.gamestate.label_height,
            -0.4,
            0.53,
            gamestate,
            gamestate.font)

        self.show_credits = Label(
            str(self.gamestate.gamemanager.credits),
            self.gamestate.label_width,
            self.gamestate.label_height,
            -0.3,
            0.53,
            gamestate,
            gamestate.font)

        self.bet_text = Label('Bet',
                              self.gamestate.label_width,
                              self.gamestate.label_height,
                              0.13,
                              0.53,
                              gamestate,
                              self.gamestate.font)

        self.bet_amount = Button(
            str(gamestate.gamemanager.current_bet),
            self.gamestate.small_button_width,
            self.gamestate.small_button_height,
            0.20,
            0.44,
            gamestate.font, gamestate.display)

        self.increase_bet = Button('+',
                                   self.gamestate.small_button_width,
                                   self.gamestate.small_button_height,
                                   0.25,
                                   0.44,
                                   gamestate.font,
                                   gamestate.display,
                                   gamestate.gamemanager.increase_bet)

        self.decrease_bet = Button('-',
                                   self.gamestate.small_button_width,
                                   self.gamestate.small_button_height,
                                   0.15,
                                   0.44,
                                   gamestate.font,
                                   gamestate.display,
                                   gamestate.gamemanager.decrease_bet)

        self.play_main_objects.append(self.open_payout)
        self.play_main_objects.append(self.deal_button)
        self.play_main_objects.append(self.credit_text)
        self.play_main_objects.append(self.show_credits)
        self.play_main_objects.append(self.bet_text)
        self.play_main_objects.append(self.bet_amount)

        self.play_bet_objects.append(self.increase_bet)
        self.play_bet_objects.append(self.decrease_bet)

    def update(self, event):
        if self.gamestate.gamemanager.deal_active:
            for i in range(0, 5):
                self.hold_objects[i].update(
                    event,
                    self.gamestate.gamemanager.card_on_hold[i])

        if self.gamestate.gamemanager.deal_active is False:
            for bet_obj in self.play_bet_objects:
                bet_obj.update(event)

        self.bet_amount.change_button_text(
            str(self.gamestate.gamemanager.current_bet))

        self.show_credits.change_text(
            str(self.gamestate.gamemanager.credits))

        for main_obj in self.play_main_objects:
            main_obj.update(event)

    def deal(self):
        if self.gamestate.gamemanager.gameover:
            return

        self.card_objects = []
        self.gamestate.gamemanager.deal()
        cards = self.gamestate.gamemanager.player_hand
        offset_x = self.card_offset_x
        offset_y = self.card_offset_y

        for i in range(0, 5):
            card_obj = GameCard(cards[i],
                                self.gamestate.card_width,
                                self.gamestate.card_height,
                                offset_x,
                                offset_y,
                                self.gamestate.display,
                                self.gamestate.font)
            self.card_objects.append(card_obj)
            offset_x += 0.15

    def update_cards(self):
        for card in self.card_objects:
            if card is not None:
                card.update()

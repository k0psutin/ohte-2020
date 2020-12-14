from ui.components.button import Button
from ui.components.label import Label
from ui.components.gamecard import GameCard

import pygame


class Play():
    def __init__(self, game_state, game_manager):
        self.game_state = game_state
        self.game_manager = game_manager

        self.card_offset_x = -0.37
        self.card_offset_y = -0.3

        self.hold_offset_x_increment = 0.15
        self.hold_start_offset_x = -0.3

        self.card_objects = [None, None, None, None, None]
        self.hold_objects = []
        self.play_main_objects = []
        self.play_bet_objects = []

        self.credits = 0

        self.open_payout = Button('Payouts',
                                  self.game_state.button_width,
                                  self.game_state.button_height,
                                  0.43,
                                  -0.47,
                                  game_state.font,
                                  game_state.display,
                                  game_state.payout)

        for i in range(0, 5):
            hold_button = Button('Hold',
                                 self.game_state.button_width,
                                 self.game_state.button_height,
                                 self.hold_start_offset_x,
                                 0.2,
                                 game_state.font,
                                 game_state.display,
                                 game_manager.hold_card,
                                 i)
            self.hold_objects.append(hold_button)
            self.hold_start_offset_x += self.hold_offset_x_increment

        self.deal_button = Button(
            'Deal',
            self.game_state.button_width,
            self.game_state.button_height,
            0.40,
            0.44,
            game_state.font,
            game_state.display,
            game_manager.deal)

        self.credit_text = Label(
            'Credits:',
            self.game_state.label_width,
            self.game_state.label_height,
            -0.4,
            0.53,
            game_state,
            game_state.font)

        self.show_credits = Label(
            str(self.credits),
            self.game_state.label_width,
            self.game_state.label_height,
            -0.3,
            0.53,
            game_state,
            game_state.font)

        self.bet_text = Label('Bet',
                              self.game_state.label_width,
                              self.game_state.label_height,
                              0.13,
                              0.53,
                              game_state,
                              self.game_state.font)

        self.bet_amount = Button(
            str(game_manager.current_bet),
            self.game_state.small_button_width,
            self.game_state.small_button_height,
            0.20,
            0.44,
            game_state.font, game_state.display)

        self.increase_bet = Button('+',
                                   self.game_state.small_button_width,
                                   self.game_state.small_button_height,
                                   0.25,
                                   0.44,
                                   game_state.font,
                                   game_state.display,
                                   game_manager.increase_bet)

        self.decrease_bet = Button('-',
                                   self.game_state.small_button_width,
                                   self.game_state.small_button_height,
                                   0.15,
                                   0.44,
                                   game_state.font,
                                   game_state.display,
                                   game_manager.decrease_bet)

        self.play_main_objects.append(self.open_payout)
        self.play_main_objects.append(self.deal_button)
        self.play_main_objects.append(self.credit_text)
        self.play_main_objects.append(self.show_credits)
        self.play_main_objects.append(self.bet_text)
        self.play_main_objects.append(self.bet_amount)

        self.play_bet_objects.append(self.increase_bet)
        self.play_bet_objects.append(self.decrease_bet)

        offset_x = self.card_offset_x
        offset_y = self.card_offset_y

        for i in range(0, 5):
            self.card_objects[i] = GameCard(None,
                                            self.game_state.card_width,
                                            self.game_state.card_height,
                                            offset_x,
                                            offset_y,
                                            self.game_state.display,
                                            self.game_state.font)
            offset_x += 0.15

    def update(self, event):
        if self.game_state.game_manager.deal_active:
            for i in range(0, 5):
                self.hold_objects[i].update(
                    event,
                    self.game_state.game_manager.card_on_hold[i])

        if self.game_state.game_manager.deal_active is False:
            for bet_obj in self.play_bet_objects:
                bet_obj.update(event)

        self.bet_amount.change_button_text(
            str(self.game_state.game_manager.current_bet))

        self.show_credits.change_text(
            str(self.game_state.game_manager.player.credits))

        for main_obj in self.play_main_objects:
            main_obj.update(event)

    def update_cards(self):
        cards = self.game_manager.player_hand

        for i in range(0, 5):
            self.card_objects[i].update_card(cards[i])

        for card in self.card_objects:
            card.update()

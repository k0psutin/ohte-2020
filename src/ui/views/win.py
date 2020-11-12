from ui.components.button import Button


class Win():
    def __init__(self, game_state, game_manager):
        self.display = game_state.display
        self.game_state = game_state
        self.game_manager = game_manager
        self.font = game_state.font
        self.winning_hand_text = 'Four of a kind!'
        self.win_text = 'You won 0 credits!'

        self.double = Button('Double or nothing!',
                             self.game_state.button_width,
                             self.game_state.button_height,
                             -0.075,
                             0.0,
                             self.font,
                             self.display,
                             self.game_manager.double)
        self.claim = Button('Claim win',
                            self.game_state.button_width,
                            self.game_state.button_height,
                            0.075,
                            0.0,
                            self.font,
                            self.display,
                            self.game_manager.claim_win)
        self.winning_hand = Button(
            self.winning_hand_text,
            self.game_state.button_width * 2,
            self.game_state.button_height,
            0.0,
            -0.15,
            self.font,
            self.display)
        self.win = Button(
            self.win_text,
            self.game_state.button_width * 2,
            self.game_state.button_height,
            0.0,
            -0.1,
            self.font,
            self.display)

    def update(self, event):
        self.double.update(event)
        self.claim.update(event)
        self.win.update(event)
        self.winning_hand.update(event)
        self.win.change_button_text(self.game_manager.get_win_amount())
        self.winning_hand.change_button_text(
            self.game_manager.winning_hand)

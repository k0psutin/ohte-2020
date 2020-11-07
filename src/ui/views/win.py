from ui.components.button import Button


class Win():
    def __init__(self, gamestate, game_manager):
        self.display = gamestate.display
        self.gamestate = gamestate
        self.gamemanager = game_manager
        self.font = gamestate.font
        self.winning_hand_text = 'Four of a kind!'
        self.win_text = 'You won 0 credits!'

        self.double = Button('Double or nothing!',
                             self.gamestate.button_width,
                             self.gamestate.button_height,
                             -0.075,
                             0.0,
                             self.font,
                             self.display,
                             self.gamestate.double)
        self.claim = Button('Claim win',
                            self.gamestate.button_width,
                            self.gamestate.button_height,
                            0.075,
                            0.0,
                            self.font,
                            self.display,
                            self.gamestate.claim)
        self.winning_hand = Button(
            self.winning_hand_text,
            self.gamestate.button_width * 2,
            self.gamestate.button_height,
            0.0,
            -0.15,
            self.font,
            self.display)
        self.win = Button(
            self.win_text,
            self.gamestate.button_width * 2,
            self.gamestate.button_height,
            0.0,
            -0.1,
            self.font,
            self.display)

    def update(self, event):
        self.double.update(event)
        self.claim.update(event)
        self.win.update(event)
        self.winning_hand.update(event)
        self.win.change_button_text(self.gamemanager.get_win_amount())
        self.winning_hand.change_button_text(
            self.gamemanager.winning_hand)

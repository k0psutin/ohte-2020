from ui.components.button import Button


class Confirmation():
    def __init__(self, text, yes, no, game_state, width_multiplier=2):

        self.font = game_state.font

        self.text_width = game_state.button_width * width_multiplier

        self.yes_button = Button('Yes',
                                 game_state.button_width,
                                 game_state.button_height,
                                 -0.075,
                                 0.0,
                                 self.font,
                                 game_state.display,
                                 yes)
        self.no_button = Button('No',
                                game_state.button_width,
                                game_state.button_height,
                                0.075,
                                0.0,
                                self.font,
                                game_state.display,
                                no)
        self.quit_game_text = Button(
            text,
            self.text_width,
            game_state.button_height,
            0.0,
            -0.1,
            self.font,
            game_state.display)

    def update(self, event):
        self.yes_button.update(event)
        self.no_button.update(event)
        self.quit_game_text.update(event)

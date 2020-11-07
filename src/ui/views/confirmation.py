from ui.components.button import Button


class Confirmation():
    def __init__(self, text, yes_action, no_action, gamestate, font):
        self.yes_action = yes_action
        self.no_action = no_action
        self.text = text

        self.display = gamestate.display
        self.font = font

        self.yes_button = Button('Yes',
                                 gamestate.button_width,
                                 gamestate.button_height,
                                 -0.075,
                                 0.0,
                                 self.font,
                                 self.display,
                                 self.yes_action)
        self.no_button = Button('No',
                                gamestate.button_width,
                                gamestate.button_height,
                                0.075,
                                0.0,
                                self.font,
                                self.display,
                                self.no_action)
        self.quit_game_text = Button(
            self.text,
            gamestate.button_width * 2,
            gamestate.button_height,
            0.0,
            -0.1,
            self.font,
            self.display)

    def update(self, event):
        self.yes_button.update(event)
        self.no_button.update(event)
        self.quit_game_text.update(event)

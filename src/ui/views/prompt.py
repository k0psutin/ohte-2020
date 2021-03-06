from ui.components.button import Button


class Prompt():
    def __init__(self, text, game_state, game_manager, action):
        self.display = game_state.display

        self.game_state = game_state
        self.game_manager = game_manager
        self.font = game_state.font
        self.text = text
        self.x_offset = 0.0
        self.y_offset = -0.05

        self.ok_button = Button('Ok',
                                self.game_state.button_width,
                                self.game_state.button_height,
                                self.x_offset,
                                self.y_offset,
                                self.font,
                                self.display,
                                action)
        self.prompt = Button(self.text,
                             self.game_state.button_width * 2,
                             self.game_state.button_height,
                             self.x_offset,
                             self.y_offset - 0.1,
                             self.font,
                             self.display)

    def update(self, event):
        self.prompt.update(event)
        self.ok_button.update(event)

from ui.components.button import Button


class Prompt():
    def __init__(self, text, gamestate, game_manager, action):
        self.display = gamestate.display
        self.gamestate = gamestate
        self.gamemanager = game_manager
        self.font = gamestate.font
        self.text = text

        self.ok_button = Button('Ok',
                                self.gamestate.button_width,
                                self.gamestate.button_height,
                                0.0,
                                0.0,
                                self.font,
                                self.display,
                                action)
        self.prompt = Button(self.text,
                             self.gamestate.button_width * 2,
                             self.gamestate.button_height,
                             0.0,
                             -0.1,
                             self.font,
                             self.display)

    def update(self, event):
        self.prompt.update(event)
        self.ok_button.update(event)

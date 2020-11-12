from ui.components.button import Button
from ui.components.label import Label


class Scoreboard():
    def __init__(self, game_state):
        self.scoreboard_text = Label('Kings and Queens of poker',
                                     game_state.small_button_width,
                                     game_state.small_button_height,
                                     -0.175,
                                     -0.4,
                                     game_state,
                                     game_state.large_font)
        self.close_scoreboard_button = Button('Close',
                                              game_state.button_width,
                                              game_state.button_height,
                                              0,
                                              0.45,
                                              game_state.font,
                                              game_state.display,
                                              game_state.main_menu)

        self.scoreboard_objects = []

        self.scoreboard_objects.append(self.scoreboard_text)
        self.scoreboard_objects.append(self.close_scoreboard_button)

    def update(self, event):
        for obj in self.scoreboard_objects:
            obj.update(event)

from ui.components.button import Button
from ui.components.label import Label


class Scoreboard():
    def __init__(self, gamestate):
        self.scoreboard_text = Label('Kings and Queens of poker',
                                     gamestate.small_button_width,
                                     gamestate.small_button_height,
                                     -0.175,
                                     -0.4,
                                     gamestate,
                                     gamestate.large_font)
        self.close_scoreboard_button = Button('Close',
                                              gamestate.button_width,
                                              gamestate.button_height,
                                              0,
                                              0.45,
                                              gamestate.font,
                                              gamestate.display,
                                              gamestate.main_menu)

        self.scoreboard_objects = []

        self.scoreboard_objects.append(self.scoreboard_text)
        self.scoreboard_objects.append(self.close_scoreboard_button)

    def update(self, event):
        for obj in self.scoreboard_objects:
            obj.update(event)

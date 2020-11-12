from ui.components.button import Button
from ui.components.label import Label


class Payout():
    def __init__(self, game_state):
        self.payout_text = Label(
            'Payouts',
            game_state.small_button_width,
            game_state.small_button_height,
            -0.05,
            -0.4,
            game_state,
            game_state.large_font)
        self.close_payout_button = Button('Close',
                                          game_state.button_width,
                                          game_state.button_height,
                                          0,
                                          0.45,
                                          game_state.font,
                                          game_state.display,
                                          game_state.play)

        self.payout_objects = []

        self.payout_objects.append(self.payout_text)
        self.payout_objects.append(self.close_payout_button)

    def update(self, event):
        for obj in self.payout_objects:
            obj.update(event)

from ui.components.button import Button
from ui.components.label import Label


class Payout():
    def __init__(self, gamestate):
        self.payout_text = Label(
            'Payouts',
            gamestate.small_button_width,
            gamestate.small_button_height,
            -0.05,
            -0.4,
            gamestate,
            gamestate.large_font)
        self.close_payout_button = Button('Close',
                                          gamestate.button_width,
                                          gamestate.button_height,
                                          0,
                                          0.45,
                                          gamestate.font,
                                          gamestate.display,
                                          gamestate.play)

        self.payout_objects = []

        self.payout_objects.append(self.payout_text)
        self.payout_objects.append(self.close_payout_button)

    def update(self, event):
        for obj in self.payout_objects:
            obj.update(event)

from ui.components.button import Button
from ui.components.label import Label
from ui.components.gamecard import GameCard


class Double():
    def __init__(self, gamestate):

        self.gamestate = gamestate

        self.low_button = Button('Low',
                                 gamestate.button_width,
                                 gamestate.button_height,
                                 -0.1,
                                 0.2,
                                 gamestate.font,
                                 gamestate.display,
                                 gamestate.gamemanager.low)
        self.high_button = Button('High',
                                  gamestate.button_width,
                                  gamestate.button_height,
                                  0.1,
                                  0.2,
                                  gamestate.font,
                                  gamestate.display,
                                  gamestate.gamemanager.high)

        self.credit_text = Label('Credits:',
                                 gamestate.label_width,
                                 gamestate.label_height,
                                 -0.4,
                                 0.53,
                                 gamestate,
                                 gamestate.font)

        self.show_credits = Label(
            str(self.gamestate.gamemanager.credits),
            self.gamestate.label_width,
            self.gamestate.label_height,
            -0.3,
            0.53,
            gamestate,
            gamestate.font)

        self.double_objects = []

        # self.double_objects.append(self.payouts)
        self.double_objects.append(self.low_button)
        self.double_objects.append(self.high_button)
        self.double_objects.append(self.credit_text)
        self.double_objects.append(self.show_credits)

    def update(self, event):
        if self.gamestate.gamemanager.player_hand[0] is not None:
            self.card_obj = GameCard(self.gamestate.gamemanager.player_hand[0],
                                     self.gamestate.card_width,
                                     self.gamestate.card_height,
                                     -0.07,
                                     -0.3,
                                     self.gamestate.display,
                                     self.gamestate.font)

            self.card_obj.update()

        for obj in self.double_objects:
            if obj is not None:
                obj.update(event)

        self.show_credits.change_text(str(self.gamestate.gamemanager.credits))

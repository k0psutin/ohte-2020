from ui.components.button import Button
from ui.components.label import Label


class Payout():
    def __init__(self, game_state):
        payouts = [1, 2, 3, 4, 6, 9, 25, 50, 250]
        win_type = ['One Pair',
                    'Two pairs',
                    'Three of a kind',
                    'Straight',
                    'Flush',
                    'Full House',
                    'Four of a kind',
                    'Straight Flush',
                    'Royal Flush']
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

        self.bet_text = Label(
            'Bet:',
            game_state.small_button_width,
            game_state.small_button_height,
            -0.15,
            0.3,
            game_state,
            game_state.font)

        self.payout_objects.append(self.bet_text)

        for i in range(1, 6):
            self.payout_objects.append(Label(
                str(i),
                game_state.small_button_width,
                game_state.small_button_height,
                -0.15+(i*0.1),
                0.3,
                game_state,
                game_state.font))

        for i in range(0, 9):
            self.payout_objects.append(Label(
                win_type[i],
                game_state.small_button_width,
                game_state.small_button_height,
                -0.3,
                0.2-(i*0.05),
                game_state,
                game_state.font))

            for j in range(1, 6):
                amount = str(payouts[i] * j)
                if i == 8 and j == 5:
                    amount = '4000'
                self.payout_objects.append(Label(
                    amount,
                    game_state.small_button_width,
                    game_state.small_button_height,
                    -0.15+(j*0.1),
                    0.2-(i*0.05),
                    game_state,
                    game_state.font))

    def update(self, event):
        for obj in self.payout_objects:
            obj.update(event)

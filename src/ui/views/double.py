from ui.components.button import Button
from ui.components.label import Label
from ui.components.gamecard import GameCard


class Double():
    def __init__(self, game_state, game_manager):

        self.game_state = game_state
        self.game_manager = game_manager

        self.low_button = Button('Low',
                                 game_state.button_width,
                                 game_state.button_height,
                                 -0.1,
                                 0.2,
                                 game_state.font,
                                 game_state.display,
                                 game_manager.guess_card_rank,
                                 'low')
        self.high_button = Button('High',
                                  game_state.button_width,
                                  game_state.button_height,
                                  0.1,
                                  0.2,
                                  game_state.font,
                                  game_state.display,
                                  game_manager.guess_card_rank,
                                  'high')

        self.credit_text = Label('Credits:',
                                 game_state.label_width,
                                 game_state.label_height,
                                 -0.4,
                                 0.53,
                                 game_state,
                                 game_state.font)

        self.show_credits = Label(
            '',
            self.game_state.label_width,
            self.game_state.label_height,
            -0.3,
            0.53,
            game_state,
            game_state.font)

        self.double_objects = []
        self.playview_objects = []

        self.double_objects.append(self.low_button)
        self.double_objects.append(self.high_button)
        self.playview_objects.append(self.credit_text)
        self.playview_objects.append(self.show_credits)

    def update(self, event):
        self.card_obj = GameCard(
            self.game_manager.player_hand[0],
            self.game_state.card_width,
            self.game_state.card_height,
            -0.07,
            -0.3,
            self.game_state.display,
            self.game_state.font)

        self.card_obj.update()

        for obj in self.double_objects:
            if self.game_manager.player_win is not True and self.game_manager.bad_guess is not True:
                obj.update(event)

        for obj in self.playview_objects:
            if obj is not None:
                obj.update(event)

        self.show_credits.change_text(
            str(self.game_manager.player.credits))

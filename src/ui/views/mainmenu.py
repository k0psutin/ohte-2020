from ui.components.button import Button


class Mainmenu():
    def __init__(self, game_state):
        self.new_game_button = Button('New game',
                                      game_state.button_width,
                                      game_state.button_height,
                                      0, - 0.2,
                                      game_state.font,
                                      game_state.display,
                                      game_state.new_game)
        self.continue_button = Button('Continue',
                                      game_state.button_width,
                                      game_state.button_height,
                                      0, -0.1,
                                      game_state.font,
                                      game_state.display,
                                      game_state.continue_game)
        self.scoreboard_button = Button('Scoreboard',
                                        game_state.button_width,
                                        game_state.button_height,
                                        0, 0,
                                        game_state.font,
                                        game_state.display,
                                        game_state.scoreboard)
        self.quit_button = Button('Quit', game_state.button_width,
                                  game_state.button_height,
                                  0, 0.1,
                                  game_state.font,
                                  game_state.display,
                                  game_state.quit_game)

        self.mainmenu_objects = []
        self.mainmenu_objects.append(self.new_game_button)
        self.mainmenu_objects.append(self.continue_button)
        self.mainmenu_objects.append(self.scoreboard_button)
        self.mainmenu_objects.append(self.quit_button)

    def get_components(self):
        return self.mainmenu_objects

    def update(self, event):
        for obj in self.mainmenu_objects:
            obj.update(event)

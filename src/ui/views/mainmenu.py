from ui.components.button import Button


class Mainmenu():
    def __init__(self, gamestate):
        self.new_game_button = Button('New game',
                                      gamestate.button_width,
                                      gamestate.button_height,
                                      0, - 0.2,
                                      gamestate.font,
                                      gamestate.display,
                                      gamestate.new_game)
        self.continue_button = Button('Continue',
                                      gamestate.button_width,
                                      gamestate.button_height,
                                      0, -0.1,
                                      gamestate.font,
                                      gamestate.display,
                                      gamestate.continue_game)
        self.scoreboard_button = Button('Scoreboard',
                                        gamestate.button_width,
                                        gamestate.button_height,
                                        0, 0,
                                        gamestate.font,
                                        gamestate.display,
                                        gamestate.scoreboard)
        self.quit_button = Button('Quit', gamestate.button_width,
                                  gamestate.button_height,
                                  0, 0.1,
                                  gamestate.font,
                                  gamestate.display,
                                  gamestate.quit_game)

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

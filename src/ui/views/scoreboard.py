from ui.components.button import Button
from ui.components.label import Label


class Scoreboard():
    def __init__(self, game_state, game_manager):
        self.game_state = game_state
        self.game_manager = game_manager
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

        self.highscores = game_manager.player_repository.highscores
        scoreboard_header = ['Name', 'Best credits',
                             'Best double win', 'Best double streak']

        self.scoreboard_entries = []

        for i in range(0, 4):
            self.scoreboard_objects.append(Label(
                scoreboard_header[i],
                game_state.small_button_width,
                game_state.small_button_height,
                -0.25+(i*0.13),
                -0.3,
                game_state,
                game_state.font))
        self.entries = []
        i = 0
        for highscore in self.highscores:
            j = 0
            row = []
            for entry in highscore.values():
                label = Label(
                    str(entry),
                    game_state.small_button_width,
                    game_state.small_button_height,
                    -0.25+(j*0.15),
                    0.2-(i*0.05),
                    game_state,
                    game_state.font)

                self.scoreboard_entries.append(label)
                row.append(label)
                j += 1
            self.entries.append(row)
            i += 1

    def update(self, event):
        self.highscores = self.game_manager.player_repository.highscores

        for i in range(0, 10):
            for j in range(0, 4):
                current = list(self.highscores[i].values())
                self.entries[i][j].change_text(str(current[j]))

        for obj in self.scoreboard_entries:
            obj.update(event)

        for obj in self.scoreboard_objects:
            obj.update(event)

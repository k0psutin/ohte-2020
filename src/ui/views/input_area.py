from ui.components.button import Button
from ui.components.label import Label

import pygame
import string


class InputArea():
    def __init__(self, game_state, game_manager):
        self.display = game_state.display

        self.game_state = game_state
        self.game_manager = game_manager
        self.font = game_state.font
        self.input_text = ''

        self.input_objects = []

        self.scoreboard_text = Label('Gameover',
                                     game_state.small_button_width,
                                     game_state.small_button_height,
                                     -0.05,
                                     -0.4,
                                     game_state,
                                     game_state.large_font)
        self.input_objects.append(self.scoreboard_text)

        self.highscore_text = Label('New highscore!',
                                    game_state.small_button_width,
                                    game_state.small_button_height,
                                    -0.09,
                                    -0.3,
                                    game_state,
                                    game_state.large_font)

        self.input_objects.append(self.highscore_text)

        self.submit_button = Button('Submit',
                                    self.game_state.button_width,
                                    self.game_state.button_height,
                                    0.0,
                                    0.0,
                                    self.font,
                                    self.display,
                                    self.submit_highscore)

        self.input_header = Button('Enter initials',
                                   self.game_state.button_width * 2,
                                   self.game_state.button_height,
                                   0.0,
                                   -0.2,
                                   self.font,
                                   self.display)
        self.input_objects.append(self.input_header)

        self.input_area_bground = Button('',
                                         self.game_state.button_width * 2,
                                         self.game_state.button_height,
                                         0.0,
                                         -0.1,
                                         self.font,
                                         self.display)
        self.input_objects.append(self.input_area_bground)

        self.input_area = Label(self.input_text,
                                self.game_state.button_width * 2,
                                self.game_state.button_height,
                                0.13,
                                -0.08,
                                self.game_state,
                                self.font, (170, 170, 170))
        self.input_objects.append(self.input_area)

    def update(self, event):
        for obj in self.input_objects:
            obj.update(event)

        if len(self.input_text) == 3:
            self.submit_button.update(event)

        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            txt_length = len(self.input_text)
            if txt_length < 3 and key in string.ascii_letters:
                self.input_text += key
            if txt_length > 0 and key == 'backspace':
                self.input_text = self.input_text[:-1]

            self.input_area.change_text(self.input_text.upper())

    def submit_highscore(self):
        if len(self.input_text) < 3:
            return
        self.game_manager.submit_highscore(self.input_text.upper())
        self.game_state.state = 'main_menu'

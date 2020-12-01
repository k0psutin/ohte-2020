"""Module game_state.py

    This module handles all UI related logic.
"""

import pygame
import sys

from ui.views.confirmation import Confirmation
from ui.views.mainmenu import Mainmenu
from ui.views.play import Play
from ui.views.scoreboard import Scoreboard
from ui.views.payout import Payout
from ui.views.double import Double
from ui.views.win import Win
from ui.views.prompt import Prompt

from services.game_manager import GameManager


class GameState():
    """Class that handles UI logic.

    This is a 'switcher'-class that switches UI views depending on
    the state of the game. Game is running in one loop, and views
    are controlled with if-else statements, and by an attribute
    `state`.

    Attributes:

        state: A String, name of the current state.

    Views:

       Mainmenu, Playview, Scoreboard, Payout
    """

    def __init__(self):
        """Constructor initializes game settings and all the required
           components for the multiple views, such as the GameManager,
           that handles the game logic.


        Typical usage example:
            self.game_state = GameState()
        """

        self.state = 'main_menu'

        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()

        # Initialize game settings

        self.background_color = (235, 235, 235)

        self.display = pygame.display.set_mode((1440, 900))
        self.width = self.display.get_width()
        self.height = self.display.get_height()

        # Size settings

        self.card_width = 0.139 * self.width
        self.card_height = 0.33 * self.height
        self.button_width = self.card_width
        self.button_height = 0.056 * self.height
        self.small_button_width = 0.0347 * self.width
        self.small_button_height = self.button_height
        self.large_button_height = 0.22 * self.height

        self.label_width = self.button_width
        self.label_height = self.large_button_height
        self.font_size = int(round(0.02084 * self.width))
        self.large_font_size = int(round(0.02084 * self.width)) * 2
        self.font = pygame.font.Font(None, self.font_size)
        self.large_font = pygame.font.Font(None, self.large_font_size)

        # Initialize game manager

        self.game_manager = GameManager()

        pygame.display.set_caption('Videopoker')

        # Initialize game view

        self.play_view = Play(self, self.game_manager)

        # Initialize main menu view

        self.mainmenu_view = Mainmenu(self)

        # Initialize scoreboard view

        self.scoreboard_view = Scoreboard(self)

        # Initialize payout view

        self.payout_view = Payout(self)

        # Initialize double view
        self.double_view = Double(self, self.game_manager)

        # Initialize bad double guess view
        self.loose_view = Prompt(
            'Wrong guess. Better luck next time!',
            self,
            self.game_manager,
            self.game_manager.end_double)

        # Initialize win view
        self.win_view = Win(self, self.game_manager)

        # Initialize quit confirmation view
        self.confirm_quit_play = Confirmation(
            'Quit to mainmenu?',
            self.main_menu,
            self.play,
            self)

        # Initialize old savegame found view
        self.confirm_new_game_view = Confirmation(
            'Starting a new game overwrites old save, continue?',
            self.new_game,
            self.main_menu,
            self,
            3)

        # Initialize game over view
        self.gameover_view = Prompt(
            'No credits left. Game over.',
            self,
            self.game_manager,
            self.game_over)

    def main_menu(self):
        self.state = 'main_menu'

    def scoreboard(self):
        self.state = 'scoreboard'

    def payout(self):
        self.state = 'payout'

    def continue_game(self):
        self.game_manager.continue_game()
        if self.game_manager.player is not None:
            self.state = 'play'

    def confirm_new_game(self):
        self.game_manager.new_game()
        player = self.game_manager.player.load_player()
        if player is not None:
            self.state = 'confirm_new_game'
        else:
            self.new_game()

    def new_game(self):
        self.game_manager.new_game()
        self.state = 'play'

    def quit_to_mainmenu(self):
        self.game_manager.quit_game()
        self.state = 'quit_to_mainmenu'

    def game_over(self):
        self.game_manager.quit_game()
        self.state = 'main_menu'

    def play(self):
        self.state = 'play'

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        """This method activates the main loop and switches the views.

        Typical usage example, when called from main method:
            self.game_state.run()
        """
        self.state = 'main_menu'

        while True:
            self.display.fill(self.background_color)
            event = pygame.event.poll()

            if event.type == pygame.QUIT:
                if self.state != 'main_menu':
                    self.quit_to_mainmenu()
                else:
                    self.quit_game()

            elif event.type == pygame.KEYDOWN and \
                    event.key == pygame.K_ESCAPE and \
                    self.state != 'main_menu':
                if self.game_manager.deal_active is not True:
                    self.quit_to_mainmenu()

            if self.state == 'main_menu':
                self.mainmenu_view.update(event)

            if self.state == 'confirm_new_game':
                self.confirm_new_game_view.update(event)

            if self.state == 'scoreboard':
                self.scoreboard_view.update(event)

            if self.state == 'play':
                if self.game_manager.double_active:
                    self.double_view.update(event)

                    if self.game_manager.bad_guess:
                        self.loose_view.update(event)

                    elif self.game_manager.player_win:
                        self.win_view.update(event)
                else:
                    if self.game_manager.gameover is not True:
                        self.play_view.update_cards()

                    if self.game_manager.gameover:
                        self.gameover_view.update(event)

                    elif self.game_manager.player_win:
                        self.win_view.update(event)

                    else:
                        self.play_view.update(event)

            if self.state == 'quit_to_mainmenu':
                self.confirm_quit_play.update(event)

            if self.state == 'payout':
                self.payout_view.update(event)

            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(60)

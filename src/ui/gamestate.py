import pygame

from ui.views.confirmation import Confirmation
from ui.views.mainmenu import Mainmenu
from ui.views.play import Play
from ui.views.scoreboard import Scoreboard
from ui.views.payout import Payout
from ui.views.double import Double
from ui.views.win import Win
from ui.views.prompt import Prompt

from entities.gamemanager import GameManager


class GameState():
    def __init__(self):

        self.state = 'main_menu'

        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()

        # Initialize game settings

        self.background_color = (235, 235, 235)

        # curr_display = pygame.display.Info()
        # self.display = pygame.display.set_mode(
        #    (curr_display.current_w, curr_display.current_h))

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

        self.gamemanager = GameManager()

        pygame.display.set_caption('Videopoker')

        # Initialize game view

        self.play_view = Play(self)

        # Initialize main menu view

        self.mainmenu_view = Mainmenu(self)

        # Initialize scoreboard view

        self.scoreboard_view = Scoreboard(self)

        # Initialize payout view

        self.payout_view = Payout(self)

        # Initialize double view
        self.double_view = Double(self)

        # Initialize bad double guess view
        self.loose_view = Prompt(
            'Wrong guess. Better luck next time!',
            self,
            self.gamemanager,
            self.play)

        # Initialize win view
        self.win_view = Win(self, self.gamemanager)

        # Initialize quit confirmation view
        self.confirm_quit_play = Confirmation(
            'Quit to mainmenu?',
            self.main_menu,
            self.play,
            self,
            self.font)

    def main_menu(self):
        self.state = 'main_menu'

    def scoreboard(self):
        self.state = 'scoreboard'

    def payout(self):
        self.state = 'payout'

    def continue_game(self):
        self.state = 'play'
        # TODO

    def new_game(self):
        self.state = 'play'
        # TODO

    def quit_to_mainmenu(self):
        self.state = 'quit_to_mainmenu'

    def play(self):
        self.state = 'play'

    def quit_game(self):
        pygame.quit()
        quit()

    def double(self):
        self.gamemanager.double()
        self.state = 'double_or_nothing'

    def claim(self):
        self.gamemanager.claim_win()
        self.state = 'play'

    def deal(self):
        self.gamemanager.deal()

    def run(self):
        self.state = 'main_menu'

        while True:
            if self.gamemanager.player_win is False:
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
                self.quit_to_mainmenu()

            if self.state == 'main_menu':
                self.mainmenu_view.update(event)

            if self.state == 'scoreboard':
                self.scoreboard_view.update(event)

            if self.state == 'play':
                self.play_view.update(event)

            if self.state == 'quit_to_mainmenu':
                self.confirm_quit_play.update(event)

            if self.state == 'double_or_nothing':
                self.double_view.update(event)
                if self.gamemanager.double_active is False:
                    self.loose_view.update(event)
                if self.gamemanager.player_win:
                    self.win_view.update(event)

            if self.state == 'payout':
                self.payout_view.update(event)

            if self.gamemanager.game_active and self.state == 'play':
                self.play_view.update_cards()

                if self.gamemanager.player_win:
                    self.win_view.update(event)
            else:
                self.gamemanager.game_active = False

            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(60)

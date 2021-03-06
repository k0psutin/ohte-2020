"""Module player_repository.py

       Handles saving and loading player data.
"""

import pickle
import os
import random
import string

from entities.player import Player


class PlayerRepository():
    """Creates an instance of Player Repository.

        Typical usage example:
        player_repository = PlayerRepository()
    """

    def __init__(self, save_data_name='save.dat',
                 highscore_data_name='highscores.dat'):
        """Constructor of the class.

        Args:

            save_data_name (str, optional): Defaults to 'save.dat'.
            highscore_data_name (str, optional): Defaults to 'highscores.dat'.
        """
        self.save_data_name = save_data_name
        self.highscore_data_name = highscore_data_name

        if os.path.isfile(self.save_data_name) is not True:
            save_data = {'credits': 0,
                         'best_double_streak': 0,
                         'best_double_win': 0,
                         'best_credits': 0}
            with open(self.save_data_name, 'wb') as file:
                pickle.dump(save_data, file, pickle.HIGHEST_PROTOCOL)

        if os.path.isfile(self.highscore_data_name) is not True:
            self.init_highscores()
        else:
            self.load_highscores()

    def save(self, player):
        """Saves player data to disk.

        Args:

            Player: The player object that will be saved to harddrive.
        """
        save_data = {'credits': player.credits,
                     'best_double_streak': player.best_double_streak,
                     'best_double_win': player.best_double_win,
                     'best_credits': player.best_credits}

        with open(self.save_data_name, 'wb') as file:
            pickle.dump(save_data, file, pickle.HIGHEST_PROTOCOL)

    def load(self) -> Player:
        """Fetch player data from disk.

        Returns:

            Player: Returns Player with loaded data.

        """
        save_data = None

        with open(self.save_data_name, 'rb') as file:
            save_data = pickle.load(file)

        player = Player()
        player.credits = save_data['credits']
        player.best_double_streak = save_data['best_double_streak']
        player.best_double_win = save_data['best_double_win']
        player.best_credits = save_data['best_credits']

        return player

    def has_savegame(self):
        """Checks that does savegame exist.

        Returns:

            bool: Returns True, if file exists. False otherwise.

        """
        save_data = None
        with open(self.save_data_name, 'rb') as file:
            save_data = pickle.load(file)
        return save_data['credits'] != 0

    def save_highscores(self):
        """Saves current highscore list to disk.

        Args:

            highscores (list): List of highscore entries.
        """
        with open(self.highscore_data_name, 'wb') as file:
            pickle.dump(self.highscores, file, pickle.HIGHEST_PROTOCOL)

    def load_highscores(self):
        """Fetch highscore data from disk.

        Returns:
            list: List of highscore entries.
        """
        with open(self.highscore_data_name, 'rb') as file:
            highscores = pickle.load(file)

        highscores = sorted(
            highscores, key=lambda i: i['best_credits'], reverse=False)

        self.highscores = highscores

    def init_highscores(self):
        """Generates basic entries for highscores.

        Returns:

            list: List containing 10 generated highscore entries.
        """
        highscores = []
        for i in range(1, 11):
            name = random.choice(string.ascii_uppercase)+random.choice(
                string.ascii_uppercase)+random.choice(string.ascii_uppercase)
            highscore_entry = {'name': name,
                               'best_credits': i*20,
                               'best_double_win': i*10,
                               'best_double_streak': i}
            highscores.append(highscore_entry)
        self.highscores = highscores
        self.save_highscores()

    def is_new_highscore(self, player):
        """Checks if best_credits amount if eligible for highscore.

        Args:

            Player: Current player object.

        Returns:

            bool: Returns True if eligible for highscore, False otherwise.
        """
        for score in self.highscores:
            if score['best_credits'] <= player.best_credits:
                return True

        return False

    def update_highscore(self, player, name):
        """Updates player best scores for highscore.

        Args:

            player (Player): Player-class object
            name (str): Initials for highscore list

        Typical usage example:

            update_highscore(player, 'AAA')
        """

        highscore_entry = {'name': name,
                           'best_credits': player.best_credits,
                           'best_double_win': player.best_double_win,
                           'best_double_streak': player.best_double_streak}

        updated_highscores = []
        highscores = sorted(
            self.highscores, key=lambda i: i['best_credits'], reverse=True)
        new_highscore = False
        for score in highscores:
            old_score = score['best_credits']
            current_score = highscore_entry['best_credits']
            if old_score <= current_score and new_highscore is False:
                new_highscore = True
                updated_highscores.append(highscore_entry)

            if len(updated_highscores) == 10:
                break
            updated_highscores.append(score)

        updated_highscores = sorted(
            updated_highscores, key=lambda i: i['best_credits'], reverse=False)
        self.highscores = updated_highscores
        self.save_highscores()

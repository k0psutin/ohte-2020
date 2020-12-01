"""Module player_repository.py

       Handles saving and loading player data.
"""

import pickle
import os


class PlayerRepository():
    """Creates an instance of Player Repository.

        Typical usage example:
        player_repository = PlayerRepository()
    """

    def __init__(self, save_data_name='save.dat'):
        """Constructor of the class

        Args:

            save-data-name (str, optional): Defaults to 'save.dat'.
        """
        self.save_data_name = save_data_name

    def save(self, save_data):
        with open(self.save_data_name, 'wb') as file:
            pickle.dump(save_data, file, pickle.HIGHEST_PROTOCOL)

    def load(self):
        if os.path.isfile(self.save_data_name) is not True:
            return None

        save_data = None

        with open(self.save_data_name, 'rb') as file:
            save_data = pickle.load(file)

        return save_data

    def is_save_empty(self):
        """Checks that does savegame exist

        Returns:

            bool: Returns True, if file exists. False otherwise.

        """
        if os.path.isfile(self.save_data_name) is not True:
            return False

        save_data = None
        with open(self.save_data_name, 'rb') as file:
            save_data = pickle.load(file)
        return save_data is not None

"""Module player_repository.py

       Handles saving and loading player data.
"""

import pickle
import os


class PlayerRepository():
    def __init__(self):
        pass

    def save(self, save_data):
        with open('save.dat', 'wb') as file:
            pickle.dump(save_data, file, pickle.HIGHEST_PROTOCOL)

    def load(self):
        if os.path.isfile('save.dat') is not True:
            return None

        with open('save.dat', 'rb') as file:
            save_data = pickle.load(file)

        return save_data

    def is_save_empty(self):
        if os.path.isfile('save.dat') is not True:
            return None

        save_data = None
        with open('save.dat', 'rb') as file:
            save_data = pickle.load(file)
        return save_data is not None

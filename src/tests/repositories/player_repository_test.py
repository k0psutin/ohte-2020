import unittest
import os
from repositories.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._player_repository = PlayerRepository('test.dat')

    def setUp(self):
        if os.path.isfile('test.dat'):
            os.remove('test.dat')

    @classmethod
    def tearDownClass(cls):
        if os.path.isfile('test.dat'):
            os.remove('test.dat')

    def test_is_save_empty_returns_false_if_file_not_present(self):
        self.assertFalse(self._player_repository.is_save_empty())

    def test_is_save_empty_returns_true_if_file_present(self):
        self._player_repository.save('Test')
        self.assertTrue(self._player_repository.is_save_empty())

    def test_load_returns_none_if_no_file_exists(self):
        test_load = self._player_repository.load()
        self.assertIs(test_load, None)

    def test_load_returns_none_if_file_exists_but_is_empty(self):
        self._player_repository.save(None)
        test_load = self._player_repository.load()
        self.assertIs(test_load, None)

    def test_load_returns_true_if_file_exists_and_is_not_empty(self):
        self._player_repository.save(True)
        test_load = self._player_repository.load()
        self.assertIs(test_load, True)

import unittest
import os
from repositories.player_repository import PlayerRepository
from entities.player import Player


class TestPlayerRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._player_repository = PlayerRepository(
            'test.dat', 'testhighscore.dat')

    def setUp(self):
        if os.path.isfile('test.dat'):
            os.remove('test.dat')
        if os.path.isfile('testhighscore.dat'):
            os.remove('testhighscore.dat')
        self.player = Player()
        self.player.player_repository = self._player_repository

    @classmethod
    def tearDownClass(cls):
        if os.path.isfile('test.dat'):
            os.remove('test.dat')
        if os.path.isfile('testhighscore.dat'):
            os.remove('testhighscore.dat')

    def test_is_save_empty_returns_true_if_file_present(self):
        self._player_repository.save('Test')
        self.assertTrue(self._player_repository.is_save_empty())

    def test_if_player_has_a_new_highscore_return_true(self):
        self.player.best_credits = 100
        self.assertTrue(self._player_repository.is_new_highscore(
            self.player.best_credits))

    def test_if_player_doesnt_have_a_new_highscore_return_false(self):
        self.player.best_credits = 10
        self.assertFalse(self._player_repository.is_new_highscore(
            self.player.best_credits))

    def test_submit_highscore_returns_correct_highscore(self):
        self.player.best_credits = 210
        self.player.submit_highscore('AAA')
        self.assertEqual(self._player_repository.highscores[9]['name'], 'AAA')

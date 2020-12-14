import unittest
import os
from repositories.player_repository import PlayerRepository
from entities.player import Player


class TestPlayerRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.player_repository = PlayerRepository(
            'test.dat', 'testhighscore.dat')

    def setUp(self):
        if os.path.isfile('test.dat'):
            os.remove('test.dat')
        if os.path.isfile('testhighscore.dat'):
            os.remove('testhighscore.dat')
        self.player = Player()

    @classmethod
    def tearDownClass(cls):
        if os.path.isfile('test.dat'):
            os.remove('test.dat')
        if os.path.isfile('testhighscore.dat'):
            os.remove('testhighscore.dat')

    def test_has_savegame_returns_false_if_player_has_no_credits(self):
        self.player.credits = 0
        self.player_repository.save(self.player)
        self.assertFalse(self.player_repository.has_savegame())

    def test_has_savegame_returns_true_if_player_has_credits(self):
        self.player.credits = 10
        self.player_repository.save(self.player)
        self.assertTrue(self.player_repository.has_savegame())

    def test_load_returns_correct_player(self):
        self.player_repository.save(self.player)
        test_player = {'credits': self.player.credits,
                       'best_double_streak': self.player.best_double_streak,
                       'best_double_win': self.player.best_double_win,
                       'best_credits': self.player.best_credits}
        test_load = self.player_repository.load()
        test_load_player = {'credits': test_load.credits,
                            'best_double_streak': test_load.best_double_streak,
                            'best_double_win': test_load.best_double_win,
                            'best_credits': test_load.best_credits}

        self.assertEqual(test_player, test_load_player)

    def test_if_player_has_a_new_highscore_return_true(self):
        self.player.best_credits = 100
        self.assertTrue(self.player_repository.is_new_highscore(
            self.player))

    def test_if_player_doesnt_have_a_new_highscore_return_false(self):
        self.player.best_credits = 10
        self.assertFalse(self.player_repository.is_new_highscore(
            self.player))

    def test_submit_highscore_returns_correct_highscore(self):
        self.player.best_credits = 210
        self.player_repository.update_highscore(self.player, 'AAA')
        self.assertEqual(self.player_repository.highscores[9]['name'], 'AAA')

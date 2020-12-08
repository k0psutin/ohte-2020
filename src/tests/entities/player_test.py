import unittest
import os

from entities.player import Player
from repositories.player_repository import PlayerRepository


class TestPlayer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.player_repository = PlayerRepository(
            'test.dat', 'testhighscore.dat')

    def setUp(self):
        self.player = Player()
        self.player.player_repository = self.player_repository

    @classmethod
    def tearDownClass(cls):
        if os.path.isfile('test.dat'):
            os.remove('test.dat')
        if os.path.isfile('testhighscore.dat'):
            os.remove('testhighscore.dat')

    def test_calling_constructor_creates_an_object(self):
        self.assertNotEqual(self.player, None)

    def test_new_player_credits_are_set_to_10(self):
        self.assertEqual(self.player.credits, 10)

    def test_new_player_best_double_streak_is_zero(self):
        self.assertEqual(self.player.best_double_streak, 0)

    def test_new_player_best_double_win_is_zero(self):
        self.assertEqual(self.player.best_double_win, 0)

    def test_new_player_best_credits_is_ten(self):
        self.assertEqual(self.player.best_credits, 10)

    def test_new_player_current_double_streak_is_zero(self):
        self.assertEqual(self.player.current_double_streak, 0)

    def test_add_credits_increases_credits(self):
        self.player.add_credits(100)
        self.assertEqual(self.player.credits, 110)

    def test_remove_credits_decreases_credits(self):
        self.player.remove_credits(5)
        self.assertEqual(self.player.credits, 5)

    def test_remove_credits_cant_make_credits_negative(self):
        self.player.remove_credits(11)
        self.assertEqual(self.player.credits, 0)

    def test_successful_double_increases_beast_streak(self):
        self.player.successful_double(True)
        self.player.double_win(0)
        self.assertEqual(self.player.best_double_streak, 1)

    def test_unsuccessful_double_resets_streak(self):
        self.player.successful_double(True)
        self.player.successful_double(False)
        self.assertEqual(self.player.best_double_streak, 0)

    def test_unsuccessful_double_saves_best_streak(self):
        for _ in range(0, 5):
            self.player.successful_double(True)

        self.player.double_win(0)

        self.assertEqual(self.player.best_double_streak, 5)

    def test_if_double_streak_is_lower_than_best_it_is_not_saved(self):
        for _ in range(0, 5):
            self.player.successful_double(True)

        self.player.double_win(0)

        for _ in range(0, 3):
            self.player.successful_double(True)

        self.player.double_win(0)

        self.assertEqual(self.player.best_double_streak, 5)

    def test_if_double_win_is_the_new_best_it_is_saved(self):
        self.player.best_double_win = 0
        self.player.double_win(10)
        self.assertEqual(self.player.best_double_win, 10)

    def test_player_save_returns_correct_data_when_loaded(self):
        self.player.save_player()
        test_load = self.player.load_player()
        self.assertEqual(self.player, test_load)

    def test_player_save_returns_none_if_player_saved_had_0_credits(self):
        self.player.credits = 0
        self.player.save_player()
        test_load = self.player.load_player()
        self.assertEqual(test_load, None)

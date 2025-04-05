from unittest import TestCase

from unittest.mock import patch

from game import game_intro


class TestGameIntro(TestCase):

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['s'])
    def test_game_intro_success_lower_s(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['S'])
    def test_game_intro_success_upper_s(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['start'])
    def test_game_intro_success_start(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['START'])
    def test_game_intro_success_START(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['StArT'])
    def test_game_intro_success_StArT(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['s s', 'start'])
    def test_game_intro_two_lower_s_then_start(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['ss', 'start'])
    def test_game_intro_two_lower_s_combined_then_start(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['start start', 'start'])
    def test_game_intro_two_start_then_start(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['starts', 'start'])
    def test_game_intro_misspell_starts_then_start(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['strat', 'start'])
    def test_game_intro_misspell_strat_then_start(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['star', 'start'])
    def test_game_intro_misspell_star_then_start(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['sta rt', 'start'])
    def test_game_intro_space_in_start_then_start(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['123', 'start'])
    def test_game_intro_invalid_integer_then_start(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['hello', 'start'])
    def test_game_intro_invalid_string_then_start(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['3.14', 'start'])
    def test_game_intro_invalid_float_then_start(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['!#$', 'start'])
    def test_game_intro_invalid_symbols_then_start(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['', 'start'])
    def test_game_intro_empty_input_then_start(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

    @patch('game.clear_screen')
    @patch('time.sleep', return_value=0)
    @patch('builtins.input', side_effect=['   ', 'start'])
    def test_game_intro_space_input_then_start(self, _, __, ___):
        result = game_intro()
        self.assertEqual(result, True)

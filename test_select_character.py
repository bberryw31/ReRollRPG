from unittest import TestCase

from unittest.mock import patch

import io

from game import select_character


class TestSelectCharacterInvalidInputOutput(TestCase):

    @patch('builtins.input', side_effect=["1"])
    @patch('game.clear_screen')
    @patch('game.random_character')
    def test_select_character_confirm(self, mock_random_character, _, __):
        result = select_character(["Boxer", "Chef", "Hunter"], 0)
        expected = mock_random_character()
        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=["2", "1"])
    @patch('game.clear_screen')
    @patch('game.random_character')
    def test_select_character_roll_once_then_confirm(self, mock_random_character, _, __):
        result = select_character(["Boxer", "Chef", "Hunter"], 0)
        expected = mock_random_character()
        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=["2", "2", "1"])
    @patch('game.clear_screen')
    @patch('game.random_character')
    def test_select_character_roll_twice_then_confirm(self, mock_random_character, _, __):
        result = select_character(["Boxer", "Chef", "Hunter"], 0)
        expected = mock_random_character()
        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=["2", "2", "2", "2", "2", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.clear_screen')
    @patch('game.random_character')
    def test_select_character_roll_five_times_then_confirm(self, mock_random_character, _, mock_stdout, __):
        class_pool = ["Boxer", "Chef", "Hunter"]
        result = select_character(class_pool, 0)
        expected = mock_random_character()
        output = mock_stdout.getvalue()
        self.assertIn("Unlocked Class: \033[0m\033[91m\033[1mGambler", output)
        self.assertIn("Gambler", class_pool)
        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.clear_screen')
    @patch('game.random_character')
    def test_select_character_restart_count_2(self, mock_random_character, _, mock_stdout, __):
        class_pool = ["Boxer", "Chef", "Hunter"]
        result = select_character(class_pool, 2)
        expected = mock_random_character()
        output = mock_stdout.getvalue()
        self.assertIn("Unlocked Class: \033[0m\033[91m\033[1mJimmy Jimster the legendary adventurer", output)
        self.assertIn("Jimmy", class_pool)
        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=["a", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.clear_screen')
    @patch('game.random_character')
    def test_select_character_invalid_input_string_then_confirm(self, mock_random_character, _, mock_stdout, __):
        result = select_character(["Boxer", "Chef", "Hunter"], 0)
        expected = mock_random_character()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input.", output)
        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=[" ", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.clear_screen')
    @patch('game.random_character')
    def test_select_character_invalid_input_space_then_confirm(self, mock_random_character, _, mock_stdout, __):
        result = select_character(["Boxer", "Chef", "Hunter"], 0)
        expected = mock_random_character()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input.", output)
        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=["3", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.clear_screen')
    @patch('game.random_character')
    def test_select_character_invalid_integer_then_confirm(self, mock_random_character, _, mock_stdout, __):
        result = select_character(["Boxer", "Chef", "Hunter"], 0)
        expected = mock_random_character()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input.", output)
        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=["", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.clear_screen')
    @patch('game.random_character')
    def test_select_character_invalid_input_empty_then_confirm(self, mock_random_character, _, mock_stdout, __):
        result = select_character(["Boxer", "Chef", "Hunter"], 0)
        expected = mock_random_character()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input.", output)
        self.assertEqual(result, expected)
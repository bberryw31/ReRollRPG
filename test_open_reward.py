from unittest import TestCase

from unittest.mock import patch

import io

from game import open_reward


class TestOpenReward(TestCase):

    @patch("builtins.input", side_effect=["n"])
    def test_open_reward_decline_with_string(self, _):
        character = {
            "HP": 5,
            "max_HP": 10,
            "roll": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        self.assertEqual(open_reward(character), False)

    @patch("builtins.input", side_effect=["1"])
    def test_open_reward_decline_with_integer(self, _):
        character = {
            "HP": 5,
            "max_HP": 10,
            "roll": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        self.assertEqual(open_reward(character), False)

    @patch("builtins.input", side_effect=[" "])
    def test_open_reward_decline_with_space(self, _):
        character = {
            "HP": 5,
            "max_HP": 10,
            "roll": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        self.assertEqual(open_reward(character), False)

    @patch("builtins.input", side_effect=[""])
    def test_open_reward_decline_with_empty(self, _):
        character = {
            "HP": 5,
            "max_HP": 10,
            "roll": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        self.assertEqual(open_reward(character), False)

    @patch("builtins.input", side_effect=["y", "1"])
    @patch("time.sleep")
    def test_open_reward_open_confirm_option_1(self, _, __):
        character_default = {
            "HP": 5,
            "max_HP": 10,
            "roll": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        character = {
            "HP": 5,
            "max_HP": 10,
            "roll": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        open_reward(character)
        self.assertNotEqual(character, character_default)

    @patch("builtins.input", side_effect=["y", "2"])
    @patch("time.sleep")
    def test_open_reward_open_confirm_option_2(self, _, __):
        character_default = {
            "HP": 5,
            "max_HP": 10,
            "roll": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        character = {
            "HP": 5,
            "max_HP": 10,
            "roll": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        open_reward(character)
        self.assertNotEqual(character, character_default)

    @patch("builtins.input", side_effect=["y", "r", "2"])
    @patch("time.sleep")
    def test_open_reward_open_roll_once_then_confirm_option_1(self, _, __):
        character_default = {
            "HP": 5,
            "max_HP": 10,
            "roll": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        character = {
            "HP": 5,
            "max_HP": 10,
            "roll": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        open_reward(character)
        self.assertEqual(character["roll"], character_default["roll"] - 1)
        character.pop("roll")
        character_default.pop("roll")
        self.assertNotEqual(character, character_default)

    @patch("builtins.input", side_effect=["y", "r", "2"])
    @patch("time.sleep")
    def test_open_reward_open_roll_once_then_confirm_option_2(self, _, __):
        character_default = {
            "HP": 5,
            "max_HP": 10,
            "roll": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        character = {
            "HP": 5,
            "max_HP": 10,
            "roll": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        open_reward(character)
        self.assertEqual(character["roll"], character_default["roll"] - 1)
        character.pop("roll")
        character_default.pop("roll")
        self.assertNotEqual(character, character_default)

    @patch("builtins.input", side_effect=["y", "r", "r", "1"])
    @patch("time.sleep")
    def test_open_reward_open_roll_twice_then_confirm(self, _, __):
        character_default = {
            "HP": 5,
            "max_HP": 10,
            "roll": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        character = {
            "HP": 5,
            "max_HP": 10,
            "roll": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        open_reward(character)
        self.assertEqual(character["roll"], character_default["roll"] - 2)
        character.pop("roll")
        character_default.pop("roll")
        self.assertNotEqual(character, character_default)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["y", "r", "1"])
    @patch("time.sleep")
    def test_open_reward_open_out_of_roll_then_confirm(self, _, __, mock_stdout):
        character_default = {
            "HP": 5,
            "max_HP": 10,
            "roll": 0,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        character = {
            "HP": 5,
            "max_HP": 10,
            "roll": 0,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        open_reward(character)
        output = mock_stdout.getvalue()
        self.assertEqual(character["roll"], 0)
        self.assertIn("You are out of re-rolls!", output)
        self.assertNotEqual(character, character_default)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["y", "r", "r", "1"])
    @patch("time.sleep")
    def test_open_reward_open_roll_once_out_of_roll_then_confirm(self, _, __, mock_stdout):
        character_default = {
            "HP": 5,
            "max_HP": 10,
            "roll": 1,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        character = {
            "HP": 5,
            "max_HP": 10,
            "roll": 1,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        open_reward(character)
        output = mock_stdout.getvalue()
        self.assertEqual(character["roll"], 0)
        self.assertIn("You are out of re-rolls!", output)
        self.assertNotEqual(character, character_default)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["y", "3", "1"])
    @patch("time.sleep")
    def test_open_reward_open_invalid_integer_input_then_confirm(self, _, __, mock_stdout):
        character_default = {
            "HP": 5,
            "max_HP": 10,
            "roll": 1,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        character = {
            "HP": 5,
            "max_HP": 10,
            "roll": 1,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        open_reward(character)
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input.", output)
        self.assertNotEqual(character, character_default)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["y", "n", "1"])
    @patch("time.sleep")
    def test_open_reward_open_invalid_string_input_then_confirm(self, _, __, mock_stdout):
        character_default = {
            "HP": 5,
            "max_HP": 10,
            "roll": 1,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        character = {
            "HP": 5,
            "max_HP": 10,
            "roll": 1,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        open_reward(character)
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input.", output)
        self.assertNotEqual(character, character_default)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["y", " ", "1"])
    @patch("time.sleep")
    def test_open_reward_open_invalid_space_input_then_confirm(self, _, __, mock_stdout):
        character_default = {
            "HP": 5,
            "max_HP": 10,
            "roll": 1,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        character = {
            "HP": 5,
            "max_HP": 10,
            "roll": 1,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        open_reward(character)
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input.", output)
        self.assertNotEqual(character, character_default)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["y", "", "1"])
    @patch("time.sleep")
    def test_open_reward_open_invalid_empty_input_then_confirm(self, _, __, mock_stdout):
        character_default = {
            "HP": 5,
            "max_HP": 10,
            "roll": 1,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        character = {
            "HP": 5,
            "max_HP": 10,
            "roll": 1,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}
        }
        open_reward(character)
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input.", output)
        self.assertNotEqual(character, character_default)
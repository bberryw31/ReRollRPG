from unittest import TestCase

from unittest.mock import patch

from game import fight_enemy

class TestFightEnemy(TestCase):

    @patch("builtins.input", side_effect=["n"])
    def test_fight_enemy_decline_with_invalid_string(self, _):
        character = {
            "HP": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1},
            "class": {"main_stats": ["STR"], "icon": "🦾 "},
            "roll": 0
        }
        result = fight_enemy("🐜 ", character, 1)
        self.assertFalse(result)

    @patch("builtins.input", side_effect=["hello"])
    def test_fight_enemy_decline_with_invalid_string_long(self, _):
        character = {
            "HP": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1},
            "class": {"main_stats": ["STR"], "icon": "🦾 "},
            "roll": 0
        }
        result = fight_enemy("🐜 ", character, 1)
        self.assertFalse(result)

    @patch("builtins.input", side_effect=["1"])
    def test_fight_enemy_decline_with_invalid_integer(self, _):
        character = {
            "HP": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1},
            "class": {"main_stats": ["STR"], "icon": "🦾 "},
            "roll": 0
        }
        result = fight_enemy("🐜 ", character, 1)
        self.assertFalse(result)

    @patch("builtins.input", side_effect=[" "])
    def test_fight_enemy_decline_with_invalid_space(self, _):
        character = {
            "HP": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1},
            "class": {"main_stats": ["STR"], "icon": "🦾 "},
            "roll": 0
        }
        result = fight_enemy("🐜 ", character, 1)
        self.assertFalse(result)

    @patch("builtins.input", side_effect=[""])
    def test_fight_enemy_decline_with_invalid_empty(self, _):
        character = {
            "HP": 10,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1},
            "class": {"main_stats": ["STR"], "icon": "🦾 "},
            "roll": 0
        }
        result = fight_enemy("🐜 ", character, 1)
        self.assertFalse(result)

    @patch("builtins.input", side_effect=["y"])
    @patch("time.sleep")
    def test_fight_enemy_accept_and_dead(self, _, __):
        character = {
            "HP": 1,
            "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1},
            "class": {"main_stats": ["STR"], "icon": "🦾 "},
            "roll": 0
        }
        result = fight_enemy("💀 ", character, 4)
        self.assertFalse(result)

    @patch("builtins.input", side_effect=["y"])
    @patch("time.sleep")
    def test_fight_enemy_accept_and_win(self, _, __):
        character = {
            "HP": 99,
            "stats": {"str": 99, "dex": 99, "int": 1, "luc": 99},
            "class": {"main_stats": ["STR", "DEX", "LUC"], "icon": "🦾 "},
            "roll": 0
        }
        result = fight_enemy("🐜 ", character, 1)
        self.assertTrue(result)

    @patch("builtins.input", side_effect=["y"])
    @patch("time.sleep")
    def test_fight_enemy_accept_gain_inspiration_and_win(self, _, __):
        character = {
            "HP": 99,
            "stats": {"str": 1, "dex": 1, "int": 99, "luc": 1},
            "class": {"main_stats": ["STR"], "icon": "🦾 "},
            "roll": 0
        }
        result = fight_enemy("🐜 ", character, 1)
        self.assertTrue(character["roll"] > 0)
        self.assertTrue(result)
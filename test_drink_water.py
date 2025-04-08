from unittest import TestCase

from unittest.mock import patch

from game import drink_water

class TestDrinkWater(TestCase):

    @patch("builtins.input", return_value="n")
    def test_drink_water_decline_with_string(self, _):
        character = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        drink_water(character)
        character_expected = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        self.assertEqual(character, character_expected)

    @patch("builtins.input", return_value="1")
    def test_drink_water_decline_with_integer(self, _):
        character = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        drink_water(character)
        character_expected = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        self.assertEqual(character, character_expected)

    @patch("builtins.input", return_value=" ")
    def test_drink_water_decline_with_space(self, _):
        character = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        drink_water(character)
        character_expected = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        self.assertEqual(character, character_expected)

    @patch("builtins.input", return_value="")
    def test_drink_water_decline_with_empty(self, _):
        character = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        drink_water(character)
        character_expected = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        self.assertEqual(character, character_expected)

    @patch("builtins.input", return_value="n")
    def test_drink_water_decline(self, mock_input):
        character = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        drink_water(character)
        self.assertEqual(character["HP"], 5)
        self.assertEqual(character["stats"]["str"], 1)

    @patch("random.choice", return_value="str")
    @patch("random.randint", side_effect=[10, 1])
    @patch("builtins.input", return_value="y")
    @patch("time.sleep")
    def test_drink_water_stat_gain_str_1(self, _, __, ___, ____):
        character = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        drink_water(character)
        self.assertEqual(character["stats"]["str"], 2)

    @patch("random.choice", return_value="str")
    @patch("random.randint", side_effect=[10, 2])
    @patch("builtins.input", return_value="y")
    @patch("time.sleep")
    def test_drink_water_stat_gain_str_2(self, _, __, ___, ____):
        character = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        drink_water(character)
        self.assertEqual(character["stats"]["str"], 3)

    @patch("random.choice", return_value="dex")
    @patch("random.randint", side_effect=[10, 1])
    @patch("builtins.input", return_value="y")
    @patch("time.sleep")
    def test_drink_water_stat_gain_dex(self, _, __, ___, ____):
        character = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        drink_water(character)
        self.assertEqual(character["stats"]["dex"], 2)

    @patch("random.choice", return_value="int")
    @patch("random.randint", side_effect=[10, 1])
    @patch("builtins.input", return_value="y")
    @patch("time.sleep")
    def test_drink_water_stat_gain_int(self, _, __, ___, ____):
        character = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        drink_water(character)
        self.assertEqual(character["stats"]["int"], 2)

    @patch("random.choice", return_value="luc")
    @patch("random.randint", side_effect=[10, 1])
    @patch("builtins.input", return_value="y")
    @patch("time.sleep")
    def test_drink_water_stat_gain_luc(self, _, __, ___, ____):
        character = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        drink_water(character)
        self.assertEqual(character["stats"]["luc"], 2)

    @patch("random.randint", side_effect=[30, 1])
    @patch("builtins.input", return_value="y")
    @patch("time.sleep")
    def test_drink_water_heal_hp_1(self, mock_sleep, mock_randint, mock_input):
        character = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        drink_water(character)
        self.assertEqual(character["HP"], 6)

    @patch("random.randint", side_effect=[30, 2])
    @patch("builtins.input", return_value="y")
    @patch("time.sleep")
    def test_drink_water_heal_hp_2(self, mock_sleep, mock_randint, mock_input):
        character = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        drink_water(character)
        self.assertEqual(character["HP"], 7)

    @patch("random.randint", return_value=99)
    @patch("builtins.input", return_value="y")
    @patch("time.sleep")
    def test_drink_water_poison(self, _, __, ___):
        character = {"HP": 5, "max_HP": 10, "stats": {"str": 1, "dex": 1, "int": 1, "luc": 1}}
        drink_water(character)
        self.assertEqual(character["HP"], 4)
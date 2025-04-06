from unittest import TestCase

from game import random_character


class TestRandomCharacter(TestCase):

    def test_random_character_class_pool_1(self):
        character = random_character(["Boxer"])
        self.assertIn(character["class"]["class_name"], ["Boxer"])

    def test_random_character_class_pool_2(self):
        character = random_character(["Boxer", "Chef"])
        self.assertIn(character["class"]["class_name"], ["Boxer", "Chef"])

    def test_random_character_class_pool_3(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertIn(character["class"]["class_name"], ["Boxer", "Chef", "Hunter"])

    def test_random_character_has_hp(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertIn("HP", character)

    def test_random_character_hp_is_integer(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertIsInstance(character["HP"], int)

    def test_random_character_hp_is_in_range(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertTrue(5 <= character["HP"] <= 10)

    def test_random_character_has_max_hp(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertIn("max_HP", character)

    def test_random_character_has_stats(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertIn("stats", character)

    def test_random_character_has_stat_str(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertIn("str", character["stats"])

    def test_random_character_has_stat_dex(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertIn("dex", character["stats"])

    def test_random_character_has_stat_int(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertIn("int", character["stats"])

    def test_random_character_has_stat_luc(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertIn("luc", character["stats"])

    def test_random_character_stat_str_is_int(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertIsInstance(character["stats"]["str"], int)

    def test_random_character_stat_dex_is_int(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertIsInstance(character["stats"]["dex"], int)

    def test_random_character_stat_int_is_int(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertIsInstance(character["stats"]["int"], int)

    def test_random_character_stat_luc_is_int(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertIsInstance(character["stats"]["luc"], int)

    def test_random_character_has_roll(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertIn("roll", character)

    def test_random_character_roll_is_int(self):
        character = random_character(["Boxer", "Chef", "Hunter"])
        self.assertIsInstance(character["roll"], int)

    def test_random_character_gambler_roll_is_13(self):
        character = random_character(["Gambler"])
        self.assertEqual(character["roll"], 13)
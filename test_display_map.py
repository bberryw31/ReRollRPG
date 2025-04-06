from unittest import TestCase

from unittest.mock import patch

import io

from game import display_map


class TestDisplayMap(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_map_stage_0(self, mock_stdout):
        room = [[".  "] * 17 for _ in range(10)]
        character = {
            "coordinates": (5, 5),
            "class": {"icon": "🎮 "},
            "HP": 6,
            "max_HP": 7,
            "roll": 8,
            "stats": {"str": 5, "dex": 6, "int": 7, "luc": 8}
        }
        stage = 0
        display_map(room, character, stage)
        output = mock_stdout.getvalue()
        self.assertIn("🌑 Starting Room", output)
        self.assertIn("🎮 ", output)
        self.assertIn("CHARACTER INFO", output)
        self.assertIn("HP", output)
        self.assertIn("🎲", output)
        self.assertIn("STR", output)
        self.assertIn("DEX", output)
        self.assertIn("INT", output)
        self.assertIn("LUC", output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_map_stage_1(self, mock_stdout):
        room = [[".  "] * 17 for _ in range(10)]
        character = {
            "coordinates": (5, 5),
            "class": {"icon": "🎮 "},
            "HP": 6,
            "max_HP": 7,
            "roll": 8,
            "stats": {"str": 5, "dex": 6, "int": 7, "luc": 8}
        }
        stage = 1
        display_map(room, character, stage)
        output = mock_stdout.getvalue()
        self.assertIn("🌘 Dungeon Stage", output)
        self.assertIn("🎮 ", output)
        self.assertIn("CHARACTER INFO", output)
        self.assertIn("HP", output)
        self.assertIn("🎲", output)
        self.assertIn("STR", output)
        self.assertIn("DEX", output)
        self.assertIn("INT", output)
        self.assertIn("LUC", output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_map_stage_2(self, mock_stdout):
        room = [[".  "] * 17 for _ in range(10)]
        character = {
            "coordinates": (5, 5),
            "class": {"icon": "🎮 "},
            "HP": 6,
            "max_HP": 7,
            "roll": 8,
            "stats": {"str": 5, "dex": 6, "int": 7, "luc": 8}
        }
        stage = 2
        display_map(room, character, stage)
        output = mock_stdout.getvalue()
        self.assertIn("🌗 Dungeon Stage", output)
        self.assertIn("🎮 ", output)
        self.assertIn("CHARACTER INFO", output)
        self.assertIn("HP", output)
        self.assertIn("🎲", output)
        self.assertIn("STR", output)
        self.assertIn("DEX", output)
        self.assertIn("INT", output)
        self.assertIn("LUC", output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_map_stage_3(self, mock_stdout):
        room = [[".  "] * 17 for _ in range(10)]
        character = {
            "coordinates": (5, 5),
            "class": {"icon": "🎮 "},
            "HP": 6,
            "max_HP": 7,
            "roll": 8,
            "stats": {"str": 5, "dex": 6, "int": 7, "luc": 8}
        }
        stage = 3
        display_map(room, character, stage)
        output = mock_stdout.getvalue()
        self.assertIn("🌖 Dungeon Stage", output)
        self.assertIn("🎮 ", output)
        self.assertIn("CHARACTER INFO", output)
        self.assertIn("HP", output)
        self.assertIn("🎲", output)
        self.assertIn("STR", output)
        self.assertIn("DEX", output)
        self.assertIn("INT", output)
        self.assertIn("LUC", output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_map_stage_4(self, mock_stdout):
        room = [[".  "] * 17 for _ in range(10)]
        character = {
            "coordinates": (5, 5),
            "class": {"icon": "🎮 "},
            "HP": 6,
            "max_HP": 7,
            "roll": 8,
            "stats": {"str": 5, "dex": 6, "int": 7, "luc": 8}
        }
        stage = 4
        display_map(room, character, stage)
        output = mock_stdout.getvalue()
        self.assertIn("🌕 Dungeon Boss Room", output)
        self.assertIn("🎮 ", output)
        self.assertIn("CHARACTER INFO", output)
        self.assertIn("HP", output)
        self.assertIn("🎲", output)
        self.assertIn("STR", output)
        self.assertIn("DEX", output)
        self.assertIn("INT", output)
        self.assertIn("LUC", output)


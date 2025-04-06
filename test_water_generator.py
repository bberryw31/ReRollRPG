from unittest import TestCase

from unittest.mock import patch

from game import water_generator


class TestWaterGenerator(TestCase):

    @patch('random.choice', side_effect=[(3, 3)])
    def test_water_generator_zone_left_top_left_corner(self, mock_choice):
        water_center_zone = [(row, col) for row in range(3, 7) for col in range(3, 6)]
        water_zone = [(row, col) for row in range(2, 8) for col in range(2, 7)]
        room = [[".  "] * 17 for _ in range(10)]
        water_generator(water_center_zone, room)
        self.assertEqual(room[3][3], "🌀 ")
        water_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] == "🌀 "]
        for water in water_spots:
            self.assertIn(water, water_zone)

    @patch('random.choice', side_effect=[(3, 5)])
    def test_water_generator_zone_left_top_right_corner(self, mock_choice):
        water_center_zone = [(row, col) for row in range(3, 7) for col in range(3, 6)]
        water_zone = [(row, col) for row in range(2, 8) for col in range(2, 7)]
        room = [[".  "] * 17 for _ in range(10)]
        water_generator(water_center_zone, room)
        self.assertEqual(room[3][5], "🌀 ")
        water_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] == "🌀 "]
        for water in water_spots:
            self.assertIn(water, water_zone)

    @patch('random.choice', side_effect=[(6, 3)])
    def test_water_generator_zone_left_bottom_left_corner(self, mock_choice):
        water_center_zone = [(row, col) for row in range(3, 7) for col in range(3, 6)]
        water_zone = [(row, col) for row in range(2, 8) for col in range(2, 7)]
        room = [[".  "] * 17 for _ in range(10)]
        water_generator(water_center_zone, room)
        self.assertEqual(room[6][3], "🌀 ")
        water_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] == "🌀 "]
        for water in water_spots:
            self.assertIn(water, water_zone)

    @patch('random.choice', side_effect=[(6, 5)])
    def test_water_generator_zone_left_bottom_right_corner(self, mock_choice):
        water_center_zone = [(row, col) for row in range(3, 7) for col in range(3, 6)]
        water_zone = [(row, col) for row in range(2, 8) for col in range(2, 7)]
        room = [[".  "] * 17 for _ in range(10)]
        water_generator(water_center_zone, room)
        self.assertEqual(room[6][5], "🌀 ")
        water_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] == "🌀 "]
        for water in water_spots:
            self.assertIn(water, water_zone)

    @patch('random.choice', side_effect=[(4, 4)])
    def test_water_generator_zone_left_center(self, mock_choice):
        water_center_zone = [(row, col) for row in range(3, 7) for col in range(3, 6)]
        water_zone = [(row, col) for row in range(2, 8) for col in range(2, 7)]
        room = [[".  "] * 17 for _ in range(10)]
        water_generator(water_center_zone, room)
        self.assertEqual(room[4][4], "🌀 ")
        water_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] == "🌀 "]
        for water in water_spots:
            self.assertIn(water, water_zone)

    @patch('random.choice', side_effect=[(3, 11)])
    def test_water_generator_zone_right_top_left_corner(self, mock_choice):
        water_center_zone = [(row, col) for row in range(3, 7) for col in range(11, 14)]
        water_zone = [(row, col) for row in range(2, 8) for col in range(10, 15)]
        room = [[".  "] * 17 for _ in range(10)]
        water_generator(water_center_zone, room)
        self.assertEqual(room[3][11], "🌀 ")
        water_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] == "🌀 "]
        for water in water_spots:
            self.assertIn(water, water_zone)

    @patch('random.choice', side_effect=[(3, 13)])
    def test_water_generator_zone_right_top_right_corner(self, mock_choice):
        water_center_zone = [(row, col) for row in range(3, 7) for col in range(11, 14)]
        water_zone = [(row, col) for row in range(2, 8) for col in range(10, 15)]
        room = [[".  "] * 17 for _ in range(10)]
        water_generator(water_center_zone, room)
        self.assertEqual(room[3][13], "🌀 ")
        water_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] == "🌀 "]
        for water in water_spots:
            self.assertIn(water, water_zone)

    @patch('random.choice', side_effect=[(6, 11)])
    def test_water_generator_zone_right_bottom_left_corner(self, mock_choice):
        water_center_zone = [(row, col) for row in range(3, 7) for col in range(11, 14)]
        water_zone = [(row, col) for row in range(2, 8) for col in range(10, 15)]
        room = [[".  "] * 17 for _ in range(10)]
        water_generator(water_center_zone, room)
        self.assertEqual(room[6][11], "🌀 ")
        water_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] == "🌀 "]
        for water in water_spots:
            self.assertIn(water, water_zone)

    @patch('random.choice', side_effect=[(6, 13)])
    def test_water_generator_zone_right_bottom_right_corner(self, mock_choice):
        water_center_zone = [(row, col) for row in range(3, 7) for col in range(11, 14)]
        water_zone = [(row, col) for row in range(2, 8) for col in range(10, 15)]
        room = [[".  "] * 17 for _ in range(10)]
        water_generator(water_center_zone, room)
        self.assertEqual(room[6][13], "🌀 ")
        water_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] == "🌀 "]
        for water in water_spots:
            self.assertIn(water, water_zone)

    @patch('random.choice', side_effect=[(4, 12)])
    def test_water_generator_zone_right_center(self, mock_choice):
        water_center_zone = [(row, col) for row in range(3, 7) for col in range(11, 14)]
        water_zone = [(row, col) for row in range(2, 8) for col in range(10, 15)]
        room = [[".  "] * 17 for _ in range(10)]
        water_generator(water_center_zone, room)
        self.assertEqual(room[4][12], "🌀 ")
        water_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] == "🌀 "]
        for water in water_spots:
            self.assertIn(water, water_zone)
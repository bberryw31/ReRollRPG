from unittest import TestCase

from game import generate_map


class TestGenerateMap(TestCase):

    def test_generate_map_stage_0_size(self):
        room = generate_map(0)
        self.assertEqual(len(room), 10)
        for row in room:
            self.assertEqual(len(row), 17)

    def test_generate_map_stage_1_size(self):
        room = generate_map(1)
        self.assertEqual(len(room), 10)
        for row in room:
            self.assertEqual(len(row), 17)

    def test_generate_map_stage_2_size(self):
        room = generate_map(2)
        self.assertEqual(len(room), 10)
        for row in room:
            self.assertEqual(len(row), 17)

    def test_generate_map_stage_3_size(self):
        room = generate_map(3)
        self.assertEqual(len(room), 10)
        for row in room:
            self.assertEqual(len(row), 17)

    def test_generate_map_stage_4_size(self):
        room = generate_map(4)
        self.assertEqual(len(room), 10)
        for row in room:
            self.assertEqual(len(row), 17)

    def test_generate_map_stage_0_door_location(self):
        room = generate_map(0)
        self.assertEqual(room[0][8], "🚪 ")
        self.assertEqual(room[9][8], "🔒 ")

    def test_generate_map_stage_1_door_location(self):
        room = generate_map(1)
        self.assertEqual(room[0][8], "🚪 ")
        self.assertEqual(room[9][8], "🔒 ")

    def test_generate_map_stage_2_door_location(self):
        room = generate_map(2)
        self.assertEqual(room[0][8], "🚪 ")
        self.assertEqual(room[9][8], "🔒 ")

    def test_generate_map_stage_3_door_location(self):
        room = generate_map(3)
        self.assertEqual(room[0][8], "🚪 ")
        self.assertEqual(room[9][8], "🔒 ")

    def test_generate_map_stage_4_door_location(self):
        room = generate_map(4)
        self.assertEqual(room[0][8], "🚪 ")
        self.assertEqual(room[9][8], "🔒 ")

    def test_generate_map_stage_0_tutorial_reward(self):
        room = generate_map(0)
        self.assertEqual(room[3][8], "🎁 ")

    def test_generate_map_stage_0_tutorial(self):
        room = generate_map(0)
        tutorial = {
            (4, 4): "\033[1m\033[33mW  \033[0m",
            (5, 3): "\033[1m\033[33mA  \033[0m",
            (5, 4): "\033[1m\033[33mS  \033[0m",
            (5, 5): "\033[1m\033[33mD  \033[0m",
            (3, 4): "⬆️ ",
            (5, 2): "⬅️ ",
            (6, 4): "⬇️ ",
            (5, 6): "➡️ ",
            (4, 11): "\033[1m\033[33mQ  \033[0m",
            (4, 12): "  Q",
            (4, 13): "UIT",
            (4, 14): "   "
        }
        for (row, col), expected in tutorial.items():
            self.assertEqual(room[row][col], expected)

    def test_generate_map_stage_1_rewards(self):
        reward_spots = [(1, 1), (1, 15), (8, 1), (8, 15)]
        room = generate_map(1)
        rewards = [(row, col) for row in range(10) for col in range(17) if room[row][col] == "🎁 "]
        reward_count = len(rewards)
        self.assertEqual(reward_count, 1)
        for reward in rewards:
            self.assertIn(reward, reward_spots)

    def test_generate_map_stage_2_rewards(self):
        reward_spots = [(1, 1), (1, 15), (8, 1), (8, 15)]
        room = generate_map(2)
        rewards = [(row, col) for row in range(10) for col in range(17) if room[row][col] == "🎁 "]
        reward_count = len(rewards)
        self.assertEqual(reward_count, 2)
        for reward in rewards:
            self.assertIn(reward, reward_spots)

    def test_generate_map_stage_3_rewards(self):
        reward_spots = [(1, 1), (1, 15), (8, 1), (8, 15)]
        room = generate_map(3)
        rewards = [(row, col) for row in range(10) for col in range(17) if room[row][col] == "🎁 "]
        reward_count = len(rewards)
        self.assertEqual(reward_count, 3)
        for reward in rewards:
            self.assertIn(reward, reward_spots)

    def test_generate_map_stage_1_enemies(self):
        enemy_zone = ([(row, col) for row in range(3, 7) for col in range(3, 6)] +
                      [(row, col) for row in range(3, 7) for col in range(11, 14)])
        room = generate_map(1)
        enemies = ["🐜 ", "🦇 ", "🦖 ", "🐊 ", "🦄 ", "🐍 ", "🦂 ", "🐌 ", "🦟 "]
        enemy_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] in enemies]
        enemy_count = len(enemy_spots)
        self.assertEqual(enemy_count, 2)
        for enemy in enemy_spots:
            self.assertIn(enemy, enemy_zone)

    def test_generate_map_stage_2_enemies(self):
        enemy_zone = ([(row, col) for row in range(3, 7) for col in range(3, 6)] +
                      [(row, col) for row in range(3, 7) for col in range(11, 14)])
        room = generate_map(2)
        enemies = ["🐜 ", "🦇 ", "🦖 ", "🐊 ", "🦄 ", "🐍 ", "🦂 ", "🐌 ", "🦟 "]
        enemy_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] in enemies]
        enemy_count = len(enemy_spots)
        self.assertEqual(enemy_count, 3)
        for enemy in enemy_spots:
            self.assertIn(enemy, enemy_zone)

    def test_generate_map_stage_3_enemies(self):
        enemy_zone = ([(row, col) for row in range(3, 7) for col in range(3, 6)] +
                      [(row, col) for row in range(3, 7) for col in range(11, 14)])
        room = generate_map(3)
        enemies = ["🐜 ", "🦇 ", "🦖 ", "🐊 ", "🦄 ", "🐍 ", "🦂 ", "🐌 ", "🦟 "]
        enemy_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] in enemies]
        enemy_count = len(enemy_spots)
        self.assertEqual(enemy_count, 4)
        for enemy in enemy_spots:
            self.assertIn(enemy, enemy_zone)

    def test_generate_map_stage_1_water_in_zone(self):
        room = generate_map(1)
        water_tile = "🌀 "
        water_zone = ([(row, col) for row in range(2, 8) for col in range(2, 7)] +
                      [(row, col) for row in range(2, 8) for col in range(10, 15)])
        water_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] == water_tile]
        for water in water_spots:
            self.assertIn(water, water_zone)

    def test_generate_map_stage_2_water_in_zone(self):
        room = generate_map(2)
        water_tile = "🌀 "
        water_zone = ([(row, col) for row in range(2, 8) for col in range(2, 7)] +
                      [(row, col) for row in range(2, 8) for col in range(10, 15)])
        water_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] == water_tile]
        for water in water_spots:
            self.assertIn(water, water_zone)

    def test_generate_map_stage_3_water_in_zone(self):
        room = generate_map(3)
        water_tile = "🌀 "
        water_zone = ([(row, col) for row in range(2, 8) for col in range(2, 7)] +
                      [(row, col) for row in range(2, 8) for col in range(10, 15)])
        water_spots = [(row, col) for row in range(10) for col in range(17) if room[row][col] == water_tile]
        for water in water_spots:
            self.assertIn(water, water_zone)

    def test_generate_map_boss_room_boss_location(self):
        room = generate_map(4)
        self.assertEqual(room[4][8], "💀 ")

    def test_generate_map_boss_room_rewards(self):
        room = generate_map(4)
        self.assertEqual(room[8][6], "🎁 ")
        self.assertEqual(room[8][10], "🎁 ")

    def test_generate_map_boss_room_door_location(self):
        room = generate_map(4)
        self.assertEqual(room[0][8], "🚪 ")
        self.assertEqual(room[9][8], "🔒 ")
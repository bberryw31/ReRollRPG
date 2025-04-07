from unittest import TestCase

from game import room_cleared


class TestRoomCleared(TestCase):

    def test_room_cleared_no_enemies(self):
        room = [[".  "] * 17 for _ in range(10)]
        self.assertTrue(room_cleared(room))

    def test_room_cleared_with_tunnel_ant(self):
        room = [[".  "] * 17 for _ in range(10)]
        room[1][1] = "🐜 "
        self.assertFalse(room_cleared(room))

    def test_room_cleared_with_cave_bat(self):
        room = [[".  "] * 17 for _ in range(10)]
        room[1][1] = "🦇 "
        self.assertFalse(room_cleared(room))

    def test_room_cleared_with_ancient_raptor(self):
        room = [[".  "] * 17 for _ in range(10)]
        room[1][1] = "🦖 "
        self.assertFalse(room_cleared(room))

    def test_room_cleared_with_angry_crocodile(self):
        room = [[".  "] * 17 for _ in range(10)]
        room[1][1] = "🐊 "
        self.assertFalse(room_cleared(room))

    def test_room_cleared_with_baby_unicorn(self):
        room = [[".  "] * 17 for _ in range(10)]
        room[1][1] = "🦄 "
        self.assertFalse(room_cleared(room))

    def test_room_cleared_with_fat_serpent(self):
        room = [[".  "] * 17 for _ in range(10)]
        room[1][1] = "🐍 "
        self.assertFalse(room_cleared(room))

    def test_room_cleared_with_scorpion_prince(self):
        room = [[".  "] * 17 for _ in range(10)]
        room[1][1] = "🦂 "
        self.assertFalse(room_cleared(room))

    def test_room_cleared_with_doom_slug(self):
        room = [[".  "] * 17 for _ in range(10)]
        room[1][1] = "🐌 "
        self.assertFalse(room_cleared(room))

    def test_room_cleared_with_giant_mosquito(self):
        room = [[".  "] * 17 for _ in range(10)]
        room[1][1] = "🦟 "
        self.assertFalse(room_cleared(room))

    def test_room_cleared_with_boss_demon_king(self):
        room = [[".  "] * 17 for _ in range(10)]
        room[1][1] = "💀 "
        self.assertFalse(room_cleared(room))

    def test_room_cleared_with_water(self):
        room = [[".  "] * 17 for _ in range(10)]
        room[4][5] = "🌀 "
        self.assertTrue(room_cleared(room))

    def test_room_cleared_with_reward(self):
        room = [[".  "] * 17 for _ in range(10)]
        room[2][7] = "🎁 "
        self.assertTrue(room_cleared(room))

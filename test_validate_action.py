from unittest import TestCase

from unittest.mock import patch

from game import validate_action


class Test(TestCase):

    def test_validate_action_quit_stage_0(self):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        result = validate_action(character, "q", room, 0)
        self.assertEqual(result, "q")

    def test_validate_action_quit_stage_1(self):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        result = validate_action(character, "q", room, 1)
        self.assertEqual(result, "q")

    def test_validate_action_quit_stage_2(self):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        result = validate_action(character, "q", room, 2)
        self.assertEqual(result, "q")

    def test_validate_action_quit_stage_3(self):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        result = validate_action(character, "q", room, 3)
        self.assertEqual(result, "q")

    def test_validate_action_quit_stage_4(self):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        result = validate_action(character, "q", room, 4)
        self.assertEqual(result, "q")

    def test_validate_action_empty_tile_stage_0(self):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        result = validate_action(character, (-1, 0), room, 0)
        self.assertEqual(result, (4, 5))

    def test_validate_action_empty_tile_stage_1(self):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        result = validate_action(character, (-1, 0), room, 1)
        self.assertEqual(result, (4, 5))

    def test_validate_action_empty_tile_stage_2(self):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        result = validate_action(character, (-1, 0), room, 2)
        self.assertEqual(result, (4, 5))

    def test_validate_action_empty_tile_stage_3(self):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        result = validate_action(character, (-1, 0), room, 3)
        self.assertEqual(result, (4, 5))

    def test_validate_action_empty_tile_stage_4(self):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        result = validate_action(character, (-1, 0), room, 4)
        self.assertEqual(result, (4, 5))

    @patch("game.fight_enemy", return_value=True)
    @patch("game.open_reward", return_value=True)
    def test_validate_action_enemy_defeated_reward_claimed_stage_1(self, _, __):
        character = {"coordinates": (5, 5), "HP": 10}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🦇 "
        result = validate_action(character, (-1, 0), room, 1)
        self.assertEqual(result, (4, 5))

    @patch("game.fight_enemy", return_value=True)
    @patch("game.open_reward", return_value=True)
    def test_validate_action_enemy_defeated_reward_claimed_stage_2(self, _, __):
        character = {"coordinates": (5, 5), "HP": 10}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🦇 "
        result = validate_action(character, (-1, 0), room, 2)
        self.assertEqual(result, (4, 5))

    @patch("game.fight_enemy", return_value=True)
    @patch("game.open_reward", return_value=True)
    def test_validate_action_enemy_defeated_reward_claimed_stage_3(self, _, __):
        character = {"coordinates": (5, 5), "HP": 10}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🦇 "
        result = validate_action(character, (-1, 0), room, 3)
        self.assertEqual(result, (4, 5))

    @patch("game.fight_enemy", return_value=True)
    @patch("game.open_reward", return_value=True)
    def test_validate_action_boss_defeated_reward_claimed_stage_4(self, _, __):
        character = {"coordinates": (5, 5), "HP": 10}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "💀 "
        result = validate_action(character, (-1, 0), room, 4)
        self.assertEqual(result, (4, 5))

    @patch("game.fight_enemy", return_value=True)
    @patch("game.open_reward", return_value=False)
    def test_validate_action_enemy_defeated_reward_unclaimed_stage_1(self, _, __):
        character = {"coordinates": (5, 5), "HP": 10}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🦇 "
        result = validate_action(character, (-1, 0), room, 1)
        self.assertEqual(result, (5, 5))

    @patch("game.fight_enemy", return_value=True)
    @patch("game.open_reward", return_value=False)
    def test_validate_action_enemy_defeated_reward_unclaimed_stage_2(self, _, __):
        character = {"coordinates": (5, 5), "HP": 10}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🦇 "
        result = validate_action(character, (-1, 0), room, 2)
        self.assertEqual(result, (5, 5))

    @patch("game.fight_enemy", return_value=True)
    @patch("game.open_reward", return_value=False)
    def test_validate_action_enemy_defeated_reward_unclaimed_stage_3(self, _, __):
        character = {"coordinates": (5, 5), "HP": 10}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🦇 "
        result = validate_action(character, (-1, 0), room, 3)
        self.assertEqual(result, (5, 5))

    @patch("game.fight_enemy", return_value=True)
    @patch("game.open_reward", return_value=False)
    def test_validate_action_boss_defeated_reward_unclaimed_stage_4(self, _, __):
        character = {"coordinates": (5, 5), "HP": 10}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "💀 "
        result = validate_action(character, (-1, 0), room, 4)
        self.assertEqual(result, (5, 5))

    @patch("game.fight_enemy", return_value=False)
    def test_validate_action_enemy_kills_character_stage_1(self, _):
        character = {"coordinates": (5, 5), "HP": 0}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🦇 "
        result = validate_action(character, (-1, 0), room, 1)
        self.assertEqual(result, "dead")

    @patch("game.fight_enemy", return_value=False)
    def test_validate_action_enemy_kills_character_stage_2(self, _):
        character = {"coordinates": (5, 5), "HP": 0}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🦇 "
        result = validate_action(character, (-1, 0), room, 2)
        self.assertEqual(result, "dead")

    @patch("game.fight_enemy", return_value=False)
    def test_validate_action_enemy_kills_character_stage_3(self, _):
        character = {"coordinates": (5, 5), "HP": 0}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🦇 "
        result = validate_action(character, (-1, 0), room, 3)
        self.assertEqual(result, "dead")

    @patch("game.fight_enemy", return_value=False)
    def test_validate_action_enemy_kills_character_stage_4(self, _):
        character = {"coordinates": (5, 5), "HP": 0}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🦇 "
        result = validate_action(character, (-1, 0), room, 4)
        self.assertEqual(result, "dead")

    @patch("game.open_reward", return_value=True)
    def test_validate_action_reward_tile_claim_stage_0(self, _):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🎁 "
        result = validate_action(character, (-1, 0), room, 0)
        self.assertEqual(result, (4, 5))

    @patch("game.open_reward", return_value=True)
    def test_validate_action_reward_tile_claim_stage_1(self, _):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🎁 "
        result = validate_action(character, (-1, 0), room, 1)
        self.assertEqual(result, (4, 5))

    @patch("game.open_reward", return_value=True)
    def test_validate_action_reward_tile_claim_stage_2(self, _):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🎁 "
        result = validate_action(character, (-1, 0), room, 2)
        self.assertEqual(result, (4, 5))

    @patch("game.open_reward", return_value=True)
    def test_validate_action_reward_tile_claim_stage_3(self, _):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🎁 "
        result = validate_action(character, (-1, 0), room, 3)
        self.assertEqual(result, (4, 5))

    @patch("game.open_reward", return_value=True)
    def test_validate_action_reward_tile_claim_stage_4(self, _):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🎁 "
        result = validate_action(character, (-1, 0), room, 4)
        self.assertEqual(result, (4, 5))

    @patch("game.open_reward", return_value=False)
    def test_validate_action_reward_tile_not_claim_stage_0(self, _):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🎁 "
        result = validate_action(character, (-1, 0), room, 0)
        self.assertEqual(result, (5, 5))

    @patch("game.open_reward", return_value=False)
    def test_validate_action_reward_tile_not_claim_stage_1(self, _):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🎁 "
        result = validate_action(character, (-1, 0), room, 1)
        self.assertEqual(result, (5, 5))

    @patch("game.open_reward", return_value=False)
    def test_validate_action_reward_tile_not_claim_stage_2(self, _):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🎁 "
        result = validate_action(character, (-1, 0), room, 2)
        self.assertEqual(result, (5, 5))

    @patch("game.open_reward", return_value=False)
    def test_validate_action_reward_tile_not_claim_stage_3(self, _):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🎁 "
        result = validate_action(character, (-1, 0), room, 3)
        self.assertEqual(result, (5, 5))

    @patch("game.open_reward", return_value=False)
    def test_validate_action_reward_tile_not_claim_stage_4(self, _):
        character = {"coordinates": (5, 5)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🎁 "
        result = validate_action(character, (-1, 0), room, 4)
        self.assertEqual(result, (5, 5))

    @patch("game.drink_water")
    def test_validate_action_water_tile_survive_stage_1(self, _):
        character = {"coordinates": (5, 5), "HP": 5}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🌀 "
        result = validate_action(character, (-1, 0), room, 1)
        self.assertEqual(result, (5, 5))

    @patch("game.drink_water")
    def test_validate_action_water_tile_survive_stage_2(self, _):
        character = {"coordinates": (5, 5), "HP": 5}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🌀 "
        result = validate_action(character, (-1, 0), room, 2)
        self.assertEqual(result, (5, 5))

    @patch("game.drink_water")
    def test_validate_action_water_tile_survive_stage_3(self, _):
        character = {"coordinates": (5, 5), "HP": 5}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🌀 "
        result = validate_action(character, (-1, 0), room, 3)
        self.assertEqual(result, (5, 5))

    @patch("game.drink_water", side_effect=lambda character: character.update({"HP": 0}))
    def test_validate_action_water_tile_death_stage_1(self, _):
        character = {"coordinates": (5, 5), "HP": 1}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🌀 "
        result = validate_action(character, (-1, 0), room, 1)
        self.assertEqual(result, "dead")

    @patch("game.drink_water", side_effect=lambda character: character.update({"HP": 0}))
    def test_validate_action_water_tile_death_stage_2(self, _):
        character = {"coordinates": (5, 5), "HP": 1}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🌀 "
        result = validate_action(character, (-1, 0), room, 2)
        self.assertEqual(result, "dead")

    @patch("game.drink_water", side_effect=lambda character: character.update({"HP": 0}))
    def test_validate_action_water_tile_death_stage_3(self, _):
        character = {"coordinates": (5, 5), "HP": 1}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][5] = "🌀 "
        result = validate_action(character, (-1, 0), room, 3)
        self.assertEqual(result, "dead")

    @patch("game.room_cleared", return_value=False)
    def test_validate_action_door_not_cleared_stage_1(self, _):
        character = {"coordinates": (1, 8)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[0][8] = "🚪 "
        result = validate_action(character, (-1, 0), room, 1)
        self.assertEqual("\033[91mYou must first defeat all enemies!\033[0m", result)

    @patch("game.room_cleared", return_value=False)
    def test_validate_action_door_not_cleared_stage_2(self, _):
        character = {"coordinates": (1, 8)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[0][8] = "🚪 "
        result = validate_action(character, (-1, 0), room, 2)
        self.assertEqual("\033[91mYou must first defeat all enemies!\033[0m", result)

    @patch("game.room_cleared", return_value=False)
    def test_validate_action_door_not_cleared_stage_3(self, _):
        character = {"coordinates": (1, 8)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[0][8] = "🚪 "
        result = validate_action(character, (-1, 0), room, 3)
        self.assertEqual("\033[91mYou must first defeat all enemies!\033[0m", result)

    @patch("game.room_cleared", return_value=False)
    def test_validate_action_door_not_cleared_stage_4(self, _):
        character = {"coordinates": (1, 8)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[0][8] = "🚪 "
        result = validate_action(character, (-1, 0), room, 4)
        self.assertEqual("\033[91mYou must first defeat all enemies!\033[0m", result)

    @patch("game.room_cleared", return_value=True)
    def test_validate_action_door_cleared_stage_0(self, mock_clear):
        character = {"coordinates": (1, 8)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[0][8] = "🚪 "
        result = validate_action(character, (-1, 0), room, 0)
        self.assertEqual(result, "clear")

    @patch("game.room_cleared", return_value=True)
    def test_validate_action_door_cleared_stage_1(self, mock_clear):
        character = {"coordinates": (1, 8)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[0][8] = "🚪 "
        result = validate_action(character, (-1, 0), room, 1)
        self.assertEqual(result, "clear")

    @patch("game.room_cleared", return_value=True)
    def test_validate_action_door_cleared_stage_2(self, mock_clear):
        character = {"coordinates": (1, 8)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[0][8] = "🚪 "
        result = validate_action(character, (-1, 0), room, 2)
        self.assertEqual(result, "clear")

    @patch("game.room_cleared", return_value=True)
    def test_validate_action_door_cleared_stage_3(self, mock_clear):
        character = {"coordinates": (1, 8)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[0][8] = "🚪 "
        result = validate_action(character, (-1, 0), room, 3)
        self.assertEqual(result, "clear")

    @patch("game.room_cleared", return_value=True)
    def test_validate_action_door_cleared_stage_4(self, mock_clear):
        character = {"coordinates": (1, 8)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[0][8] = "🚪 "
        result = validate_action(character, (-1, 0), room, 4)
        self.assertEqual(result, "clear")

    def test_validate_action_locked_door_stage_0(self):
        character = {"coordinates": (8, 8)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[9][8] = "🔒 "
        result = validate_action(character, (1, 0), room, 0)
        self.assertIn("\033[91mThe door is locked from the other side.\033[0m", result)

    def test_validate_action_locked_door_stage_1(self):
        character = {"coordinates": (8, 8)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[9][8] = "🔒 "
        result = validate_action(character, (1, 0), room, 1)
        self.assertIn("\033[91mThe door is locked from the other side.\033[0m", result)

    def test_validate_action_locked_door_stage_2(self):
        character = {"coordinates": (8, 8)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[9][8] = "🔒 "
        result = validate_action(character, (1, 0), room, 2)
        self.assertIn("\033[91mThe door is locked from the other side.\033[0m", result)

    def test_validate_action_locked_door_stage_3(self):
        character = {"coordinates": (8, 8)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[9][8] = "🔒 "
        result = validate_action(character, (1, 0), room, 3)
        self.assertIn("\033[91mThe door is locked from the other side.\033[0m", result)

    def test_validate_action_locked_door_stage_4(self):
        character = {"coordinates": (8, 8)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[9][8] = "🔒 "
        result = validate_action(character, (1, 0), room, 4)
        self.assertIn("\033[91mThe door is locked from the other side.\033[0m", result)

    def test_validate_action_blocked_by_wall_stage_0(self):
        character = {"coordinates": (1, 1)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        result = validate_action(character, (-1, 0), room, 0)
        self.assertIn("\033[91mSomething is blocking your way...\033[0m", result)

    def test_validate_action_blocked_by_wall_stage_1(self):
        character = {"coordinates": (1, 1)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        result = validate_action(character, (-1, 0), room, 1)
        self.assertIn("\033[91mSomething is blocking your way...\033[0m", result)

    def test_validate_action_blocked_by_wall_stage_2(self):
        character = {"coordinates": (1, 1)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        result = validate_action(character, (-1, 0), room, 2)
        self.assertIn("\033[91mSomething is blocking your way...\033[0m", result)

    def test_validate_action_blocked_by_wall_stage_3(self):
        character = {"coordinates": (1, 1)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        result = validate_action(character, (-1, 0), room, 3)
        self.assertIn("\033[91mSomething is blocking your way...\033[0m", result)

    def test_validate_action_blocked_by_wall_stage_4(self):
        character = {"coordinates": (1, 1)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        result = validate_action(character, (-1, 0), room, 4)
        self.assertIn("\033[91mSomething is blocking your way...\033[0m", result)

    def test_validate_action_blocked_by_other_thing(self):
        character = {"coordinates": (4, 3)}
        room = ([["⬛️ "] * 17] +
                [["⬛️ "] + [".  "] * 15 + ["⬛️ "] for _ in range(8)] +
                [["⬛️ "] * 17])
        room[4][4] = "⬆️ "
        result = validate_action(character, (0, 1), room, 0)
        self.assertIn("\033[91mSomething is blocking your way...\033[0m", result)
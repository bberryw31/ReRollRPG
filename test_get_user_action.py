from unittest import TestCase

from unittest.mock import patch

import io

from game import get_user_action


class TestGetUserAction(TestCase):

    @patch("builtins.input", side_effect=["w"])
    def test_get_user_action_lower_w(self, mock_input):
        self.assertEqual(get_user_action(), (-1, 0))

    @patch("builtins.input", side_effect=["W"])
    def test_get_user_action_upper_w(self, mock_input):
        self.assertEqual(get_user_action(), (-1, 0))

    @patch("builtins.input", side_effect=["up"])
    def test_get_user_action_lower_up(self, mock_input):
        self.assertEqual(get_user_action(), (-1, 0))

    @patch("builtins.input", side_effect=["UP"])
    def test_get_user_action_upper_up(self, mock_input):
        self.assertEqual(get_user_action(), (-1, 0))

    @patch("builtins.input", side_effect=["Up"])
    def test_get_user_action_mixed_case_Up(self, mock_input):
        self.assertEqual(get_user_action(), (-1, 0))

    @patch("builtins.input", side_effect=["uP"])
    def test_get_user_action_mixed_case_uP(self, mock_input):
        self.assertEqual(get_user_action(), (-1, 0))

    @patch("builtins.input", side_effect=["s"])
    def test_get_user_action_lower_s(self, mock_input):
        self.assertEqual(get_user_action(), (1, 0))

    @patch("builtins.input", side_effect=["S"])
    def test_get_user_action_upper_s(self, mock_input):
        self.assertEqual(get_user_action(), (1, 0))

    @patch("builtins.input", side_effect=["down"])
    def test_get_user_action_lower_down(self, mock_input):
        self.assertEqual(get_user_action(), (1, 0))

    @patch("builtins.input", side_effect=["DOWN"])
    def test_get_user_action_upper_down(self, mock_input):
        self.assertEqual(get_user_action(), (1, 0))

    @patch("builtins.input", side_effect=["Down"])
    def test_get_user_action_mixed_case_Down(self, mock_input):
        self.assertEqual(get_user_action(), (1, 0))

    @patch("builtins.input", side_effect=["dOwN"])
    def test_get_user_action_mixed_case_dOwN(self, mock_input):
        self.assertEqual(get_user_action(), (1, 0))

    @patch("builtins.input", side_effect=["a"])
    def test_get_user_action_lower_a(self, mock_input):
        self.assertEqual(get_user_action(), (0, -1))

    @patch("builtins.input", side_effect=["A"])
    def test_get_user_action_upper_a(self, mock_input):
        self.assertEqual(get_user_action(), (0, -1))

    @patch("builtins.input", side_effect=["left"])
    def test_get_user_action_lower_left(self, mock_input):
        self.assertEqual(get_user_action(), (0, -1))

    @patch("builtins.input", side_effect=["LEFT"])
    def test_get_user_action_upper_left(self, mock_input):
        self.assertEqual(get_user_action(), (0, -1))

    @patch("builtins.input", side_effect=["Left"])
    def test_get_user_action_mixed_case_Left(self, mock_input):
        self.assertEqual(get_user_action(), (0, -1))

    @patch("builtins.input", side_effect=["lEfT"])
    def test_get_user_action_mixed_case_lEfT(self, mock_input):
        self.assertEqual(get_user_action(), (0, -1))

    @patch("builtins.input", side_effect=["d"])
    def test_get_user_action_lower_d(self, mock_input):
        self.assertEqual(get_user_action(), (0, 1))

    @patch("builtins.input", side_effect=["D"])
    def test_get_user_action_upper_d(self, mock_input):
        self.assertEqual(get_user_action(), (0, 1))

    @patch("builtins.input", side_effect=["right"])
    def test_get_user_action_lower_right(self, mock_input):
        self.assertEqual(get_user_action(), (0, 1))

    @patch("builtins.input", side_effect=["RIGHT"])
    def test_get_user_action_upper_right(self, mock_input):
        self.assertEqual(get_user_action(), (0, 1))

    @patch("builtins.input", side_effect=["Right"])
    def test_get_user_action_mixed_case_Right(self, mock_input):
        self.assertEqual(get_user_action(), (0, 1))

    @patch("builtins.input", side_effect=["RiGhT"])
    def test_get_user_action_mixed_case_RiGhT(self, mock_input):
        self.assertEqual(get_user_action(), (0, 1))

    @patch("builtins.input", side_effect=["q", "y"])
    def test_get_user_action_lower_q_confirm(self, mock_input):
        self.assertEqual(get_user_action(), "q")

    @patch("builtins.input", side_effect=["q", "Y"])
    def test_get_user_action_lower_q_upper_confirm(self, mock_input):
        self.assertEqual(get_user_action(), "q")

    @patch("builtins.input", side_effect=["Q", "y"])
    def test_get_user_action_upper_q_confirm(self, mock_input):
        self.assertEqual(get_user_action(), "q")

    @patch("builtins.input", side_effect=["quit", "y"])
    def test_get_user_action_lower_quit_confirm(self, mock_input):
        self.assertEqual(get_user_action(), "q")

    @patch("builtins.input", side_effect=["QUIT", "y"])
    def test_get_user_action_upper_quit_confirm(self, mock_input):
        self.assertEqual(get_user_action(), "q")

    @patch("builtins.input", side_effect=["Quit", "y"])
    def test_get_user_action_mixed_case_quit_confirm(self, mock_input):
        self.assertEqual(get_user_action(), "q")

    @patch("builtins.input", side_effect=["q", "n", "w"])
    def test_get_user_action_quit_reject_then_valid(self, mock_input):
        self.assertEqual(get_user_action(), (-1, 0))

    @patch("builtins.input", side_effect=["hello", "a"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_user_action_invalid_input_string_then_valid(self, mock_stdout, mock_input):
        result = get_user_action()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input.", output)
        self.assertEqual(result, (0, -1))

    @patch("builtins.input", side_effect=["123", "a"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_user_action_invalid_input_integer_then_valid(self, mock_stdout, mock_input):
        result = get_user_action()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input.", output)
        self.assertEqual(result, (0, -1))

    @patch("builtins.input", side_effect=["", "a"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_user_action_invalid_input_empty_then_valid(self, mock_stdout, mock_input):
        result = get_user_action()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input.", output)
        self.assertEqual(result, (0, -1))

    @patch("builtins.input", side_effect=[" ", "a"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_user_action_invalid_input_space_then_valid(self, mock_stdout, mock_input):
        result = get_user_action()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input.", output)
        self.assertEqual(result, (0, -1))

    @patch("builtins.input", side_effect=["hello", "world", "123", "", "a"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_user_action_multiple_invalid_inputs_then_valid(self, mock_stdout, mock_input):
        result = get_user_action()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input.", output)
        self.assertEqual(result, (0, -1))
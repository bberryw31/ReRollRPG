import unittest

from game import stage_counter


class TestStageCounter(unittest.TestCase):

    def test_stage_counter_start_from_zero(self):
        counter = stage_counter(0)
        self.assertEqual(next(counter), 0)
        self.assertEqual(next(counter), 1)
        self.assertEqual(next(counter), 2)
        self.assertEqual(next(counter), 3)
        self.assertEqual(next(counter), 4)

    def test_stage_counter_start_from_ten(self):
        counter = stage_counter(10)
        self.assertEqual(next(counter), 10)
        self.assertEqual(next(counter), 11)
        self.assertEqual(next(counter), 12)
        self.assertEqual(next(counter), 13)
        self.assertEqual(next(counter), 14)

    def test_stage_counter_negative_start(self):
        counter = stage_counter(-5)
        self.assertEqual(next(counter), -5)
        self.assertEqual(next(counter), -4)
        self.assertEqual(next(counter), -3)
        self.assertEqual(next(counter), -2)
        self.assertEqual(next(counter), -1)
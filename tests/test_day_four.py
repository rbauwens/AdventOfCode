import unittest
from days.day_four import meets_criteria_one, day_four_part_one, meets_criteria_two, day_four_part_two


class AddTests(unittest.TestCase):
    def test_meets_critera_one(self):
        self.assertEqual(True, meets_criteria_one(111111))

    def test_meets_critera_two(self):
        self.assertEqual(False, meets_criteria_one(223450))

    def test_meets_critera_three(self):
        self.assertEqual(False, meets_criteria_one(123789))

    def test_day_four_part_one(self):
        self.assertEqual(530, day_four_part_one())

    def test_meets_critera2_one(self):
        self.assertEqual(True, meets_criteria_two(112233))

    def test_meets_critera2_two(self):
        self.assertEqual(False, meets_criteria_two(123444))

    def test_meets_critera2_three(self):
        self.assertEqual(True, meets_criteria_two(111122))

    def test_meets_critera2_four(self):
        self.assertEqual(False, meets_criteria_two(111222))

    def test_meets_critera2_5(self):
        self.assertEqual(True, meets_criteria_two(122233))

    def test_day_four_part_two(self):
        self.assertEqual(324, day_four_part_two())

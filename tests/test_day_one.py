import unittest
from days.day_one import compute_fuel, compute_sum_fuel, compute_fuel_recursive, compute_sum_fuel_recursive


class PartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(2, compute_fuel(12))

    def test_two(self):
        self.assertEqual(2, compute_fuel(14))

    def test_three(self):
        self.assertEqual(654, compute_fuel(1969))

    def test_four(self):
        self.assertEqual(33583, compute_fuel(100756))
    
    def test_final(self):
        self.assertEqual(3515171, compute_sum_fuel())

class PartTwo(unittest.TestCase):
    def test_p2_one(self):
        self.assertEqual(2, compute_fuel_recursive(14))

    def test_p2_two(self):
        self.assertEqual(966, compute_fuel_recursive(1969))

    def test_p2_three(self):
        self.assertEqual(50346, compute_fuel_recursive(100756))

    def test_final(self):
        self.assertEqual(5269882, compute_sum_fuel_recursive())


import unittest
from days.day_three import closest_distance, day_three_part_one, day_three_part_two

class AddTests(unittest.TestCase):
    def test_one(self):
        wire1 = ["R8", "U5", "L5", "D3"]
        wire2 = ["U7", "R6", "D4", "L4"]
        self.assertEqual(6, closest_distance(wire1, wire2))

    def test_two(self):
        string1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
        string2 = "U62,R66,U55,R34,D71,R55,D58,R83"
        wire1 = string1.split(",")
        wire2 = string2.split(",")
        self.assertEqual(159, closest_distance(wire1, wire2))

    def test_three(self):
        string1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
        string2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        wire1 = string1.split(",")
        wire2 = string2.split(",")
        self.assertEqual(135, closest_distance(wire1, wire2))

    def test_part_one(self):
        self.assertEqual(303, day_three_part_one())
        

    def test_part_two_one(self):
        wire1 = ["R8", "U5", "L5", "D3"]
        wire2 = ["U7", "R6", "D4", "L4"]
        self.assertEqual(30, closest_distance(wire1, wire2, True))

    def test_part_two_two(self):
        string1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
        string2 = "U62,R66,U55,R34,D71,R55,D58,R83"
        wire1 = string1.split(",")
        wire2 = string2.split(",")
        self.assertEqual(610, closest_distance(wire1, wire2, True))

    def test_part_two_three(self):
        string1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
        string2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        wire1 = string1.split(",")
        wire2 = string2.split(",")
        self.assertEqual(410, closest_distance(wire1, wire2, True))

    def test_part_two(self):
        self.assertEqual(11222, day_three_part_two())
    
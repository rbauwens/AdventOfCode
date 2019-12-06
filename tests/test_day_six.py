import unittest
from days.day_six import num_orbits1

class AddTests(unittest.TestCase):
    # A-B
    def test_one(self):
        orbits = dict()
        orbits["A"] = "B"
        num_orbits = 0
        for focus in orbits:
            _, new = num_orbits1(orbits, focus, 0)
            num_orbits = num_orbits + new
        self.assertEqual(1, num_orbits)


# A -B -C
    def test_two(self):
        orbits = dict()
        orbits["A"] = "B"
        orbits["B"] = "C"
        num_orbits = 0
        for focus in orbits:
            _, new = num_orbits1(orbits, focus, 0)
            num_orbits = num_orbits + new
        self.assertEqual(3, num_orbits)


#    B - C
#   /
# A
#  \
#   D

    def test_three(self):
        orbits = dict()
        orbits["A"] = ["B", "D"]
        orbits["B"] = "C"
        num_orbits = 0
        for focus in orbits:
            _, new = num_orbits1(orbits, focus, 0)
            num_orbits = num_orbits + new
        self.assertEqual(4, num_orbits)

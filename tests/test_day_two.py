import unittest
from days.day_two import opcode, day_two_part_one

class AddTests(unittest.TestCase):
    def test_one(self):
        self.assertEqual([2,0,0,0,99], opcode([1,0,0,0,99]))

    def test_two(self):
        self.assertEqual([2,3,0,6,99], opcode([2,3,0,3,99]))

    def test_three(self):
        self.assertEqual([2,4,4,5,99,9801], opcode([2,4,4,5,99,0]))

    def test_four(self):
        self.assertEqual([30,1,1,4,2,5,6,0,99], opcode([1,1,1,4,99,5,6,0,99]))

    def test_final(self):
        self.assertEqual(3562672, day_two_part_one())



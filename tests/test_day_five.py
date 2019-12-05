import unittest
from parameterized import parameterized
from days.day_five import get_opcode, day_five


class AddTests(unittest.TestCase):
    
    @parameterized.expand([
        [2, [1, 0, 0], 102],
        [2, [0, 1, 0], 1002],
        [2, [0, 1, 1], 11002]
        ])
    def test_get_opcode(self, exp_opcode, exp_modes, entry):
        opcode, modes = get_opcode(entry)
        self.assertEqual(opcode, exp_opcode)
        self.assertEqual(modes, exp_modes)

    # input 1
    # def test_day_five_part_one(self):
    #     self.assertEqual(9938601, day_five())

    # input 5
    # def test_day_five_part_one(self):
    #     self.assertEqual(4283952, day_five())
    

    
import unittest
from unittest.mock import patch
from parameterized import parameterized
from days.day_five import get_opcode, day_five, take_input, opcode


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

    @patch('days.day_five.take_input', return_value='7')
    def test_answer_one(self, input):
        input_data = [3,9,8,9,10,9,4,9,99,-1,8]
        result = opcode(input_data)
        self.assertEqual(result, 0)
    
    @patch('days.day_five.take_input', return_value='8')
    def test_answer_two(self, input):
        input_data = [3,9,8,9,10,9,4,9,99,-1,8]
        result = opcode(input_data)
        self.assertEqual(result, 1)

    @patch('days.day_five.take_input', return_value='8')
    def test_answer_three(self, input):
        input_data = [3,3,1108,-1,8,3,4,3,99]
        result = opcode(input_data)
        self.assertEqual(result, 1)

    @patch('days.day_five.take_input', return_value='9')
    def test_answer_four(self, input):
        input_data = [3,3,1108,-1,8,3,4,3,99]
        result = opcode(input_data)
        self.assertEqual(result, 0)

    @patch('days.day_five.take_input', return_value='7')
    def test_answer_five(self, input):
        input_data = [3,3,1107,-1,8,3,4,3,99]
        result = opcode(input_data)
        self.assertEqual(result, 1)

    @patch('days.day_five.take_input', return_value='9')
    def test_answer_six(self, input):
        input_data = [3,3,1107,-1,8,3,4,3,99]
        result = opcode(input_data)
        self.assertEqual(result, 0)

    @patch('days.day_five.take_input', return_value='0')
    def test_answer_seven(self, input):
        input_data = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        result = opcode(input_data)
        self.assertEqual(result, 0)

    @patch('days.day_five.take_input', return_value='9')
    def test_answer_eight(self, input):
        input_data = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        result = opcode(input_data)
        self.assertEqual(result, 1)

    @patch('days.day_five.take_input', return_value='0')
    def test_answer_nine(self, input):
        input_data = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        result = opcode(input_data)
        self.assertEqual(result, 0)

    @patch('days.day_five.take_input', return_value='9')
    def test_answer_ten(self, input):
        input_data = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        result = opcode(input_data)
        self.assertEqual(result, 1)

    @patch('days.day_five.take_input', return_value='6')
    def test_answer_eleven(self, input):
        input_data = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
        999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        result = opcode(input_data)
        self.assertEqual(result, 999)

    @patch('days.day_five.take_input', return_value='8')
    def test_answer_twelve(self, input):
        input_data = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
        999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        result = opcode(input_data)
        self.assertEqual(result, 1000)

    @patch('days.day_five.take_input', return_value='9')
    def test_answer_thirteen(self, input):
        input_data = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
        999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        result = opcode(input_data)
        self.assertEqual(result, 1001)


    # # input 1
    # @patch('days.day_five.take_input', return_value='1')
    # def test_day_five_part_one(self, input):
    #     self.assertEqual(9938601, day_five())

    # input 5
    @patch('days.day_five.take_input', return_value='5')
    def test_day_five_part_two(self, input):
        self.assertEqual(4283952, day_five())
    

    
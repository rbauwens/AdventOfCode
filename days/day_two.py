import sys
import os

ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_two_data')


def get_opcode():
    with open(DATA_FILE) as fp:
        line = fp.readline()
        opcode_from_file = list(map(int, line.split(",")))

    return opcode_from_file


def opcode(array):
    new_array = array
    op_index = 0

    while op_index < len(array):

        operation = array[op_index]
        if operation == 99:
            return new_array

        index_1 = array[op_index + 1]
        index_2 = array[op_index + 2]
        res_index = array[op_index + 3]

        num1 = array[index_1]
        num2 = array[index_2]

        if operation == 1:
            result = num1 + num2
        elif operation == 2:
            result = num1 * num2
        else:
            sys.exit("Invalid operation code")

        new_array[res_index] = result

        op_index = op_index + 4

def day_two_part_one():
    opcode_array = get_opcode()
    opcode_array[1] = 12
    opcode_array[2] = 2
    final_array = opcode(opcode_array)
    return final_array[0]


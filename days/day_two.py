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
    new_array = []
    new_array = array
    op_index = 0

    while op_index < len(array):

        operation = array[op_index]
        if operation == 99:
            return new_array, ""

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
            return [0], "Invalid operation code"
            #sys.exit("Invalid operation code")

        new_array[res_index] = result

        op_index = op_index + 4

def compute_part_two_answer(noun, verb):
    return 100 * noun + verb

def day_two_part_one():
    opcode_array = get_opcode()
    opcode_array[1] = 12
    opcode_array[2] = 2
    final_array, _ = opcode(opcode_array)
    return final_array[0]

def day_two_part_two():
    opcode_array = get_opcode()
    altered = opcode_array
    altered[1] = 12
    altered[2] = 2

    for noun in range(0,100):
        for verb in range(0,100):
        # noun = 12
        # verb = 2
            tmp_array = []
            tmp_array = get_opcode()
            

            tmp_array[1] = noun
            tmp_array[2] = verb

            # if (noun == 12) & (verb == 2):
            #     if tmp_array != altered:
            #         sys.exit("PROBLEMS")
            #     else:
            #         answer, _ = opcode(tmp_array)
            #         print("HERE: {}".format(answer[0]))

            final_array, _ = opcode(tmp_array)
            # print("answer: {}".format(final_array[0]))
            # print("error: {}".format(error))
            answer = final_array[0]
            if answer == 19690720:
                print("FOUND IT")
                print ("noun {} verb {}".format(noun, verb))
                part_two_answer = compute_part_two_answer(noun, verb)
                print("So the answer 100 * noun + verb = {}".format(part_two_answer))
                return part_two_answer
    print("DID NOT FIND IT")


day_two_part_two()

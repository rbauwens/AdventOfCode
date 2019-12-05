import math 
import os
import sys

ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_five_data')


def get_opcode_from_file():
    with open(DATA_FILE) as fp:
        line = fp.readline()
        opcode_from_file = list(map(int, line.split(",")))

    return opcode_from_file

def take_input():
    value = input("enter value")
    return value

def get_opcode(number):
    # last 2 digits are the code
    string_num = str(number)
    modes = [0, 0, 0]
    length = len(string_num)

    if length > 1:
        
        opcode = string_num[length - 2:]
        
        if length == 3:
            modes = [int(string_num[0]), 0, 0]
        elif length == 4:
            modes = [int(string_num[1]), int(string_num[0]), 0]
        elif length == 5:
            modes = [int(string_num[2]), int(string_num[1]), int(string_num[0])]
        
        return int(opcode), modes
    else:
        return number, modes
    

def opcode(array):
    new_array = []
    new_array = array
    op_index = 0

    while op_index < len(array):       
        operation, modes = get_opcode(array[op_index])
        if operation == 99:
            return new_array, ""

        elif operation == 1 or operation == 2 or \
        operation == 5 or operation == 6 or \
        operation == 7 or operation == 8:
            index_1 = array[op_index + 1]
            index_2 = array[op_index + 2]
            res_index = array[op_index + 3]

            if modes[0] == 0:
                num1 = array[index_1]
            elif modes[0] == 1:
                num1 = array[op_index + 1]

            if modes[1] == 0:
                num2 = array[index_2]
            elif modes[1] == 1:
                num2 = array[op_index + 2]

            if modes[2] == 0:
                res_index = array[op_index + 3]
            elif modes[2] == 1:
                raise("Immediate mode for return parameter")
            
        elif operation == 3 or operation == 4:
           res_index = array[op_index + 1]           

        if operation == 1:
            result = num1 + num2
            jump = 4
        elif operation == 2:
            result = num1 * num2
            jump = 4
        elif operation == 3:
            result = take_input()
            jump = 2
        elif operation == 4:
            if modes[0] == 0:
                result = array[res_index]
            else:
                result = res_index
            jump = 2
        elif operation == 5:
            if num1 != 0:
                op_index = num2
            else:
                op_index = op_index + 3
            continue
        elif operation == 6:
            if num1 == 0:
                op_index = num2
            else:
                op_index = op_index + 3
            continue
        elif operation == 7:
            if num1 < num2:
                result = 1
            else:
                result = 0
            jump = 4
        elif operation == 8:
            if num1 == num2:
                result = 1
            else:
                result = 0
            jump = 4
        else:
            sys.exit("Invalid operation code at op_index {}".format(op_index))

        if operation !=4:
            new_array[res_index] = int(result)
        elif operation == 4:
            print(result)
            

        op_index = op_index + jump


def day_five():
    opcode_array = get_opcode_from_file()
    opcode(opcode_array)


# opcode([3,9,8,9,10,9,4,9,99,-1,8])
# opcode([3,9,7,9,10,9,4,9,99,-1,8])
# opcode([3,3,1108,-1,8,3,4,3,99])
# opcode([3,3,1107,-1,8,3,4,3,99])
# opcode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
# opcode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1])
# opcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])


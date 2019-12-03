import math 
import os
import sys

ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_three_data')
EXPECTED_LINES = 2

def get_instructions():
    instructions = []
    with open(DATA_FILE) as fp:
        line = fp.readline()
        lines_read = 1
        while line:
            instructions.append(line.strip())
            line = fp.readline()
            lines_read += 1

    if (lines_read != EXPECTED_LINES + 1):
        sys.exit("Did not read the correct amount of lines")

    return instructions[0], instructions[1]

def get_wire_path(wire):
    starting_point = [0,0]
    wire_path = [starting_point]
    i = 0

    for instruction in wire:
        next_pos = wire_path[i].copy()
        
        direction = instruction[0]
        distance = int(instruction[1:])
        if direction == "R":
            for j in range(1, distance + 1):
                wire_path.append([next_pos[0] + j, next_pos[1]])
        elif direction == "L":
            for j in range(1, distance + 1):
                wire_path.append([next_pos[0] - j, next_pos[1]])
        elif direction == "U":
            for j in range(1, distance + 1):
                wire_path.append([next_pos[0], next_pos[1] + j])
        elif direction == "D":
            for j in range(1, distance + 1):
                wire_path.append([next_pos[0], next_pos[1] - j])
        else:
            raise("Unknown direction")
    
        i = i + distance
    
    return wire_path
    


def closest_distance(wire1, wire2, part_two = False):
    
    wire1_path = get_wire_path(wire1)
    wire2_path = get_wire_path(wire2)
    
    mat = [tuple(t) for t in wire1_path]
    mat2 = [tuple(t) for t in wire2_path]
    crossing_points = set(mat).intersection(mat2)
    crossing_points.remove((0,0))
    closest_distance = 99999999999
    
    if not part_two:        
        for point in crossing_points:
            point_distance = abs(point[0]) + abs(point[1])
            if point_distance < closest_distance:
                closest_distance = point_distance
                
        print(closest_distance)
        return closest_distance
    else:
        fewest_steps = 99999999999
        for point in crossing_points:
            wire1_steps = wire1_path.index(list(point))
            wire2_steps = wire2_path.index(list(point))
            print("wire1_steps: {}, wire1_steps: {}".format(wire1_steps, wire2_steps))
            total_steps = wire1_steps + wire2_steps

            if total_steps < fewest_steps:
                fewest_steps = total_steps
                
        print(fewest_steps)
        return fewest_steps


def day_three_part_one():
    string1, string2 = get_instructions()
    wire1 = string1.split(",")
    wire2 = string2.split(",")
    return closest_distance(wire1, wire2)


def day_three_part_two():
    string1, string2 = get_instructions()
    wire1 = string1.split(",")
    wire2 = string2.split(",")
    return closest_distance(wire1, wire2, True)


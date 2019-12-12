import math 
import os
import sys
from collections import defaultdict

ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'day_six_data')


def return_orbit(orbit):
    lines = orbit.split('\n')
    orbit_dict = defaultdict(list)
    for line in lines:
        focus = line.split(")")[0].strip()
        orbiter = line.split(")")[1].strip()
        
        orbit_dict[focus].append(orbiter)
    return orbit_dict

def return_orbit_part_two(orbit):
    lines = orbit.split('\n')
    orbit_dict = defaultdict(str)
    for line in lines:
        focus = line.split(")")[0].strip()
        orbiter = line.split(")")[1].strip()
        
        orbit_dict[orbiter] = focus
    return orbit_dict



def calculate_part_one(my_orbit):
    direct_count = my_orbit.count_direct("COM")
    indirect_count = 0

    for name in my_orbit.ORBIT:
        if name != "COM":
            indirect_count += my_orbit.count_direct(name)

    part_one = direct_count + indirect_count
    return part_one

class Orbits:
    
    def __init__(self, orbit):
        self.ORBIT = orbit  

    def count_direct(self, name):
        # my_sum = sum(self.count_direct(n) for n in self.ORBIT[name])
        loc = 0
        for n in self.ORBIT[name]:
            loc = loc + self.count_direct(n)
        return len(self.ORBIT[name])  + loc

    def get_orbits(self, name):
        # print(expected_orbit[name])
        while (name := self.ORBIT[name]) :
            # print(name)
            yield name


def part_one():

    with open(DATA_FILE, "r") as f:
        input_data = f.read()

    expected_orbit = return_orbit(input_data)
    my_orbit = Orbits(expected_orbit)
    part_one = calculate_part_one(my_orbit)
    return part_one


def calculate_part_two(string1):
    expected_orbit = return_orbit_part_two(string1)
    my_orbit = Orbits(expected_orbit)
    # print(expected_orbit)
    from_you = list(my_orbit.get_orbits("YOU"))
    from_santa = list(my_orbit.get_orbits("SAN"))
    intersection = set(from_you).intersection(set(from_santa))
    print(intersection)
    min_len = 99999
    for a in intersection:
        len = from_you.index(a) + from_santa.index(a)
        if len < min_len:
            min_len = len


    # ans = min(from_you.index(a) + from_santa.index(a) for a in intersection)
    return min_len

def part_two():

    with open(DATA_FILE, "r") as f:
        input_data = f.read()

    # expected_orbit = return_orbit_part_two(input_data)
    # my_orbit = Orbits(expected_orbit)
    part_two = calculate_part_two(input_data)
    

    return part_two

ans = part_two()
print(ans)

#not51
# with open(DATA_FILE, "r") as f:
#     input_data = f.read()
# parent = defaultdict(str)

# for rel in input_data.split("\n"):
#     obj, orbit = rel.split(")")
#     parent[orbit] = obj


# def get_orbits(name):
#     while (name := parent[name]) :
#         yield name


# from_you = list(get_orbits("YOU"))
# from_san = list(get_orbits("SAN"))

# common = set(from_you).intersection(set(from_san))

# part_two = min(from_you.index(a) + from_san.index(a) for a in common)
# print(part_two)
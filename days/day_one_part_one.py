import sys
import os.path
import math 

ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'dayonepartone_data')
EXPECTED_LINES = 100


# basic fuel compution for day one part one
def compute_fuel(mass):
    div = mass / 3
    round  = math.floor(div)
    answer = round - 2 
    return answer

# more complex fuel compution for day one part two
def compute_fuel_recursive(mass):
    total_fuel = 0
    fuel = compute_fuel(mass)

    while fuel > 0:
        total_fuel += fuel
        fuel = compute_fuel(fuel)

    return total_fuel


def get_masses():
    masses_from_file = []
    with open(DATA_FILE) as fp:
        line = fp.readline()
        lines_read = 1
        while line:
            masses_from_file.append(int(line.strip()))
            line = fp.readline()
            lines_read += 1


    if (lines_read != EXPECTED_LINES + 1):
        sys.exit("Did not read the correct amount of lines")

    return masses_from_file

# day one part one
def compute_sum_fuel():

    masses = get_masses()
   
    fuel = []
    for mass in masses:
        fuel.append(compute_fuel(mass))

    sum_of_fuel = sum(fuel)
    return sum_of_fuel

print("Day One Part One: {}".format(compute_sum_fuel()))

def compute_sum_fuel_recursive():
    masses = get_masses()
    fuel = []
    for mass in masses:
        fuel.append(compute_fuel_recursive(mass))

    sum_of_fuel = sum(fuel)
    return sum_of_fuel


print("Day One Part Two: {}".format(compute_sum_fuel_recursive()))




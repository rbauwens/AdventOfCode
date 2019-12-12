import math 
from collections import defaultdict



def return_orbit(orbit):
    lines = orbit.split('\n')
    orbit_dict = defaultdict(list)
    for line in lines:
        focus = line.split(")")[0].strip()
        orbiter = line.split(")")[1].strip()
        
        orbit_dict[focus].append(orbiter)
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




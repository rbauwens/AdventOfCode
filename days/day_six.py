import math 

ORBITS = dict()

def get_orbit(orbit):
    focus = orbit.split(")")[0]
    orbiter = orbit.split(")")[1]
    if focus in ORBITS:
        ORBITS[focus].append(orbiter)
    else:
        ORBITS[focus] = [orbiter]


def num_orbits(focus, num_orbiters, end):
    if focus in ORBITS and end != 1:
        orbiters = ORBITS[focus]
        num_orbiters = num_orbiters + len(ORBITS[focus])
        new_orbits = 0
        for object in orbiters:
            new_orbits, end = num_orbits(object, num_orbiters, end)
            if end == 1:
                return num_orbiters, 1
        # num_orbiters = num_orbiters + new_orbits
    return num_orbiters, 1

def num_orbits1(orbits, focus, num_orb):
    # if focus not in orbits:
    #     return None
    # else:
    new = 0
    for tmp in orbits[focus]:
        num_orb = num_orb + 1
        if tmp not in orbits:
            return -999, num_orb
        while tmp in orbits and new != -999:
            new, num_orb = num_orbits1(orbits, tmp, num_orb)
            if new != -999:
                num_orb = num_orb + new
    return 0, num_orb


print(ORBITS)
get_orbit("A)B")
print(ORBITS)
get_orbit("B)C")
print(ORBITS)

values = []
for focus in ORBITS:
    print("focus: {}".format(focus))
    values.append(num_orbits(focus, 0, 0)[0])

print(values)
print(sum(values))


import unittest
from days.day_six import return_orbit, Orbits, calculate_part_one

class AddTests(unittest.TestCase):
   

    def test_four(self):
        list_one = " \
        COM)B\n \
        B)C\n \
        COM)D"

        expected_orbit = return_orbit(list_one)
        my_orbit = Orbits(expected_orbit)
        part_one = calculate_part_one(my_orbit)
        
        self.assertEqual(part_one, 4)

    def test_five(self):
        list_one = "COM)B\n\
B)C\n\
C)D\n\
D)E\n\
E)F\n\
B)G\n\
G)H\n\
D)I\n\
E)J\n\
J)K\n\
K)L"
        
        expected_orbit = return_orbit(list_one)
        my_orbit = Orbits(expected_orbit)
        part_one = calculate_part_one(my_orbit)
        # direct_count = my_orbit.count_direct("COM")
        # indirect_count = 0

        # for name in expected_orbit:
        #     if name != "COM":
        #         indirect_count += my_orbit.count_direct(name)

        # part_one = direct_count + indirect_count
        self.assertEqual(part_one, 42)

# def count_direct(name):
#     return len(d[name]) + sum(count_direct(n) for n in d[name])



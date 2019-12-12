import unittest
from days.day_six import return_orbit, Orbits, calculate_part_one, part_one, calculate_part_two, part_two

class AddTests(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(453028, part_one())
   
    def test_three(self):
        list_one = " \
        COM)21X\n \
        21X)BWV\n \
        COM)D"

        expected_orbit = return_orbit(list_one)
        my_orbit = Orbits(expected_orbit)
        part_one = calculate_part_one(my_orbit)
        
        self.assertEqual(part_one, 4)

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
        self.assertEqual(part_one, 42)



    def test_one(self):
        string1 = "COM)B\n\
B)C\n\
C)D\n\
D)E\n\
E)F\n\
B)G\n\
G)H\n\
D)I\n\
E)J\n\
J)K\n\
K)L\n\
K)YOU\n\
I)SAN"
        self.assertEqual(4, calculate_part_two(string1))
    
    def test_part_two(self):
        self.assertEquals(562, part_two())
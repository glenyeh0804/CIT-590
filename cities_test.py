import random
import unittest
from cities import *

class Testcities(unittest.TestCase):
    def test_compute_total_distance(self):
        # test the total distance
        city_list = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                     ('Alaska', 'Juneau', 58.301935, -134.41974),
                     ('Arizona', 'Phoenix', 33.448457, -112.073844),
                     ('Arkansas', 'Little Rock', 34.736009, -92.331122)]
        self.assertAlmostEqual(6368.5788737, compute_total_distance(city_list), 5)

    def test_swap_adjacent_cities(self):
        # swap test, index = 0
        city_list = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                     ('Alaska', 'Juneau', 58.301935, -134.41974),
                     ('Arizona', 'Phoenix', 33.448457, -112.073844),
                     ('Arkansas', 'Little Rock', 34.736009, -92.331122)]
        new_city_list = [('Alaska', 'Juneau', 58.301935, -134.41974),
                         ('Alabama', 'Montgomery', 32.361538, -86.279118),
                         ('Arizona', 'Phoenix', 33.448457, -112.073844),
                         ('Arkansas', 'Little Rock', 34.736009, -92.331122)]
        output = swap_adjacent_cities(city_list, 0)
        self.assertEqual(new_city_list, output[0])
        self.assertAlmostEqual(compute_total_distance(new_city_list), output[1], 5)

        # swap test, index = the end of the list
        city_list = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                     ('Alaska', 'Juneau', 58.301935, -134.41974),
                     ('Arizona', 'Phoenix', 33.448457, -112.073844),
                     ('Arkansas', 'Little Rock', 34.736009, -92.331122)]
        new2_city_list = [('Arkansas', 'Little Rock', 34.736009, -92.331122),
                          ('Alaska', 'Juneau', 58.301935, -134.41974),
                          ('Arizona', 'Phoenix', 33.448457, -112.073844),
                          ('Alabama', 'Montgomery', 32.361538, -86.279118)]
        output2 = swap_adjacent_cities(city_list, 3)
        self.assertEqual(new2_city_list, output2[0])
        self.assertAlmostEqual(compute_total_distance(new2_city_list), output2[1], 5)

    def test_swap_cities(self):

        # swap test, index1 = 0, index2 = 2
        city_list = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                     ('Alaska', 'Juneau', 58.301935, -134.41974),
                     ('Arizona', 'Phoenix', 33.448457, -112.073844),
                     ('Arkansas', 'Little Rock', 34.736009, -92.331122)]
        new_city_list = [('Arizona', 'Phoenix', 33.448457, -112.073844),
                         ('Alaska', 'Juneau', 58.301935, -134.41974),
                         ('Alabama', 'Montgomery', 32.361538, -86.279118),
                         ('Arkansas', 'Little Rock', 34.736009, -92.331122)]
        output = swap_cities(city_list, 0, 2)
        self.assertEqual(new_city_list, output[0])
        self.assertAlmostEqual(compute_total_distance(new_city_list), output[1], 5)

        # swap test, index1 = index2
        city_list = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                     ('Alaska', 'Juneau', 58.301935, -134.41974),
                     ('Arizona', 'Phoenix', 33.448457, -112.073844),
                     ('Arkansas', 'Little Rock', 34.736009, -92.331122)]
        output = swap_cities(city_list, 1, 1)
        self.assertEqual(city_list, output[0])
        self.assertAlmostEqual(compute_total_distance(city_list), output[1], 5)

    def test_find_best_cycle(self):
        # Check the function returns a valid road map, with no cities omitted or duplicated
        road_map = read_cities('city-data.txt')
        original_road_map = road_map[:]
        optimized_road_map = find_best_cycle(road_map)
        s1 = set(original_road_map)
        s2 = set(optimized_road_map)
        self.assertEqual(s1, s2)
        self.assertNotEqual(original_road_map, optimized_road_map)

        # Check the function returns an optimized map
        city_list = [('Alaska', 'Juneau', 58.301935, -134.41974),
                     ('Arkansas', 'Little Rock', 34.736009, -92.331122),
                     ('Alabama', 'Montgomery', 32.361538, -86.279118),
                    ('Arizona', 'Phoenix', 33.448457, -112.073844)]
        optimized_road_map = find_best_cycle(city_list)
        self.assertAlmostEqual(6368.578864, compute_total_distance(optimized_road_map), 2)


unittest.main()

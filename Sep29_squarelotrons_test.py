import unittest
import copy
from squarelotrons import *


flat_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
ori_squarelotron = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]]

class Testsquarelotrons(unittest.TestCase):

    def test_make_squarelotron(self):
        """Test whether the function can return a correct squarelotron based on the given list"""
        self.assertEqual(make_squarelotron(flat_list), [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]])

    def test_make_list(self):
        """Test whether the function can return a flat list based on the given squarelotron"""
        self.assertEqual(make_list(ori_squarelotron), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                                   15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

    def test_upside_down_flip(self):
        """Test whether the function can flip with the upside-down way"""
        self.assertEqual(upside_down_flip(ori_squarelotron, 'outer'),
                         [[21, 22, 23, 24, 25],
                         [16, 7, 8, 9, 20],
                         [11, 12, 13, 14, 15],
                         [6, 17, 18, 19, 10],
                         [1, 2, 3, 4, 5]])
        self.assertEqual(upside_down_flip(ori_squarelotron, 'inner'),
                         [[1, 2, 3, 4, 5],
                          [6, 17, 18, 19, 10],
                          [11, 12, 13, 14, 15],
                          [16, 7, 8, 9, 20],
                          [21, 22, 23, 24, 25]])

    def test_left_right_flip(self):
        """Test whether the function can flip with the left-right way"""
        self.assertEqual(left_right_flip(ori_squarelotron, 'outer'),
                         [[5, 4, 3, 2, 1],
                          [10, 7, 8, 9, 6],
                          [15, 12, 13, 14, 11],
                          [20, 17, 18, 19, 16],
                          [25, 24, 23, 22, 21]])
        self.assertEqual(left_right_flip(ori_squarelotron, 'inner'),
                         [[1, 2, 3, 4, 5],
                          [6, 9, 8, 7, 10],
                          [11, 14, 13, 12, 15],
                          [16, 19, 18, 17, 20],
                          [21, 22, 23, 24, 25]])

    def test_inverse_diagonal_flip(self):
        """Test whether the function can flip with the inverse-diagonal way"""
        self.assertEqual(inverse_diagonal_flip(ori_squarelotron, 'outer'),
                         [[25, 20, 15, 10, 5],
                          [24, 7, 8, 9, 4],
                          [23, 12, 13, 14, 3],
                          [22, 17, 18, 19, 2],
                          [21, 16, 11, 6, 1]])
        self.assertEqual(inverse_diagonal_flip(ori_squarelotron, 'inner'),
                         [[1, 2, 3, 4, 5],
                          [6, 19, 14, 9, 10],
                          [11, 18, 13, 8, 15],
                          [16, 17, 12, 7, 20],
                          [21, 22, 23, 24, 25]])

    def test_main_diagonal_flip(self):
        """Test whether the function can flip with the main-diagonal way"""
        self.assertEqual(main_diagonal_flip(ori_squarelotron, 'outer'),
                         [[1, 6, 11, 16, 21],
                         [2, 7, 8, 9, 22],
                         [3, 12, 13, 14, 23],
                         [4, 17, 18, 19, 24],
                         [5, 10, 15, 20, 25]])
        self.assertEqual(main_diagonal_flip(ori_squarelotron, 'inner'),
                         [[1, 2, 3, 4, 5],
                         [6, 7, 12, 17, 10],
                         [11, 8, 13, 18, 15],
                         [16, 9, 14, 19, 20],
                         [21, 22, 23, 24, 25]])

    def test_flip_decision(self):
        """Test whether the function can correctly flip with the given way"""
        self.assertEqual(flip_decision(ori_squarelotron, 'U', 'outer'), upside_down_flip(ori_squarelotron, 'outer'))
        self.assertEqual(flip_decision(ori_squarelotron, 'U', 'inner'), upside_down_flip(ori_squarelotron, 'inner'))
        self.assertEqual(flip_decision(ori_squarelotron, 'L', 'outer'), left_right_flip(ori_squarelotron, 'outer'))
        self.assertEqual(flip_decision(ori_squarelotron, 'L', 'inner'), left_right_flip(ori_squarelotron, 'inner'))
        self.assertEqual(flip_decision(ori_squarelotron, 'M', 'outer'), main_diagonal_flip(ori_squarelotron, 'outer'))
        self.assertEqual(flip_decision(ori_squarelotron, 'M', 'inner'), main_diagonal_flip(ori_squarelotron, 'inner'))
        self.assertEqual(flip_decision(ori_squarelotron, 'I', 'outer'),
                         inverse_diagonal_flip(ori_squarelotron, 'outer'))
        self.assertEqual(flip_decision(ori_squarelotron, 'I', 'inner'),
                         inverse_diagonal_flip(ori_squarelotron, 'inner'))

unittest.main()

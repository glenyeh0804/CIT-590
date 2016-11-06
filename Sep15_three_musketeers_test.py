import unittest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'


class TestThreeMusketeers(unittest.TestCase):
    def setUp(self):
        set_board([[_, _, _, M, _],
                   [_, _, R, M, _],
                   [_, R, M, R, _],
                   [_, R, _, _, _],
                   [_, _, _, R, _]])

    def test_create_board(self):
        create_board()
        self.assertEqual(at((0, 0)), 'R')
        self.assertEqual(at((0, 4)), 'M')

    def test_set_board(self):
        self.assertEqual(at((0, 0)), '-')
        self.assertEqual(at((1, 2)), 'R')
        self.assertEqual(at((1, 3)), 'M')

    def test_get_board(self):
        self.assertEqual([[_, _, _, M, _],
                          [_, _, R, M, _],
                          [_, R, M, R, _],
                          [_, R, _, _, _],
                          [_, _, _, R, _]],
                         get_board())

    def test_string_to_location(self):
        self.assertEqual(string_to_location('A5'), (0, 4))

    def test_location_to_string(self):
        location = (0, 4)
        self.assertEqual(location_to_string(location), 'A5')

    def test_at(self):
        self.assertEqual(at((0, 3)), 'M')
        self.assertEqual(at((1, 2)), 'R')
        self.assertEqual(at((4, 0)), '-')
        
    def test_all_locations(self):
        all_list = all_locations()
        self.assertEqual(all_list[5], (1, 0))
        self.assertEqual(all_list[23], (4, 3))

    def test_adjacent_location(self):
        location = (2, 1)
        self.assertEqual(adjacent_location(location, 'L'), (2, 0))
        location = (3, 2)
        self.assertEqual(adjacent_location(location, 'R'), (3, 3))
        location = (4, 1)
        self.assertEqual(adjacent_location(location, 'U'), (3, 1))
        location = (3, 3)
        self.assertEqual(adjacent_location(location, 'D'), (4, 3))

    def test_is_legal_move_by_musketeer(self):
        location = (0, 3)
        self.assertFalse(is_legal_move_by_musketeer(location, 'U'))
        self.assertFalse(is_legal_move_by_musketeer(location, 'D'))
        location = (1, 3)
        self.assertFalse(is_legal_move_by_musketeer(location, 'U'))
        self.assertTrue(is_legal_move_by_musketeer(location, 'D'))

    def test_is_legal_move_by_enemy(self):
        location = (4, 3)
        self.assertFalse(is_legal_move_by_enemy(location, 'D'))
        self.assertTrue(is_legal_move_by_enemy(location, 'R'))
        location = (1, 2)
        self.assertFalse(is_legal_move_by_enemy(location, 'R'))
        
    def test_is_legal_move(self):
        location = (2, 2)
        self.assertTrue(is_legal_move(location, 'R'))
        self.assertFalse(is_legal_move(location, 'D'))
        location = (3, 1)
        self.assertTrue(is_legal_move(location, 'D'))
        self.assertFalse(is_legal_move(location, 'U'))        

    def test_has_some_legal_move_somewhere(self):
        set_board([[_, _, _, M, _],
                   [_, R, _, M, _],
                   [_, _, M, _, R],
                   [_, R, _, _, _],
                   [_, _, _, R, _]])
        self.assertFalse(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))
        set_board([[_, _, _, _, _],
                   [_, _, _, _, M],
                   [_, _, _, M, R],
                   [_, _, _, _, M],
                   [_, _, _, _, _]])
        self.assertFalse(has_some_legal_move_somewhere('R'))
        self.assertTrue(has_some_legal_move_somewhere('M'))     
        set_board([[_, _, _, M, _],
                   [_, _, R, M, _],
                   [_, R, M, R, _],
                   [_, R, _, _, _],
                   [_, _, _, R, _]])
        self.assertTrue(has_some_legal_move_somewhere('R'))
        self.assertTrue(has_some_legal_move_somewhere('M')) 

    def test_possible_moves_from(self):
        location = (2, 2)
        self.assertEqual(possible_moves_from(location), ['up', 'left', 'right'])
        location = (3, 1)
        self.assertEqual(possible_moves_from(location), ['down', 'left', 'right'])
        location = (0, 3)
        self.assertEqual(possible_moves_from(location), [])
        location = (0, 0)
        self.assertEqual(possible_moves_from(location), [])

    def test_can_move_piece_at(self):
        set_board([[_, _, _, M, R],
                   [_, _, _, M, M],
                   [_, _, R, _, _],
                   [_, _, _, _, _],
                   [_, _, _, _, _]])
        location = (0, 3)
        self.assertTrue(can_move_piece_at(location))
        location = (2, 2)
        self.assertTrue(can_move_piece_at(location))
        location = (0, 4)
        self.assertFalse(can_move_piece_at(location))

    def test_is_legal_location(self):
        self.assertTrue(is_legal_location((3, 4)))
        self.assertFalse(is_legal_location((6, 3)))

    def test_is_within_board(self):
        self.assertTrue(is_within_board((0, 4), 'D'))
        self.assertFalse(is_within_board((0, 4), 'U'))

    def test_all_possible_moves_for(self):
        set_board([[_, _, R, M, R],
                   [_, _, _, M, M], 
                   [_, _, _, _, _],
                   [_, _, _, _, _],
                   [_, _, _, _, _]])
        
        self.assertEqual(all_possible_moves_for('R'), [((0, 2), 'down'), ((0, 2), 'left')])
        self.assertEqual(all_possible_moves_for('M'), [((0, 3), 'left'), ((0, 3), 'right'), ((1, 4), 'up')])

    def test_make_move(self):
        make_move((1, 3), 'L')
        self.assertEqual(at((1, 2)), 'M')
        self.assertEqual(at((1, 3)), '-')
        make_move((4, 3), 'R')
        self.assertEqual(at((4, 4)), 'R')
        self.assertEqual(at((4, 3)), '-')

    def test_choose_computer_move(self):
        option = choose_computer_move('M')
        self.assertEqual(option[0], (1, 3))
        self.assertEqual(option[1], 'left')
        option = choose_computer_move('R')
        self.assertEqual(option[0], (1, 2))
        self.assertEqual(option[1], 'left')

    def test_is_enemy_win(self):
        self.assertFalse(is_enemy_win())
        set_board([[_, _, R, R, R],
                   [_, M, _, M, M], 
                   [_, _, _, _, _],
                   [_, _, _, _, _],
                   [_, _, _, _, _]])
        self.assertTrue(is_enemy_win())
        set_board([[_, _, R, M, R],
                   [_, _, _, M, R], 
                   [_, _, _, _, _],
                   [_, _, _, _, _],
                   [_, _, _, M, _]])
        self.assertTrue(is_enemy_win())

unittest.main()

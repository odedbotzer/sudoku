import unittest
from sudoku.solver import solve_in_a_terrible_manner, NoSolutionException
from sudoku.verifier import MISSING_VAL


class TestSudokuSolver(unittest.TestCase):
    def test_null_case(self):
        board = [
            [1, 5, 2, 4, 8, 9, 3, 7, 6],
            [7, 3, 9, 2, 5, 6, 8, 4, 1],
            [4, 6, 8, 3, 7, 1, 2, 9, 5],
            [3, 8, 7, 1, 2, 4, 6, 5, 9],
            [5, 9, 1, 7, 6, 3, 4, 2, 8],
            [2, 4, 6, 8, 9, 5, 7, 1, 3],
            [9, 1, 4, 6, 3, 7, 5, 8, 2],
            [6, 2, 5, 9, 4, 8, 1, 3, 7],
            [8, 7, 3, 5, 1, 2, 9, 6, 4]
        ]
        self.assertEqual(solve_in_a_terrible_manner(board), board)

    def test_full_with_no_solution(self):
        self.assertRaises(NoSolutionException, solve_in_a_terrible_manner, [
            [1, 5, 2, 4, 8, 9, 3, 1, 1],
            [7, 3, 9, 2, 5, 6, 8, 1, 1],
            [4, 6, 8, 3, 7, 1, 2, 1, 1],
            [3, 8, 7, 1, 2, 4, 6, 1, 1],
            [5, 9, 1, 7, 6, 3, 4, 1, 1],
            [2, 4, 6, 8, 9, 5, 7, 1, 1],
            [9, 1, 4, 6, 3, 7, 5, 1, 1],
            [6, 2, 5, 9, 4, 8, 1, 1, 1],
            [8, 7, 3, 5, 1, 2, 9, 1, 1]
        ])

    def test_partial_with_no_solution(self):
        self.assertRaises(NoSolutionException, solve_in_a_terrible_manner, [
            [1, 5, 2, 4, 8, 9, 3, 1, 1],
            [7, 3, 9, 2, 5, 6, 8, 1, 1],
            [4, 6, 8, 3, 7, 1, 2, 1, 1],
            [3, 8, 7, 1, 2, 4, 6, 1, 1],
            [5, 9, 1, 7, 6, 3, 4, 1, 1],
            [2, 4, 6, 8, 9, 5, 7, 1, 1],
            [9, 1, 4, 6, 3, 7, 5, 1, 1],
            [6, 2, 5, 9, 4, 8, 1, 1, 1],
            [8, 7, 3, 5, 1, 2, 9, 1, MISSING_VAL]
        ])

    def test_simple_solution(self):
        solution = solve_in_a_terrible_manner([
            [1, 5, 2, 4, 8, 9, 3, 7, 6],
            [7, 3, 9, 2, 5, 6, 8, 4, 1],
            [4, 6, 8, 3, 7, 1, 2, 9, 5],
            [3, 8, 7, 1, 2, 4, 6, 5, 9],
            [5, 9, 1, 7, 6, 3, 4, 2, 8],
            [2, 4, 6, 8, 9, 5, 7, 1, 3],
            [9, 1, 4, 6, 3, 7, 5, 8, 2],
            [6, 2, 5, 9, 4, 8, 1, 3, 7],
            [8, 7, 3, 5, 1, 2, 9, 6, MISSING_VAL]
        ])

        self.assertListEqual(solution, [
            [1, 5, 2, 4, 8, 9, 3, 7, 6],
            [7, 3, 9, 2, 5, 6, 8, 4, 1],
            [4, 6, 8, 3, 7, 1, 2, 9, 5],
            [3, 8, 7, 1, 2, 4, 6, 5, 9],
            [5, 9, 1, 7, 6, 3, 4, 2, 8],
            [2, 4, 6, 8, 9, 5, 7, 1, 3],
            [9, 1, 4, 6, 3, 7, 5, 8, 2],
            [6, 2, 5, 9, 4, 8, 1, 3, 7],
            [8, 7, 3, 5, 1, 2, 9, 6, 4]
        ])

    def test_not_so_simple_solution(self):
        solution = solve_in_a_terrible_manner([
            [1, 5, 2, 4, 8, 9, 3, 7, 6],
            [7, 3, 9, MISSING_VAL, 5, 6, 8, 4, MISSING_VAL],
            [4, 6, 8, 3, 7, 1, MISSING_VAL, 9, 5],
            [3, 8, 7, 1, 2, 4, MISSING_VAL, 5, 9],
            [5, 9, 1, 7, 6, 3, MISSING_VAL, 2, 8],
            [2, 4, 6, 8, 9, 5, MISSING_VAL, 1, 3],
            [9, 1, 4, 6, 3, 7, 5, 8, 2],
            [6, 2, 5, 9, 4, 8, 1, 3, 7],
            [8, 7, 3, 5, 1, 2, 9, 6, 4]
        ])

        self.assertListEqual(solution, [
            [1, 5, 2, 4, 8, 9, 3, 7, 6],
            [7, 3, 9, 2, 5, 6, 8, 4, 1],
            [4, 6, 8, 3, 7, 1, 2, 9, 5],
            [3, 8, 7, 1, 2, 4, 6, 5, 9],
            [5, 9, 1, 7, 6, 3, 4, 2, 8],
            [2, 4, 6, 8, 9, 5, 7, 1, 3],
            [9, 1, 4, 6, 3, 7, 5, 8, 2],
            [6, 2, 5, 9, 4, 8, 1, 3, 7],
            [8, 7, 3, 5, 1, 2, 9, 6, 4]
        ])


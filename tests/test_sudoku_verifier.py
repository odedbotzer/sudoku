import unittest

from sudoku.verifier import verify, InvalidBoardFormatException, validate_sudoku_format, MISSING_VAL


class TestSudokuVerifier(unittest.TestCase):

    def test_partial_board_valid_format(self):
        validate_sudoku_format([
            [1, 5, 2, 4, 8, 9, 3, 7, 6],
            [7, 3, 9, 2, 5, 6, 8, 4, 1],
            [4, 6, 8, 3, 7, 1, 2, 9, 5],
            [3, 8, 7, 1, 2, 4, 6, 5, 9],
            [5, 9, 1, 7, 6, 3, 4, 2, 8],
            [2, 4, 6, 8, 9, 5, 7, 1, 3],
            [9, 1, 4, 6, 3, 7, 5, 8, 2],
            [6, 2, 5, 9, 4, 8, 1, 3, 7],
            [8, 7, 3, 5, 1, 2, 9, 6, MISSING_VAL]
        ], partial_board=True)

    def test_partial_board_wrong_key(self):
        self.assertRaises(InvalidBoardFormatException, validate_sudoku_format, [
            [1, 5, 2, 4, 8, 9, 3, 7, 6],
            [7, 3, 9, 2, 5, 6, 8, 4, 1],
            [4, 6, 8, 3, 7, 1, 2, 9, 5],
            [3, 8, 7, 1, 2, 4, 6, 5, 9],
            [5, 9, 1, 7, 6, 3, 4, 2, 8],
            [2, 4, 6, 8, 9, 5, 7, 1, 3],
            [9, 1, 4, 6, 3, 7, 5, 8, 2],
            [6, 2, 5, 9, 4, 8, 1, 3, 7],
            [8, 7, 3, 5, 1, 2, 9, 6, '']
        ], partial_board=True)

    def test_board_format_exception(self):
        self.assertRaises(InvalidBoardFormatException, validate_sudoku_format, [
            [1, 5, 2, 4, 8, 9, 3, 7, 6],
            [7, 3, 9, 2, 5, 6, 8, 4, 1],
            [4, 6, 8, 3, 7, 1, 2, 9, 5],
            [3, 8, 7, 1, 2, 4, 6, 5, 9],
            [5, 9, 1, 7, 6, 3, 4, 2, 8],
            [2, 4, 6, 8, 9, 5, 7, 1, 3],
            [9, 1, 4, 6, 3, 7, 5, 8, 2],
            [6, 2, 5, 9, 4, 8, 1, 3, 7],
            [8, 7, 3, 5, 1, 2, 9, 6]
        ])

    def test_board_format_exception2(self):
        self.assertRaises(InvalidBoardFormatException, validate_sudoku_format, [
            [1, 5, 2, 4, 8, 9, 3, 7, 6],
            [7, 3, 9, 2, 5, 6, 8, 4, 1],
            [4, 6, 8, 3, 7, 1, 2, 9, 5],
            [3, 8, 7, 1, 2, 4, 6, 5, 9],
            [5, 9, 1, 7, 6, 3, 4, 2, 8],
            [2, 4, 6, 8, 9, 5, 7, 1, 3]
        ])

    def test_correct_board(self):
        self.assertTrue(verify([
            [1, 5, 2, 4, 8, 9, 3, 7, 6],
            [7, 3, 9, 2, 5, 6, 8, 4, 1],
            [4, 6, 8, 3, 7, 1, 2, 9, 5],
            [3, 8, 7, 1, 2, 4, 6, 5, 9],
            [5, 9, 1, 7, 6, 3, 4, 2, 8],
            [2, 4, 6, 8, 9, 5, 7, 1, 3],
            [9, 1, 4, 6, 3, 7, 5, 8, 2],
            [6, 2, 5, 9, 4, 8, 1, 3, 7],
            [8, 7, 3, 5, 1, 2, 9, 6, 4]
        ]))

    def test_incorrect_board(self):
        self.assertFalse(verify([
            [1, 1, 2, 4, 8, 9, 3, 7, 6],
            [7, 3, 9, 2, 5, 6, 8, 4, 1],
            [4, 6, 8, 3, 7, 1, 2, 9, 5],
            [3, 8, 7, 1, 2, 4, 6, 5, 9],
            [5, 9, 1, 7, 6, 3, 4, 2, 8],
            [2, 4, 6, 8, 9, 5, 7, 1, 3],
            [9, 1, 4, 6, 3, 7, 5, 8, 2],
            [6, 2, 5, 9, 4, 8, 1, 3, 7],
            [8, 7, 3, 5, 1, 2, 9, 6, 4]
        ]))

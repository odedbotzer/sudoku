from itertools import chain
from typing import List

from sudoku.verifier import validate_sudoku_format, verify, MISSING_VAL


def solve_in_a_terrible_manner(board: List[List[int]]) -> List[List[int]]:
    validate_sudoku_format(board, partial_board=True)
    successful, solution = _recursive_solver(board)
    if not successful:
        raise NoSolutionException
    return solution


def _recursive_solver(board: List[List[int]]) -> (bool, List[List[int]]):
    not_found = -1
    flattened = chain.from_iterable(board)
    first_missing_ind = next((ind for (ind, val) in enumerate(flattened) if val is MISSING_VAL), not_found)
    if first_missing_ind is not_found:
        return verify(board), board
    else:
        i, j = (first_missing_ind // 9), (first_missing_ind % 9)
        return _naive_fill_and_recurse(board, i, j)


def _naive_fill_and_recurse(board: List[List[int]], i, j) -> (bool, List[List[int]]):
    for candidate in range(1, 10):
        board[i][j] = candidate
        successful, solution = _recursive_solver(board)
        if successful:
            return True, solution
    board[i][j] = MISSING_VAL
    return False, []


class NoSolutionException(Exception):
    pass

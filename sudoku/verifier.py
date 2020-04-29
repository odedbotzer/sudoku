from itertools import chain
from itertools import combinations_with_replacement as combinations
from typing import Sequence, List, Any, Generator

ALLOWED_VALUES = set(range(1, 10))
MISSING_VAL = None


def validate_sudoku_format(board, partial_board: bool = False) -> None:
    if not (isinstance(board, list) and len(board) == 9 and all(_valid_row(row, partial_board) for row in board)):
        raise InvalidBoardFormatException


def _valid_row(row, partial_board: bool) -> bool:
    def valid_value(val) -> bool:
        return (val in ALLOWED_VALUES) or (partial_board and (val is MISSING_VAL))

    return isinstance(row, list) and len(row) == 9 and all(valid_value(val) for val in row)


def verify(board: List[List[int]]) -> bool:
    validate_sudoku_format(board)
    return _rows_valid(board) and _cols_valid(board) and _subsquares_valid(board)


def _basic_seq_valid(seq: Sequence[int]) -> bool:
    return list(sorted(seq)) == list(range(1, 10))


def _rows_valid(board: List[List[int]]) -> bool:
    return all(_basic_seq_valid(row) for row in board)


def _cols_valid(board: List[List[int]]) -> bool:
    cols = (list(rows_zipper) for rows_zipper in zip(*board))
    return all(_basic_seq_valid(col) for col in cols)


def _subsquares_valid(board: List[List[int]]) -> bool:
    for i, j in combinations(iterable=[0, 3, 6], r=2):
        subsquare = list(chain.from_iterable(row[j:j + 3] for row in board[i:i + 3]))
        if not _basic_seq_valid(subsquare):
            return False
    return True


class InvalidBoardFormatException(Exception):
    pass

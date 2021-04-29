from typing import List
from unittest import TestCase


class Solution:
    def __init__(self):
        self.board = []
        self.unfilled_cells = []

    def get_possibilities(self, line, column) -> List[str]:
        blockers = set()
        start_line = line - line % 3
        start_column = column - column % 3
        for i in range(9):
            blockers.add(self.board[line][i])
            blockers.add(self.board[i][column])
            c = self.board[start_line + i // 3][start_column + i % 3]
            blockers.add(c)
        result = []
        for i in range(1, 10):
            c = chr(48 + i)  # ascii('0') = 48
            if c not in blockers:
                result.append(c)
        return result

    def solve(self, unfilled_idx) -> bool:
        if len(self.unfilled_cells) == unfilled_idx:
            return True
        (line, column) = self.unfilled_cells[unfilled_idx]
        assert self.board[line][column] == '.'
        possible_nrs = self.get_possibilities(line, column)
        for c in possible_nrs:
            self.board[line][column] = c
            if self.solve(unfilled_idx + 1):
                return True
        self.board[line][column] = '.'

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.unfilled_cells = []
        for idx_line in range(len(board)):
            line = board[idx_line]
            for idx_column in range(len(line)):
                if line[idx_column] == '.':
                    self.unfilled_cells.append((idx_line, idx_column))
        self.solve(0)


class SudokuSolverTest(TestCase):
    def test_solve_sudoku(self):
        sol = Solution()
        expected = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                    ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                    ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                    ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        sol.solveSudoku(board)
        self.assertEqual(expected, board)

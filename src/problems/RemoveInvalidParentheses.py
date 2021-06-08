import numpy as np


class Solution:
    def __init__(self):
        self.solutions = ['']
        self.min_removed_chars = 0
        self.take_index = []
        self.s = ''

    def build_current_sol(self) -> str:
        s = ''
        for i in range(len(self.take_index)):
            if self.take_index[i]:
                s += self.s[i]
        return s

    def back(self, index: int, open_parentheses: int, removed_chars: int):
        if index == len(self.s):
            if open_parentheses == 0:
                if self.min_removed_chars > removed_chars:
                    self.min_removed_chars = removed_chars
                    self.solutions = [self.build_current_sol()]
                elif self.min_removed_chars == removed_chars:
                    self.solutions.append(self.build_current_sol())
            return

        is_char = False
        if self.s[index] == ')':
            if open_parentheses > 0:
                self.take_index[index] = True
                self.back(index + 1, open_parentheses - 1, removed_chars)
        elif self.s[index] == '(':
            self.take_index[index] = True
            self.back(index + 1, open_parentheses + 1, removed_chars)
        else:
            self.take_index[index] = True
            is_char = True
            self.back(index + 1, open_parentheses, removed_chars)

        if not is_char and self.min_removed_chars > removed_chars and open_parentheses < len(self.s) - index:
            self.take_index[index] = False
            self.back(index + 1, open_parentheses, removed_chars + 1)

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.s = s
        self.take_index = [False] * len(s)
        self.min_removed_chars = len(s)
        self.back(0, 0, 0)
        return np.unique(self.solutions)

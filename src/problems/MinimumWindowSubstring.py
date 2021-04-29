from unittest import TestCase


class Solution:
    def __init__(self):
        self.occurrences = {}
        self.occurrences_count = 0
        self.occurred = {}
        self.occurred_count = 0
        self.best_left = -1
        self.best_right = -1

    def add_char(self, c: chr):
        if c in self.occurrences:
            increase_count = True
            if c in self.occurred:
                if self.occurred[c] >= self.occurrences[c]:
                    increase_count = False
                self.occurred[c] += 1
            else:
                self.occurred[c] = 1
            if increase_count:
                self.occurred_count += 1

    def remove_char(self, c: chr):
        if c in self.occurrences:
            decrease_count = True
            assert self.occurred[c] > 0
            if self.occurred[c] > self.occurrences[c]:
                decrease_count = False
            self.occurred[c] -= 1
            if decrease_count:
                self.occurred_count -= 1

    def contains_all(self) -> bool:
        assert self.occurred_count <= self.occurrences_count
        return self.occurred_count == self.occurrences_count

    def add_solution(self, left, right):
        assert 0 <= left < right
        if self.best_right == -1 or self.best_left == -1 or right - left < self.best_right - self.best_left:
            self.best_left = left
            self.best_right = right

    def initialize_new_test(self, t_length):
        self.occurrences = {}
        self.occurrences_count = t_length
        self.occurred = {}
        self.occurred_count = 0
        self.best_left = -1
        self.best_right = -1

    def get_best_solution(self, s: str) -> str:
        return '' if self.best_left == -1 or self.best_right == -1 else \
            (s[self.best_left: self.best_right] if self.best_right <= len(s) else s[self.best_left:])

    def minWindow(self, s: str, t: str) -> str:
        assert len(s) > 0 and len(t) > 0
        self.initialize_new_test(len(t))
        for c in t:
            if c in self.occurrences:
                self.occurrences[c] += 1
            else:
                self.occurrences[c] = 1
        left = 0
        right = 0
        while left < len(s):
            self.add_char(s[right])
            right += 1
            while self.contains_all():
                self.add_solution(left, right)
                self.remove_char(s[left])
                left += 1
            if right == len(s):
                break
        return self.get_best_solution(s)


class MinimumWindowSubstringTest(TestCase):
    def test_min_window(self):
        tests = [
            (('ADOBECODEBANC', 'ABC'), 'BANC'),
            (('a', 'a'), 'a'),
            (('abcdef', 'g'), ''),
        ]
        sol = Solution()
        for test in tests:
            self.assertEqual(test[1], sol.minWindow(test[0][0], test[0][1]))

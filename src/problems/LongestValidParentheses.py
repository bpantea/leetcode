import unittest


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        last_index = [None] * len(s)
        all_time_best = -1
        current_value = 0
        for i in range(len(s)):
            if s[i] == '(':
                current_value += 1
                if last_index[current_value % len(s)] is None:
                    last_index[current_value % len(s)] = i
            else:
                last_index[(current_value + 1) % len(s)] = None
                current_value -= 1
                prev_ind = last_index[(current_value + 1) % len(s)]
                if prev_ind is not None:
                    current_best = i - prev_ind
                    all_time_best = max(all_time_best, current_best)
        return all_time_best + 1


class LongestValidParenthesesTest(unittest.TestCase):
    def test_longest_valid_parentheses(self):
        solution = Solution()
        self.assertEqual(2, solution.longestValidParentheses('(()'))
        self.assertEqual(4, solution.longestValidParentheses(')()())'))
        self.assertEqual(0, solution.longestValidParentheses(''))
        self.assertEqual(0, solution.longestValidParentheses('('))

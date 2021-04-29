from unittest import TestCase


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        d = [[1] * (len(s) + 1), [0] * (len(s) + 1)]
        cur_j = 0
        for j in range(len(t)):
            if cur_j == 0:
                cur_j = 1
                prev_j = 0
            else:
                cur_j = 0
                prev_j = 1
            d[cur_j][-1] = 0
            for i in range(len(s)):
                d[cur_j][i] = d[cur_j][i - 1] + (d[prev_j][i - 1] if s[i] == t[j] else 0)
        return d[cur_j][len(s) - 1]


class DistinctSubsequences(TestCase):
    def test_num_distinct(self):
        sol = Solution()
        tests = [
            ('rabbbit', 'rabbit', 3),
            ('babgbag', 'bag', 5)
        ]
        # d = [
        #
        #
        for test in tests:
            self.assertEqual(test[2], sol.numDistinct(test[0], test[1]))

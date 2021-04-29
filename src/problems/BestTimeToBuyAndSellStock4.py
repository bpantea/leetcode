from typing import List
from unittest import TestCase


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
        d = [[None] * k, [None] * k]
        for price in prices:
            for j in reversed(range(1, k)):
                if d[0][j] is not None:
                    if d[1][j] is None or d[0][j] + price > d[1][j]:
                        d[1][j] = d[0][j] + price
                if d[1][j - 1] is not None:
                    if d[0][j] is None or d[1][j - 1] - price > d[0][j]:
                        d[0][j] = d[1][j - 1] - price
            if d[0][0] is not None:
                if d[1][0] is None or d[0][0] + price > d[1][0]:
                    d[1][0] = d[0][0] + price
            if d[0][0] is None or -price > d[0][0]:
                d[0][0] = -price

        best = 0
        for i in range(k):
            if d[1][i] is not None and d[1][i] > best:
                best = d[1][i]
        return best


class BestTimeToBuyAndSellStock4Test(TestCase):
    def test_max_profit(self):
        tests = [
            ([2, 4, 1], 2, 2),
            ([3, 2, 6, 5, 0, 3], 2, 7),
        ]
        sol = Solution()
        for test in tests:
            self.assertEqual(test[2], sol.maxProfit(test[1], test[0]))

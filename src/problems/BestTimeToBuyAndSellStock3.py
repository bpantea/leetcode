from typing import List
from unittest import TestCase


class Solution:
    def maxProfitk(self, k: int, prices: List[int]) -> int:
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

    def maxProfit(self, prices: List[int]) -> int:
        first_buy = None
        first_sell = None
        second_buy = None
        second_sell = None
        for price in prices:
            if second_buy is not None and (second_sell is None or second_buy + price > second_sell):
                second_sell = second_buy + price
            if first_sell is not None and (second_buy is None or first_sell - price > second_buy):
                second_buy = first_sell - price
            if first_buy is not None and (first_sell is None or first_buy + price > first_sell):
                first_sell = first_buy + price
            if first_buy is None or -price > first_buy:
                first_buy = -price
        best = 0
        if first_sell is not None and first_sell > best:
            best = first_sell
        if second_sell is not None and second_sell > best:
            best = second_sell
        return best


class BestTimeToBuyAndSellStock3Test(TestCase):
    def test_max_profit(self):
        tests = [
            ([3, 3, 5, 0, 0, 3, 1, 4], 6),
            ([1, 2, 3, 4, 5], 4),
            ([1], 0),
        ]
        sol = Solution()
        for test in tests:
            self.assertEqual(test[1], sol.maxProfitk(2, test[0]))

from typing import List
from unittest import TestCase


class Solution:
    def candy(self, ratings: List[int]) -> int:
        sol = len(ratings)
        descending, ascending = 0, 0
        previous = ratings[0]
        previous_top_ascending = 0
        for r in ratings:
            if r < previous:
                sol += descending
                if descending < previous_top_ascending:
                    sol -= 1
                descending += 1
                ascending = 1
            elif r > previous:
                sol += ascending
                ascending += 1
                descending = 1
                previous_top_ascending = ascending
            else:
                previous_top_ascending = 0
                ascending = 1
                descending = 1
            previous = r
        return sol


class CandyTest(TestCase):
    def test_candy(self):
        sol = Solution()
        tests = [
            ([1, 0, 2], 5),
            ([1, 2, 3, 4, 3, 2], 13),
            ([1, 3, 2, 2, 1], 7),
            ([1, 2, 87, 87, 87, 2, 1], 13),
            ([1, 2, 2], 4)
        ]
        for test in tests:
            self.assertEqual(test[1], sol.candy(test[0]))

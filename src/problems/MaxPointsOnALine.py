import math
from typing import List
from unittest import TestCase


def get_radiant(p1, p2) -> tuple[int, int]:
    diff = p2[0] - p1[0], p2[1] - p1[1]
    assert diff[0] != 0 or diff[1] != 0
    if diff[0] == 0:
        return 0, 1
    if diff[1] == 0:
        return 1, 0
    divider = math.gcd(abs(diff[0]), abs(diff[1]))
    if diff[0] > 0:
        return diff[0] // divider, diff[1] // divider
    return - diff[0] // divider, - diff[1] // divider


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        points = [(x[0], x[1]) for x in points]
        best = 0
        for i in range(len(points)):
            p1 = points[i]
            radiant_map = {}
            for j in range(i + 1, len(points)):
                p2 = points[j]
                radiant = get_radiant(p1, p2)
                radiant_map[radiant] = radiant_map.get(radiant, 1) + 1
                best = max(best, radiant_map[radiant])
        return best


class MaxPointsOnALineTest(TestCase):
    def test_max_points(self):
        sol = Solution()
        tests = [
            ([[1, 1], [2, 2], [3, 3]], 3),
            ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4),
            ([[3, 3], [1, 4], [1, 1], [2, 1], [2, 2]], 3),
            ([[0, 0], [1, 1], [1, 2], [2, 3]], 2)
        ]
        for test in tests:
            self.assertEqual(test[1], sol.maxPoints(test[0]))

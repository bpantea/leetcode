from unittest import TestCase


def minim(a: int, b: int, c: int) -> int:
    if a <= b and a <= c:
        return a
    if b <= c:
        return b
    return c


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return len(word1) + len(word2)

        d = [[i for i in range(len(word2) + 1)], [i for i in range(len(word2) + 1)]]
        i0 = 1
        for i in range(len(word1)):
            if i0 > 0:
                i0 = 0
                i1 = 1
            else:
                i0 = 1
                i1 = 0
            d[i1][0] = i + 1
            for j in range(len(word2)):
                d[i1][j + 1] = (minim(d[i1][j] + 1, d[i0][j + 1] + 1, d[i0][j] + (1 if word1[i] != word2[j] else 0)))
        return d[i1][len(word2)]


class EditDistanceTest(TestCase):
    def test_min_distance(self):
        sol = Solution()
        tests = [
            (("horse", "ros"), 3),
            (("intention", "execution"), 5),
            (("b", ""), 1),
            (("b", "b"), 0),
        ]
        for test in tests:
            self.assertEqual(test[1], sol.minDistance(test[0][0], test[0][1]))

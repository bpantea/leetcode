from unittest import TestCase


def get_ones_from_n(x) -> int:
    sol = 0
    while x > 0:
        if x % 10 == 1:
            sol += 1
        x /= 10
    return sol


class Solution:
    def __init__(self):
        self.conters = {}

    def countDigitOne(self, n: int) -> int:
        top = n // 10 * 10
        self.preprocess(top)
        sol = 0
        while n > 9:
            close = n // 10 * 10
            sol += (n // close) * self.conters[close]
            n %= close

        return sol + 1

    def preprocess(self, x):
        i = 10
        prev = 0
        while i <= x:
            prev = prev * 10 + 1
            self.conters[i] = prev
            i *= 10


class NumberOfDigitOneTest(TestCase):
    def test_digit(self):

        tests = [
            (13, 6),
            (0, 0)
        ]
        for test in tests:
            self.assertEqual(test[1], Solution().countDigitOne(test[0]))

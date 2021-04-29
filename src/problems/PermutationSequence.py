from unittest import TestCase


class Solution:
    def __init__(self):
        self.factorial_calculated = 1
        self.factorial = [1, 1]

    def get_factorial(self, n) -> int:
        if n > self.factorial_calculated:
            for i in range(self.factorial_calculated + 1, n + 1):
                self.factorial.append(self.factorial[i - 1] * i)
            self.factorial_calculated = n
        return self.factorial[n]

    def getPermutation(self, n: int, k: int) -> str:
        available_nrs = [i for i in range(1, n + 1)]
        k -= 1
        sol = 0
        while n > 0:
            n -= 1
            fact = self.get_factorial(n)
            digit = available_nrs.pop(k // fact)
            sol = sol * 10 + digit
            k = k % fact
        return str(sol)


class PermutationSequenceTest(TestCase):
    def test_get_permutation(self):
        sol = Solution()
        self.assertEqual('213', sol.getPermutation(3, 3))
        self.assertEqual('2314', sol.getPermutation(4, 9))
        self.assertEqual('123', sol.getPermutation(3, 1))

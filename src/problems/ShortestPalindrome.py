from unittest import TestCase


def is_palindrome(s: str) -> bool:
    mid = len(s) // 2
    for i in range(mid):
        if s[i] != s[-i - 1]:
            return False
    return True


class Solution:
    def __init__(self):
        self.left = {}
        self.right = {}
        self.left_cnt = 0
        self.right_cnt = 0

    def add_to_left(self, c: chr):
        self.left[c] = self.left.get(c, 0) + 1
        self.left_cnt += 1

    def add_to_right(self, c: chr):
        self.right[c] = self.right.get(c, 0) + 1
        left_c_cnt = self.left.get(c, 0)
        if self.right[c] <= left_c_cnt:
            self.right_cnt += 1

    def remove_from_left(self, c: chr):
        assert self.left[c] > 0
        self.left[c] -= 1
        self.left_cnt -= 1
        right_c_cnt = self.right.get(c, 0)
        if self.left[c] < right_c_cnt:
            self.right_cnt -= 1

    def remove_from_right(self, c: chr):
        assert self.right[c] > 0
        self.right[c] -= 1
        left_c_cnt = self.left.get(c, 0)
        if self.right[c] < left_c_cnt:
            self.right_cnt -= 1

    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        mid = len(s) // 2
        for c in s[:mid]:
            self.add_to_left(c)
        if len(s) % 2 == 0:
            right_mid = mid
        else:
            right_mid = mid + 1
        for c in s[right_mid:]:
            self.add_to_right(c)
        for i in reversed(range(len(s))):
            if self.left_cnt == self.right_cnt and is_palindrome(s[:i + 1]):
                rev_s = s[i + 1:]
                return rev_s[::-1] + s

            mid = i // 2
            if i % 2 == 1:
                self.remove_from_left(s[mid])

            self.remove_from_right(s[i])
            if i % 2 == 0:
                self.add_to_right(s[mid])
        raise Exception('')


class ShortestPalindromeTest(TestCase):
    def test_shortest_palindrome(self):
        tests = [
            ('aacecaaa', 'aaacecaaa'),
            ('', ''),
            ('abcd', 'dcbabcd'),
            ('aabvbaa', 'aabvbaa'),
            ('aabvvbaa', 'aabvvbaa'),
            ("abb", "bbabb"),
        ]
        for test in tests:
            self.assertEqual(test[1], Solution().shortestPalindrome(test[0]))

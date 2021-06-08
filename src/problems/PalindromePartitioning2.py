from unittest import TestCase


def is_palindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


class Solution:
    def minCut(self, s: str) -> int:
        d = [x for x in range(len(s) + 1)]
        d[-1] = -1
        for i in range(1, len(s)):
            br_odd = False
            br_even = False
            for j in range(1, min(i + 1, len(s) - i)):
                left = i - j
                current_partitions = d[left - 1] + 1
                right_odd = i + j
                right_even = right_odd - 1
                if s[left] != s[right_odd]:
                    br_odd = True
                elif not br_odd:
                    d[right_odd] = min(d[right_odd], current_partitions)
                if s[left] != s[right_even]:
                    br_even = True
                elif not br_even:
                    d[right_even] = min(d[right_even], current_partitions)
                if br_odd and br_even:
                    break
            d[i] = min(d[i], d[i - 1] + 1)  # extra case for odd
            if not br_even and len(s) - i < i + 1:  # extra case for even
                j = len(s) - i
                if s[i - j] == s[i + j - 1]:
                    d[i + j - 1] = min(d[i + j - 1], d[i - j - 1] + 1)

        return d[len(s) - 1]


class PalindromePartitioning2Test(TestCase):
    def test_min_cut(self):
        sol = Solution()
        tests = [
            ("abbab", 1),
            ('aaabbbaaaaaaaaaaaaaaaaaaa', 1),
            ('aab', 1),
            ('a', 0),
            ('ab', 1),
            (
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            1)
        ]
        for test in tests:
            self.assertEqual(test[1], sol.minCut(test[0]))

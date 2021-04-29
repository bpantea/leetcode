from unittest import TestCase


def matching(c: chr, p: chr) -> bool:
    if p == '?':
        return True
    return c == p


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        d = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        d[-1][-1] = True
        for j in range(len(p)):
            if p[j] != '*':
                break
            d[-1][j] = True
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == '*':
                    d[i][j] = d[i - 1][j - 1] or d[i - 1][j] or d[i][j - 1]
                else:
                    d[i][j] = d[i - 1][j - 1] and matching(s[i], p[j])
        return d[len(s) - 1][len(p) - 1]


class WildcardMatchingTest(TestCase):
    def test_is_match(self):
        sol = Solution()
        self.assertEqual(False, sol.isMatch('aa', 'a'))
        self.assertEqual(True, sol.isMatch('aa', '*'))
        self.assertEqual(False, sol.isMatch('cb', '?a'))
        self.assertEqual(True, sol.isMatch('adceb', '*a*b'))
        self.assertEqual(False, sol.isMatch('acdcb', 'a*c?b'))
        self.assertEqual(True, sol.isMatch('', '*******'))
        self.assertEqual(True, sol.isMatch('abcabczzzde', '*abc???de*'))
        self.assertEqual(True, sol.isMatch('ho', '**ho'))
        self.assertEqual(False, sol.isMatch('zacabz', '*a?b*'))

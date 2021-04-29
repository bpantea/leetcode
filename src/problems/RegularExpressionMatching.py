from unittest import TestCase


def simple_char_match(c, p):
    return c == p or p == '.'


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        d = [[False] * (len(p) + 1) for x in range(len(s) + 1)]
        d[-1][-1] = True
        for j in range(0, len(p) - 1, 2):
            if p[j + 1] != '*':
                break
            d[-1][j + 1] = True
        if len(s) == 0:
            if len(p) % 2 != 0:
                return False
            for j in range(0, len(p) - 1, 2):
                if p[j + 1] != '*':
                    return False
            return True
        for i in range(len(s)):
            for j in range(len(p)):
                if j < len(p) - 1 and p[j + 1] == '*':
                    continue
                if p[j] == '*':
                    matching_char = simple_char_match(s[i], p[j - 1])
                    d[i][j] = (d[i - 1][j - 2] or d[i - 1][j]) and matching_char or (d[i][j - 2])
                elif not d[i - 1][j - 1]:
                    continue
                else:
                    d[i][j] = simple_char_match(s[i], p[j])
        return d[len(s) - 1][len(p) - 1]


class TestSolution(TestCase):
    def test_is_match(self):
        tests = {
            ('aa', 'a'): False,
            ('aa', 'a*'): True,
            ('ab', '.*'): True,
            ('aab', 'c*a*b'): True,
            ('mississippi', 'mis*is*p*.'): False,
            ('mississippi', 'mis*is*ip*.'): True,
        }
        solution = Solution()
        self.assertEqual(False, solution.isMatch("abc", "abca"))
        self.assertEqual(False, solution.isMatch("abc", "aaa"))
        self.assertEqual(False, solution.isMatch("aaaa", "aaa"))
        self.assertEqual(True, solution.isMatch("aaaa", "aaaa"))
        self.assertEqual(False, solution.isMatch("aaaa", "aaaaa"))
        self.assertEqual(False, solution.isMatch("aaaa", "aaba"))
        self.assertEqual(False, solution.isMatch("aaaa", "aaaaa"))
        #
        self.assertEqual(False, solution.isMatch("abc", "b*c*"))
        self.assertEqual(True, solution.isMatch("abbc", "ab*c"))
        self.assertEqual(True, solution.isMatch("abbc", "a*b*c"))
        self.assertEqual(False, solution.isMatch("abbc", "d*b*c"))
        self.assertEqual(True, solution.isMatch("abbc", ".*b*c"))
        self.assertEqual(True, solution.isMatch("abbc", "d*ab*c*"))
        self.assertEqual(True, solution.isMatch("aaa", "ab*ac*a"))
        self.assertEqual(True, solution.isMatch("", "c*c*"))
        self.assertEqual(True, solution.isMatch("aaabaaaababcbccbaab", "c*c*.*c*a*..*c*"))
        self.assertEqual(True, solution.isMatch("aaa", "c*c*.*c*a*"))
        for test in tests:
            expected_result = tests[test]
            self.assertEqual(expected_result, solution.isMatch(test[0], test[1]))

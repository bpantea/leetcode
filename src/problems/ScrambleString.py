from unittest import TestCase


class Solution:
    def __init__(self):
        self.d = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        case = (s1, s2)
        if case in self.d:
            return self.d[case]
        lt = len(s1)
        if lt == 1:
            return s1 == s2
        letter_counter = [0] * 26
        for i in range(lt):
            letter_counter[ord(s1[i]) - 97] += 1
            letter_counter[ord(s2[i]) - 97] -= 1
        for i in range(26):
            if letter_counter[i] != 0:
                self.d[case] = False
                return False

        for i in range(1, lt):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) \
                    or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                self.d[case] = True
                return True
        self.d[case] = False
        return False


class ScrambleStringTest(TestCase):
    def test_is_scramble(self):
        sol = Solution()
        tests = [
            ('great', 'rgeat', True),
            ('abcde', 'caebd', False),
            ('a', 'a', True),
            ('abcdefghijklmnopq', 'efghijklmnopqcadb', False),
            ('eebaacbcbcadaaedceaaacadccd', 'eadcaacabaddaceacbceaabeccd', False)
        ]
        for test in tests:
            self.assertEqual(test[2], sol.isScramble(test[0], test[1]))

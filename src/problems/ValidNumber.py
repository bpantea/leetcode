from unittest import TestCase


def count_chars(s: str, chars: str) -> int:
    cnt = 0
    for c in s:
        if c in chars:
            cnt += 1
    return cnt


def is_digit(c: chr) -> bool:
    return '0' <= c <= '9'


def is_sign(c: chr) -> bool:
    return c == '-' or c == '+'


def valid_integer(s: str, include_sign: bool = False, accept_just_sign: bool = False) -> bool:
    if len(s) == 0:
        return False
    if include_sign and is_sign(s[0]):
        if len(s) == 1:
            return accept_just_sign
        return valid_integer(s[1:], False)
    for c in s:
        if not is_digit(c):
            return False
    return True


def valid_decimal(s: str) -> bool:
    if len(s) == 0:
        return False
    parts = s.split('.')
    if len(parts) > 2:
        return False
    if len(parts) == 1:
        return valid_integer(s, True)
    else:
        left, right = parts
        if len(left) == 0 and len(right) == 0:
            return False
        valid_left = valid_integer(left, True, len(right) > 0) if len(left) > 0 else True
        valid_right = valid_integer(right, False) if len(right) > 0 else True
        return valid_right and valid_left


def valid_e_pow(s: str) -> bool:
    return valid_integer(s, True)


class Solution:
    def isNumber(self, s: str) -> bool:
        es = count_chars(s, 'eE')
        if es > 1:
            return False
        if es == 0:
            return valid_decimal(s)
        else:
            parts = s.split('e')
            decimal, e_pow = s.split('E') if len(parts) == 1 else parts
            return valid_decimal(decimal) and valid_e_pow(e_pow)


class ValidNumberTest(TestCase):
    def test_is_number(self):
        valid_numbers = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93",
                         "-123.456e789"]
        invalid_numbers = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "+."]
        sol = Solution()
        self.assertEqual(True, sol.isNumber('0'))
        self.assertEqual(False, sol.isNumber('e'))
        self.assertEqual(False, sol.isNumber('.'))
        self.assertEqual(True, sol.isNumber('.1'))

        for nr in valid_numbers:
            self.assertTrue(sol.isNumber(nr))

        for nr in invalid_numbers:
            self.assertFalse(sol.isNumber(nr))

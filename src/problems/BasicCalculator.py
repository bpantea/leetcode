from typing import List
from unittest import TestCase


class Solution:
    def remove_open_parenthesis(self, stack: List):
        sol = 0
        last_nr = None
        while len(stack) > 0 and stack[-1] != '(':
            top = stack.pop()
            if top == '+':
                sol += last_nr
                last_nr = None
            elif top == '-':
                sol -= last_nr
                last_nr = None
            else:
                last_nr = top
        if last_nr is not None:
            sol += last_nr
        stack[-1] = sol

    def get_stack_from_str(self, s: str):
        i = 0
        stack = []
        tmp_nr = None
        while i < len(s):
            if str.isdigit(s[i]):
                if tmp_nr is None:
                    tmp_nr = int(s[i])
                else:
                    tmp_nr = tmp_nr * 10 + int(s[i])
            else:
                if tmp_nr is not None:
                    stack.append(tmp_nr)
                    tmp_nr = None
                if s[i] == '+' or s[i] == '-':
                    stack.append(s[i])
                elif s[i] == '(':
                    stack.append(s[i])
                elif s[i] == ')':
                    self.remove_open_parenthesis(stack)
            i += 1
        if tmp_nr is not None:
            stack.append(tmp_nr)
        return stack

    def calculate(self, s: str) -> int:
        return self.get_stack_from_str('(' + s + ')')[0]


class BasicCalculatorTest(TestCase):
    def test_calculator(self):
        tests = [
            ("1 + 1", 2),
            (" 2-1 + 2 ", 3),
            ("(1+(4+5+2)-3)+(6+8)", 23)
        ]
        for test in tests:
            self.assertEqual(test[1], Solution().calculate(test[0]))

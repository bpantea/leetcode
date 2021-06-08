from typing import List
from unittest import TestCase


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def parse_solutions(idx):
            for neighbour in solutions[idx]:
                if neighbour != len(s):
                    for x in parse_solutions(neighbour):
                        yield s[idx:neighbour] + ' ' + x
                else:
                    yield s[idx:]

        solutions = [[] for _ in range(len(s))]
        for i in reversed(range(len(s))):
            for j in range(len(wordDict)):
                word = wordDict[j]
                if i + len(word) <= len(s) and s[i:i + len(word)] == word and \
                        (i + len(word) == len(s) or len(solutions[i + len(word)]) > 0):
                    solutions[i].append(i + len(word))
        return [x for x in parse_solutions(0)]


class WordBreak2Test(TestCase):
    def test_word_break(self):
        sol = Solution()
        tests = [
            ('catsanddog', ["cat", "cats", "and", "sand", "dog"], ["cats and dog", "cat sand dog"]),
            ('pineapplepenapple', ["apple", "pen", "applepen", "pine", "pineapple"],
             ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"])
        ]
        for test in tests:
            self.assertEqual(sorted(test[2]), sorted(sol.wordBreak(test[0], test[1])))

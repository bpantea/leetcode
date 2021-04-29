from typing import List
from unittest import TestCase


def increment_in_map(my_map, key):
    if key in my_map:
        my_map[key] += 1
    else:
        my_map[key] = 1


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        counts = {}
        for word in words:
            increment_in_map(counts, word)
        indexes = []
        n = len(s)
        words_count = len(words)
        word_len = len(words[0])
        for i in range(0, n - words_count * word_len + 1):
            seen = {}
            j = 0
            while j < words_count:
                word = s[(i + j * word_len): (i + (j + 1) * word_len)]
                if word in counts:
                    increment_in_map(seen, word)
                    if seen[word] > counts[word]:
                        break
                else:
                    break
                j += 1
            if j == words_count:
                indexes.append(i)
        return indexes


class SubstringWithConcatenationOfAllWordsTest(TestCase):
    def test_find_substring(self):
        solution = Solution()
        self.assertEqual([0, 9], solution.findSubstring('barfoothefoobarman', ['foo', 'bar']))
        self.assertEqual([], solution.findSubstring('wordgoodgoodgoodbestword', ["word", "good", "best", "word"]))
        self.assertEqual([6, 9, 12], solution.findSubstring('barfoofoobarthefoobarman', ["bar", "foo", "the"]))

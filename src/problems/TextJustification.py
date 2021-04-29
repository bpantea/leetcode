from typing import List
from unittest import TestCase


def format_line(words: List[str], maxWidth: int, end_line: bool = False) -> str:
    assert len(words) > 0
    if end_line:
        formatted = words[0]
        for i in range(1, len(words)):
            formatted += ' ' + words[i]
        additional_spaces = maxWidth - (len(formatted))
        return formatted + ' ' * additional_spaces
    if len(words) == 1:
        return words[0] + ' ' * (maxWidth - len(words[0]))
    word_count = len(words)
    letter_count = 0
    for word in words:
        letter_count += len(word)
    available_spaces = maxWidth - letter_count
    assert available_spaces >= (len(words) - 1)
    formatted = words[0]
    for i in range(1, len(words)):
        insert_additional_space = available_spaces % (word_count - 1) >= i
        additional_spaces = 1 if insert_additional_space else 0
        nr_spaces_to_insert = available_spaces // (word_count - 1) + additional_spaces
        formatted += ' ' * nr_spaces_to_insert + words[i]
    assert len(formatted) == maxWidth
    return formatted


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        current_line = []
        current_width = -1  # -1 because we will add a new space before each word
        for word in words:
            if len(word) == maxWidth:
                if len(current_line) > 0:
                    lines.append(current_line)
                lines.append([word])
                current_line = []
                current_width = -1
            elif current_width + 1 + len(word) > maxWidth:
                assert len(current_line) > 0
                lines.append(current_line)
                current_line = [word]
                current_width = len(word)
            else:
                current_width += 1 + len(word)
                current_line.append(word)
        if len(current_line) > 0:
            lines.append(current_line)
        return [format_line(lines[i], maxWidth, end_line=i == len(lines) - 1) for i in range(len(lines))]


class TextJustificationTest(TestCase):
    def test_full_justify(self):
        sol = Solution()
        tests = [
            (["This", "is", "an", "example", "of", "text", "justification."], 16),
            (["What", "must", "be", "acknowledgment", "shall", "be"], 16),
            (["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
              "Art", "is", "everything", "else", "we", "do"], 20),
            (["Listen", "to", "many,", "speak", "to", "a", "few."], 6),
            (['a'], 1),
            (["a", "b", "c", "d", "e"], 3)
        ]
        for test in tests:
            result = sol.fullJustify(test[0], test[1])
            for line in result:
                print(line)
            for line in result:
                self.assertEqual(test[1], len(line))

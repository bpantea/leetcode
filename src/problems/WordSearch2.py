from typing import List
from unittest import TestCase


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(board) < 1 or len(board[0]) < 1:
            return []
        trie = {}
        visited = {(-1, -1)}
        delta_positions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        solutions = []

        def build_trie():
            for word in words:
                current_trie = trie
                for i in range(len(word)):
                    if word[i] not in current_trie:
                        current_trie[word[i]] = {}
                    if i == len(word) - 1:
                        current_trie[word[i]][None] = True
                    current_trie = current_trie[word[i]]

        def safe_get_char(i, j) -> chr:
            if i < 0 or i >= len(board):
                return None
            if j < 0 or j >= len(board[0]):
                return None
            return board[i][j]

        def solve(i: int, j: int, current_trie, word):
            visited.add((i, j))
            if current_trie.get(None) is True:
                solutions.append(word)
                current_trie[None] = False
            for delta in delta_positions:
                neighbour = i + delta[0], j + delta[1]
                if neighbour not in visited:
                    c = safe_get_char(neighbour[0], neighbour[1])
                    if c is not None and c in current_trie:
                        solve(neighbour[0], neighbour[1], current_trie[c], word + c)
            visited.remove((i, j))

        build_trie()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = safe_get_char(i, j)
                if c in trie:
                    solve(i, j, trie[c], c)
        return solutions


class WordSearch2Test(TestCase):
    def test_search(self):
        tests = [
            ([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
             ["oath", "pea", "eat", "rain"], ["eat", "oath"]),
            ([["a"]], ["a"], ['a'])
        ]
        sol = Solution()
        for test in tests:
            self.assertEqual(sorted(test[2]), sorted(sol.findWords(test[0], test[1])))

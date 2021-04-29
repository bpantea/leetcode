from queue import Queue
from typing import List
from unittest import TestCase


def matches(s1: str, s2: str) -> bool:
    differences = 0
    for i in range(len(s1)):
        differences += s1[i] != s2[i]
    return differences == 1


class Solution:
    def __init__(self):
        self.list = []
        self.begin = ''
        self.end = ''
        self.begin_idx = None
        self.end_idx = None
        self.min_distance = {}
        self.min_distance_neighbours = {}
        self.neighbours = []
        self.solutions = []
        self.current_solution = []  # this will hold indices in reversed order

    def calculate_neighbours(self):
        for i in range(len(self.list)):
            if self.list[i] == self.begin:
                self.begin_idx = i
            if self.list[i] == self.end:
                self.end_idx = i

        if self.begin_idx is None:
            self.begin_idx = len(self.list)
            self.list.append(self.begin)
        self.neighbours = [[] for _ in range(len(self.list))]
        for i in range(len(self.list)):
            for j in range(i + 1, len(self.list)):
                if matches(self.list[i], self.list[j]):
                    self.neighbours[i].append(j)
                    self.neighbours[j].append(i)

    def calculate_distances(self):
        my_queue = Queue()
        my_queue.put(self.begin_idx)
        self.min_distance[self.begin_idx] = 0
        self.min_distance_neighbours[self.begin_idx] = []
        while not my_queue.empty():
            current = my_queue.get()
            current_dist = self.min_distance[current]
            for neighbour in self.neighbours[current]:
                if neighbour in self.min_distance:
                    if current_dist == self.min_distance[neighbour] - 1:
                        self.min_distance_neighbours[neighbour].append(current)
                    continue
                my_queue.put(neighbour)
                self.min_distance[neighbour] = current_dist + 1
                self.min_distance_neighbours[neighbour] = [current]

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.list = wordList
        self.begin = beginWord
        self.end = endWord

        self.calculate_neighbours()
        if self.end_idx is None:
            return []
        self.calculate_distances()
        if self.end_idx in self.min_distance:
            self.calculate_solutions(self.end_idx)
        return self.solutions

    def calculate_solutions(self, idx):
        self.current_solution.append(idx)
        if idx == self.begin_idx:
            self.solutions.append([self.list[x] for x in reversed(self.current_solution)])
        else:
            for neighbour in self.min_distance_neighbours[idx]:
                self.calculate_solutions(neighbour)
        self.current_solution.pop()


class WordLatter2(TestCase):
    def test_find_ladders(self):
        tests = [
            (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
             [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]),

            (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), []),
            (("hot", "dog", ["hot", "dog"]), [])
        ]
        for test in tests:
            self.assertEqual(test[1], Solution().findLadders(test[0][0], test[0][1], test[0][2]))

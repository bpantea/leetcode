import heapq
from typing import List
from unittest import TestCase


def get_left_position(heap_el) -> int:
    return heap_el[1][0]


def get_right_position(heap_el) -> int:
    return heap_el[1][1]


class Solution:
    def __init__(self):
        self.heap: List[tuple[int, List[int]]] = []
        self.buildings: List[List[int]] = []
        self.solution = []
        self.last_position = -1

    def add_to_solution(self, sol: List[int]):
        if len(self.solution) > 0 and self.solution[-1][0] == sol[0]:
            self.solution[-1][1] = max(self.solution[-1][1], sol[1])
        elif len(self.solution) == 0 or sol[1] != self.solution[-1][1]:
            self.solution.append(sol)

    def handle_points(self, current_position: int = None):
        while len(self.heap) > 0 and (current_position is None or get_right_position(self.heap[0]) < current_position):
            top = heapq.heappop(self.heap)  # this will be a building
            right_position_top = get_right_position(top)

            # add left
            if self.last_position < right_position_top:
                self.last_position = max(self.last_position, get_left_position(top))
                self.add_to_solution([self.last_position, top[1][2]])

            # add right
            if right_position_top > self.last_position:
                while len(self.heap) > 0 and get_right_position(self.heap[0]) <= right_position_top:
                    heapq.heappop(self.heap)
                if len(self.heap) == 0:
                    self.add_to_solution([right_position_top, 0])
                self.last_position = right_position_top

        # here I should add one start of building
        if len(self.heap) > 0 and get_right_position(self.heap[0]) > self.last_position:
            top = self.heap[0]
            self.last_position = max(self.last_position, get_left_position(top))
            self.add_to_solution([self.last_position, top[1][2]])

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        self.buildings = buildings
        for i in range(len(buildings)):
            self.handle_points(current_position=buildings[i][0])
            heapq.heappush(self.heap, (-buildings[i][2], buildings[i]))
        self.handle_points()
        return self.solution


class TheSkylineProblem(TestCase):
    def test_skyline(self):
        tests = [
            ([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
             [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]),
            ([[0, 2, 3], [2, 5, 3]], [[0, 3], [5, 0]]),
            ([[1, 2, 1], [1, 2, 2], [1, 2, 3]], [[1, 3], [2, 0]]),
            ([[1, 20, 1], [1, 21, 2], [1, 22, 3]], [[1, 3], [22, 0]]),
            (
                [[2, 4, 70], [3, 8, 30], [6, 100, 41], [7, 15, 70], [10, 30, 102], [15, 25, 76], [60, 80, 91],
                 [70, 90, 72],
                 [85, 120, 59]],
                [[2, 70], [4, 30], [6, 41], [7, 70], [10, 102], [30, 41], [60, 91], [80, 72], [90, 59], [120, 0]]
            )
        ]
        for test in tests:
            self.assertEqual(test[1], Solution().getSkyline(test[0]))

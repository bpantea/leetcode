from typing import List


def array_of_arrays(lines: int, columns: int, default_value = None) -> List[List]:
    return [[default_value] * columns for _ in range(lines)]

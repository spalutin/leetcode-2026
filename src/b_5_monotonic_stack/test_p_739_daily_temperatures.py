from typing import List, Tuple

from b_5_monotonic_stack.p_739_daily_temperatures import Solution

fixtures: List[Tuple[List[int], List[int]]] = [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([30, 40, 50, 60], [1, 1, 1, 0]),
    ([30, 60, 90], [1, 1, 0]),
]


def test_solution():
    for temperatures, expected in fixtures:
        assert Solution().dailyTemperatures(temperatures) == expected

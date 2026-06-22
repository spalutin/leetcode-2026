"""
https://leetcode.com/problems/daily-temperatures/
"""
from typing import List, Tuple


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[Tuple[int, int]] = []
        result = [0] * len(temperatures)

        for ix in range(len(temperatures)):
            x = temperatures[ix]

            while stack and stack[-1][1] < x:
                jy, _ = stack.pop()
                result[jy] = ix - jy

            stack.append((ix, x))

        return result

"""
https://leetcode.com/problems/daily-temperatures/
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[int] = []
        result = [0] * len(temperatures)

        for ix in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[ix]:
                jy = stack.pop()
                result[jy] = ix - jy

            stack.append(ix)

        return result

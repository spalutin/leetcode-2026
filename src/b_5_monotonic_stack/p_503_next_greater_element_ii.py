"""
https://leetcode.com/problems/next-greater-element-ii/description/
"""
from typing import List, Dict


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        out = [-1] * len(nums)
        stack = []

        for ix in range(len(nums)):
            while stack and nums[stack[-1]] < nums[ix]:
                out[stack.pop()] = ix
            stack.append(ix)

        ix = 0

        while stack:
            jy = stack.pop()

            while 0 <= ix and nums[ix] <= nums[jy]:
                ix = out[ix]

            out[jy] = ix

        return [ix == -1 and -1 or nums[ix] for ix in out]

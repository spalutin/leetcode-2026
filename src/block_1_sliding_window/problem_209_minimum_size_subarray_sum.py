"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

7, [2,3,1,2,4,3] -> 2
4, [1,4,4] -> 1
11, [1,1,1,1,1,1,1,1] -> 0
 """
from typing import List

"""
move right index until sum >= target
if size < min_size or min_size == 0, set min_size = size

"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 1
        total = 0
        min_size = len(nums) + 1

        while right <= len(nums):
            total += nums[right - 1]

            if right - left > min_size:
                total -= nums[left]
                left += 1

            while total >= target:
                if right - left < min_size:
                    min_size = right - left

                if min_size == 1:
                    return 1

                total -= nums[left]
                left += 1

            right += 1

        return min_size <= len(nums) and min_size or 0

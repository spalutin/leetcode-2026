from typing import List

"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

[1,1,1,0,0,0,1,1,1,1,0], 2 -> 6
[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3 -> 10
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        size = len(nums)
        max_size = k
        left = 0
        right = 0
        current_size = k
        while right < size:
            current_size += nums[right]
            max_size = max(current_size, max_size)

            while right - left >= max_size:
                current_size -= nums[left]
                left += 1
            right += 1
        return min(size, max_size)

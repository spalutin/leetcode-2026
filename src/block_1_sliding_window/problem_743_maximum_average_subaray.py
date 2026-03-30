"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k
that has the maximum average value and return this value.
Any answer with a calculation error less than 10^(-5) will be accepted.

[1,12,-5,-6,50,3], 4 -> 12.75
[5], 1 -> 5.0
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum

        for ix in range(0, len(nums) - k):
            current_sum += nums[ix + k] - nums[ix]
            max_sum = max(max_sum, current_sum)

        return max_sum / k

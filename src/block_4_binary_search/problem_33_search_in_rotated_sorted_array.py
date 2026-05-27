"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        shift = self.find_shift(nums)
        print('shift', shift)
        left = 0
        right = size - 1

        if target < nums[(left + shift) % size] or target > nums[(right + shift) % size]:
            return -1

        while left <= right:
            middle = (left + right) // 2

            shifted_middle = (middle + shift) % size

            item = nums[shifted_middle]

            if item == target:
                return shifted_middle

            if target < item:
                right = middle - 1
            else:
                left = middle + 1

        return -1

    def find_shift(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] <= nums[right]:
            return left

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        return left

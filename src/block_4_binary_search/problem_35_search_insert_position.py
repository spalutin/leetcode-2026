"""
https://leetcode.com/problems/search-insert-position/description/
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if target < nums[left]:
            return left

        if target > nums[right]:
            return right + 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid

        if target > nums[right]:
            return right + 1
        else:
            return left

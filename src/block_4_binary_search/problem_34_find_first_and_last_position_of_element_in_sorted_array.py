"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target and (middle == 0 or nums[middle - 1] < target):
                ix = middle
                break

            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        else:
            return [-1, -1]

        left = ix
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target and (middle + 1 == len(nums) or nums[middle + 1] > target):
                jy = middle
                break

            if target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            return [-1, -1]

        return [ix, jy]

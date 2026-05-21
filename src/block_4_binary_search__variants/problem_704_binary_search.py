"""
https://leetcode.com/problems/binary-search/description/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if target < nums[left] or target > nums[right]:
            return -1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

        return -1

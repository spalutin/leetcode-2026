"""
https://leetcode.com/problems/next-greater-element-i/
"""
from typing import List, Dict

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = self.map_elements(nums2)
        return [(nums3[x] if x in nums3 else -1) for x in nums1]

    def map_elements(self, nums: List[int]) -> Dict[int, int]:
        out = dict()
        stack = []

        for num in nums:
            while stack and stack[-1] < num:
                out[stack.pop()] = num
            stack.append(num)

        return out

"""
Given an integer array `nums` of length `n` and an integer `target`,
find three integers at **distinct indices** in `nums` such that the sum is closest to target.

Return __the sum of the three integers.__

You may assume that each input would have exactly one solution.

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        if len(nums) == 3:
            return sum(nums)

        xx = sorted(nums)
        ha = 0
        kz = len(nums) - 1
        closest = xx[0] + xx[len(nums) // 2] + xx[kz]

        if closest == target:
            return target

        while kz - ha > 1:
            while kz - ha > 2 and xx[ha] + xx[ha + 1] + xx[kz - 1] > target:
                kz -= 1

            ix = ha + 1
            jy = kz

            while ix < jy:
                value = xx[ha] + xx[ix] + xx[jy]

                if value == target:
                    return target

                if abs(value - target) < abs(closest - target):
                    closest = value

                if value > target:
                    jy -= 1
                else:
                    ix += 1

            ha += 1

        return closest

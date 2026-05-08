"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.


Constraints:

1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        result = set()

        size = len(nums)
        xx = sorted(nums)
        hw = 0
        while size - hw > 2:
            kz = size - 1
            while kz - hw > 2:
                ix = hw + 1
                jy = kz - 1
                while ix < jy:
                    value = xx[hw] + xx[ix] + xx[jy] + xx[kz]
                    if value == target:
                        result.add((xx[hw], xx[ix], xx[jy], xx[kz]))
                    if value < target:
                        ix += 1
                    else:
                        jy -= 1
                kz -= 1
            hw += 1

        return [[x for x in xx] for xx in result]

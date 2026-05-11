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

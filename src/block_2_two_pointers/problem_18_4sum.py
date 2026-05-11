class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        result = set()

        xx = sorted(nums)
        hw = 0
        max_kz = len(nums) - 1

        while max_kz - hw > 2:
            if xx[hw] + xx[hw + 1] + xx[hw + 2] + xx[hw + 3] > target:
                break

            while max_kz - hw > 3:
                if xx[hw] + xx[hw + 1] + xx[hw + 2] + xx[max_kz - 1] < target:
                    break
                max_kz -= 1

            kz = max_kz
            while kz - hw > 2:
                if xx[kz - 3] + xx[kz - 2] + xx[kz - 1] + xx[kz] < target:
                    break
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

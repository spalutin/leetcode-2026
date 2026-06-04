class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        xx = sorted(nums)
        ha = 0
        kz = len(nums) - 1

        while kz - ha > 1:
            while kz - ha > 2 and xx[ha] + xx[ha + 1] + xx[kz] > 0:
                kz -= 1

            ix = ha + 1
            jy = kz

            while ix < jy:
                value = xx[ha] + xx[ix] + xx[jy]

                if value == 0:
                    result.append([xx[ha], xx[ix], xx[jy]])

                if value < 0:
                    while ix < jy and xx[ix] == xx[ix + 1]:
                        ix += 1
                    ix += 1
                else:
                    while jy > ix and xx[jy] == xx[jy - 1]:
                        jy -= 1
                    jy -= 1

            while ha < kz and xx[ha] == xx[ha + 1]:
                ha += 1

            ha += 1

        return result

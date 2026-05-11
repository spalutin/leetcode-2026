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

    def threeSumOld(self, nums: list[int]) -> list[list[int]]:
        result = []
        entries: dict[int, bool] = {}

        for x in nums:
            if not x and not len(result) and x in entries and entries[x]:
                result.append([0, 0, 0])

            entries[x] = x in entries

        xx = sorted(entries)

        left = 0
        right = len(xx) - 1

        a = xx[left]
        z = xx[right]

        while left < right and a < 0 < z:
            if abs(a) > abs(z):
                fixed = left
                running = right
                shift = -1
            else:
                fixed = right
                running = left
                shift = 1

            while fixed != running:
                b = xx[fixed]
                y = xx[running]
                x = -(b + y)

                if abs(x) > abs(y):
                    break
                if x in entries:
                    if x != y or entries[x]:
                        result.append([b, x, y])

                running += shift

            if shift < 0:
                left += 1
            else:
                right -= 1

            a = xx[left]
            z = xx[right]

        return result

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ix = 0
        jy = len(numbers) - 1
        while ix < jy:
            value = numbers[ix] + numbers[jy]
            if value == target:
                return [ix + 1, jy + 1]
            if value < target:
                ix += 1
            else:
                jy -= 1
        return [-1, -1]

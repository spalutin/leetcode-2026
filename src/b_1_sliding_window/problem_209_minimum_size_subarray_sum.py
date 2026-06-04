from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 1
        total = 0
        min_size = len(nums) + 1

        while right <= len(nums):
            total += nums[right - 1]

            if right - left > min_size:
                total -= nums[left]
                left += 1

            while total >= target:
                if right - left < min_size:
                    min_size = right - left

                if min_size == 1:
                    return 1

                total -= nums[left]
                left += 1

            right += 1

        return min_size <= len(nums) and min_size or 0

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        size = len(nums)
        max_size = k
        left = 0
        right = 0
        current_size = k
        while right < size:
            current_size += nums[right]
            max_size = max(current_size, max_size)

            while right - left >= max_size:
                current_size -= nums[left]
                left += 1
            right += 1
        return min(size, max_size)

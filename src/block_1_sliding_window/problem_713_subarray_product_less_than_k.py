"""
Given an array of integers nums and an integer k,
return the number of contiguous subarrays
where the product of all the elements in the subarray is strictly less than k.

"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k < 2:
            return 0

        left = 0
        right = 0
        product = 1
        total = 0

        while right < len(nums):

            product *= nums[right]

            while left < right and product >= k:
                product = product // nums[left]
                left += 1

            if product < k:
                total += right - left + 1

            right += 1

        return total

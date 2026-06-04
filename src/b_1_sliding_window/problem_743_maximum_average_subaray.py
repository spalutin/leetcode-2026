class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum

        for ix in range(0, len(nums) - k):
            current_sum += nums[ix + k] - nums[ix]
            max_sum = max(max_sum, current_sum)

        return max_sum / k

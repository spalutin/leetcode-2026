class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        fast = slow = 0

        while fast == slow or nums[fast] != nums[slow]:
            slow = (slow + fast % 2) % len(nums)
            fast = (fast + 1) % len(nums)

        return nums[slow]

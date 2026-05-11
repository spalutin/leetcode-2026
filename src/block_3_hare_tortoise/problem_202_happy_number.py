class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = Solution.getSum(n)
        while fast != slow:
            slow = Solution.getSum(slow)
            fast = Solution.getSum(fast)
            fast = Solution.getSum(fast)
        return slow == 1

    @staticmethod
    def getSum(n: int) -> int:
        m = 0
        while n > 0:
            m += (n % 10) ** 2
            n = n // 10
        return m

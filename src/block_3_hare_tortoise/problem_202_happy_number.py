class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n > 1 and n not in visited:
            visited.add(n)
            m = 0
            while n > 0:
                m += (n % 10) ** 2
                n = n // 10
            n = m
        return n == 1

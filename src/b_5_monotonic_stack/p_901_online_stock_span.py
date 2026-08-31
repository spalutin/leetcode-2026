"""
https://leetcode.com/problems/online-stock-span/description/
"""


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
class StockSpanner:
    def __init__(self):
        self.stack: list[tuple[int, int]] = []
        pass

    def next(self, price: int) -> int:
        times = 1
        while self.stack and self.stack[-1][0] <= price:
            times += self.stack.pop()[1]
        self.stack.append((price, times))
        return times

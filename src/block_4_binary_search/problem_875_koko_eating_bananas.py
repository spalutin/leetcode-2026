from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        size = len(piles)
        right = max(piles)

        if h == size:
            return right

        total = sum(piles)

        if total <= h:
            return 1

        left = total // h

        while left <= right:
            middle = left + (right - left) // 2
            hours = sum((pile - 1) // middle + 1 for pile in piles)

            if hours > h:
                left = middle + 1
            else:
                right = middle - 1

        return left

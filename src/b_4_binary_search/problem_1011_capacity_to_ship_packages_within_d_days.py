from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            middle = (left + right) // 2
            if not self.can_ship(weights, days, middle):
                left = middle + 1
            else:
                right = middle

        return left

    def can_ship(self, weights: List[int], days: int, capacity: int) -> bool:
        load = 0
        ships = 1

        for weight in weights:
            load += weight
            if load > capacity:
                ships += 1
                if ships > days:
                    return False
                load = weight

        return True

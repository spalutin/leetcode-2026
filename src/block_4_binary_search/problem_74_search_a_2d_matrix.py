"""
https://leetcode.com/problems/search-a-2d-matrix/description/
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        if height == 0:
            return False
        width = len(matrix[0])
        if width == 0:
            return False
        size = height * width

        left = 0
        right = size - 1

        if target < matrix[left // width][left % width] or target > matrix[right // width][right % width]:
            return False

        while left <= right:
            middle = (left + right) // 2
            item = matrix[middle // width][middle % width]
            if item == target:
                return True

            if target < item:
                right = middle - 1
            else:
                left = middle + 1

        return False

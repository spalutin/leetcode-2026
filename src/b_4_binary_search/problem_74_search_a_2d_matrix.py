"""
https://leetcode.com/problems/search-a-2d-matrix/description/
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.searchMatrixRect(matrix, target)

    def searchMatrixRect(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            return False
        top = 0
        bottom = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        if target < matrix[top][left] or target > matrix[bottom][right]:
            return False

        center = (top + bottom) // 2

        while top <= bottom:
            center = (top + bottom) // 2
            if target < matrix[center][left]:
                bottom = center - 1
            elif target > matrix[center][right]:
                top = center + 1
            else:
                break

        while left <= right:
            middle = (left + right) // 2

            item = matrix[center][middle]

            if item == target:
                return True

            if target < item:
                right = middle - 1
            else:
                left = middle + 1

        return False

    def searchMatrixPlain(self, matrix: List[List[int]], target: int) -> bool:
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

"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array **in-place** with `O(1)` extra memory.
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ix, jy = 0, len(s) - 1
        while ix < jy:
            s[ix], s[jy] = s[jy], s[ix]
            ix += 1
            jy -= 1

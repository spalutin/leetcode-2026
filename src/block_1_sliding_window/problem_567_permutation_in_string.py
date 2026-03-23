"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

s1 = "ab", s2 = "eidbaooo" -> True
s1 = "ab", s2 = "eidboaoo" -> False

1 <= s1.length, s2.length <= 10^4
sq, s2 ~ [a-z]
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return False

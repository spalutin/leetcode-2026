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
        ref_needle = dict()
        size = len(s1)
        for c in s1:
            if c not in ref_needle:
                ref_needle[c] = 0
            ref_needle[c] += 1

        needle = dict()
        left = 0
        right = 1

        while right <= len(s2):
            y = s2[right - 1]

            if y not in ref_needle:
                needle = dict()
                left = right
            else:
                if y not in needle:
                    needle[y] = 0

                needle[y] += 1

                while right - left > size:
                    needle[s2[left]] -= 1
                    left += 1

                if right - left == size and ref_needle == needle:
                    return True

            right += 1
        return False

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

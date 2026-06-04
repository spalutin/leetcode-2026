class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0
        left = 0
        right = 0
        met_c: dict[str, int] = dict()

        while right < len(s):
            c = s[right]
            right += 1

            if c in met_c and met_c[c] >= left:
                left = met_c[c]
            else:
                max_size = max(max_size, right - left)

            met_c[c] = right

        return max_size

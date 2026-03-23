"""
You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

"ABAB", 2 -> 4
"AABABBA", 1 -> 4

1 <= len(s) <= 10^5
s in [A-Z]
0 <= k <= len(s)

max_size = 1
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # @todo solve again
        size = len(s)

        max_size = 0
        sizes: dict[str, int] = dict()
        left, right = 0, 0

        while right < size:
            y = s[right]
            if y not in sizes:
                sizes[y] = k
            sizes[y] += 1

            max_size = max(max_size, sizes[y])

            while right - left >= max_size:
                x = s[left]
                sizes[x] -= 1
                left += 1

            right += 1

        return min(size, max_size)

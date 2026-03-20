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
in a cycle, left = 0, stop cycle when left + max_size > size
in a cycle, right = left+1, stop cycle when reached end
move right until a number of c[right] != c[left] reaches k+1
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        size = len(s)

        if size - k < 2:
            return size

        max_size = 1
        left, right = 0, 0

        while left + max_size <= size:
            counter = k
            a = s[left]
            right = left

            while right < size:
                z = s[right]

                if z != a:
                    counter -= 1

                if counter < 0:
                    break

                right += 1

            max_size = max(max_size, right - left)
            left += 1

        return max_size

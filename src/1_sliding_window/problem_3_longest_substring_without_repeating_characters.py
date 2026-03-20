"""
Given a string s, find the length of the longest substring without duplicate characters.

"abcabcbb"  -> 3
"bbbbb"     -> 1
"pwwkew"    -> 3

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.

1 <= result <= 26 (abc...xyz)

if len(s) == 0: return 0
if len(s) == 1: return 1
if len(s) == 2: return 1 + s[0] != s[1]

for test_case in test_cases:
1. max_size = 0
1. left = 0, right = 0
2. in a cycle: compare c = s[right] with a string s[left:right]
    if c not in substring:
        move right+=1,
        if right - left > max_size: max_size = right - left
    if c in substring:
        move left+1 until c not in substring

max_size = 0
left = 0
right = 0

abcabcbb
       ^
        ^
ss = b
c = b
max_size = 3

improvements:
met_c = dict[str, int]
c in met_c:
    yes:
        jump left to met_c[c]
    no:
        move right+=1
    met_c[c] = right
consumes memory
reduces time
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0
        left = 0
        right = 0
        while right < len(s):
            c = s[right]

            if c in s[left:right]:
                left += 1
            else:
                right = right + 1
                max_size = max(max_size, right - left)
        return max_size

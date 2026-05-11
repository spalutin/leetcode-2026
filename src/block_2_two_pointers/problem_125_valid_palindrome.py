"""
A phrase is a **palindrome** if,
after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a **palindrome**, or `false` otherwise.

**Constraints:**

* `1 <= s.length <= 2 * 10^5`
* `s` consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ix = 0
        jy = len(s) - 1

        while ix < jy:
            if not s[ix].isalnum():
                ix += 1
                continue

            if not s[jy].isalnum():
                jy -= 1
                continue

            if s[ix].lower() != s[jy].lower():
                return False

            ix += 1
            jy -= 1

        return True

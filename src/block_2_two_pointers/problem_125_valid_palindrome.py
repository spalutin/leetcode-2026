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
            x = Solution.mapChar(s[ix])
            y = Solution.mapChar(s[jy])

            while not x and ix < jy:
                ix += 1
                x = Solution.mapChar(s[ix])

            while not y and ix < jy:
                jy -= 1
                y = Solution.mapChar(s[jy])

            if x != y:
                return False

            ix += 1
            jy -= 1

        return True

    @staticmethod
    def mapChar(s: str) -> int:
        x = ord(s)
        if 48 <= x <= 57:
            return x - 47
        if 65 <= x <= 90:
            return x - 54
        if 97 <= x <= 122:
            return x - 86
        return 0

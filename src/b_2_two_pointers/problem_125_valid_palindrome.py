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

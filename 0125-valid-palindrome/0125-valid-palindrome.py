class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lidx = 0
        ridx = len(s) - 1

        while lidx < ridx:
            if not s[lidx].isalnum():
                lidx += 1
            elif not s[ridx].isalnum():
                ridx -= 1
            else:
                if s[lidx] != s[ridx]:
                    return False
                lidx += 1
                ridx -= 1
        return True
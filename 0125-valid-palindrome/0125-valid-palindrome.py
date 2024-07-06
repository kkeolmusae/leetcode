class Solution:
    def isPalindrome(self, s: str) -> bool:
        sidx = 0
        eidx = len(s) - 1
        
        if len(s) == 2:
            if not s[0].isalnum() or not s[1].isalnum():
                return True
            if s[0].lower() != s[1].lower():
                return False
            return True
        
        while sidx < eidx:
            if not s[sidx].isalnum():
                sidx += 1
                continue
            elif not s[eidx].isalnum():
                eidx -= 1
                continue
            
            if s[sidx].lower() == s[eidx].lower():
                sidx += 1
                eidx -= 1
                continue
            else:
                return False
        return True
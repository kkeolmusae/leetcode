### 다른 풀이
좀더 단순하고 쉽게 구현된거임. (`isalnum() == 알파벳 혹은 숫자인지 체크`)
```py
class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
```

내 코드는
```py
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
```
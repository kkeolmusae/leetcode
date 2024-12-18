# 풀이
- Difficulty:  Easy
- Topic:  Two Pointers
- Elapsed Time:  2m
- Status:  O (2 times)
- Memo: 지난번보다 쉽고 간단하게 품

## 내 풀이
```py
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
```

## 다른 풀이
내 코드랑 비슷함
### Approach 1: Two Pointers
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

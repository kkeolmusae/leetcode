# 풀이
- LeetCode 75, Easy
- Array / String
- Time: 5m 52s
- 딱히 어려움은 없었음. 더 최적화할 수 있을법한데 시간초과 안날 것 같아서 그냥 함

## 내 코드 
```py
class Solution:
    def reverseVowels(self, s: str) -> str:
        strs = ""
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        for st in s: # 모음(aeiou) 찾아서 strs에 저장하고
            if st in vowels:
                strs += st

        i = 0
        strs = "".join(reversed(strs)) # 뒤집고

        result = ""
        for idx in range(len(s)): # 다시 반복하면서 모음이 아니면 걍 더하고 모음이면 뒤집은거 순서대로 하나씩 추가함
            st = s[idx]
            if st in vowels:
                result += strs[i]
                i += 1
            else:
                result += st
        return result
```

## 다른 풀이

### Approach 1: Two Pointers
- Two Pointers 로 해결함. 이게 더 깔끔한듯. 
```py
class Solution:
    def isVowel(self, c: str) -> bool:
        # Return true if the character is a vowel (case-insensitive)
        return c in 'aeiouAEIOU'
    
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1
        s = list(s)  # 문자열은 변경이 불가능하므로 리스트로 변환
        
        # While we still have characters to traverse
        while start < end:
            # Find the leftmost vowel
            while start < len(s) and not self.isVowel(s[start]):
                start += 1
            # Find the rightmost vowel
            while end >= 0 and not self.isVowel(s[end]):
                end -= 1
            # Swap them if start is left of end
            if start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        
        return ''.join(s)  # 리스트를 다시 문자열로 변환
```
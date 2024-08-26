# 풀이
- LeetCode 75, Medium
- Stack
- Time: 1m
- 이게 Medium 이 맞나 싶을 정도로 쉽고 빠르게 품. 

## 내 풀이
```py
class Solution:
    def removeStars(self, s: str) -> str:
        q = []

        for st in s:
            if st == "*" and q:  # *이 들어오면 pop. q가 비어있으면 에러발생하니깐 q도 조건에 추가
                q.pop()
            else:
                q.append(st)
        return "".join(q)
```

## 다른 풀이
내 풀이랑 비슷함. Stack 말고 다른 방법으로 푼 코드도 있는데 그냥 넘김.
### Approach 1: Stack
```py
class Solution:
    def removeStars(self, s):
        st = []
        for i in range(0, len(s)):
            if s[i] == '*':
                st.pop()
            else:
                st.append(s[i])

        return ''.join(st)
```
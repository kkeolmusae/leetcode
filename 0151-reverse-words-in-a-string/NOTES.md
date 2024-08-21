# 풀이
- LeetCode 75, Medium
- Array / String
- Time: 2m 15s
- 쉬움. 걍 띄워쓰기로 split 하고 배열에 때려넣고 reverse 하고 join 쓰면 끝

## 내 풀이
```py
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")

        result = []
        for w in words:
            if w != "":
                result.append(w)
        result.reverse()

        return " ".join(result)
```

## 다른 풀이
### Approach 1: Built-in Split + Reverse
?? 내 코드보다 더 쉬움
```py
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
```

### 기타 풀이 생략 (어렵게 접근함)

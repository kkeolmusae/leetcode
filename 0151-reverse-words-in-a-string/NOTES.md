# 풀이
- Medium
- Array / String
- Time: 2m 15s
- 쉬움. 걍 띄워쓰기로 split 하고 뒤집어서 배열에 때려넣고 join 쓰면 끝

## 내 풀이
```py
class Solution:
    def reverseWords(self, s: str) -> str:
        new_strs = []
        for word in list(reversed(s.split(" "))):
            if word != "":
                new_strs.append(word)
        return " ".join(new_strs)
```

## 다른 풀이
### Approach 1: Built-in Split + Reverse
?? 내 코드보다 더 쉬움.
- split(" "): 스페이스를 기준으로 나눔
- split(): 공백(스페이스, 탭, 줄바꿈 등 모든 공백 문자)을 기준으로 문자열을 나누고, 연속된 공백은 무시
```py
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
```

### 기타 풀이 생략 (어렵게 접근함)

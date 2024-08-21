# 풀이
- LeetCode 75, Easy
- Array / String
- Time: 5m
- 쉬운 문제. 그냥 두 문자 하나씩 꺼내서 붙이고 나머지 붙이면 끝

## 내 풀이
```py
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            result += word1[i] + word2[j]
            i += 1
            j += 1

        if i < len(word1):  # w1을 덜 처리한 경우
            return result + word1[i:]

        if j < len(word2):
            return result + word2[j:]

        return result
```
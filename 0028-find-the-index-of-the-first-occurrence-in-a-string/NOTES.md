# 풀이
- Difficulty:  Easy
- Topic:  Array / String
- Elapsed Time:  10s?
- Status:  O
- Memo: 아주 쉬운문제

## 내 풀이
그냥 내장함수 썼다
```py
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

```

## 다른 풀이
### Approach 1: Sliding Window
```py
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)  # 검색할 문자열(needle)의 길이
        n = len(haystack)  # 대상 문자열(haystack)의 길이

        # haystack의 윈도우를 순회 (윈도우 크기는 needle의 길이와 동일)
        for window_start in range(n - m + 1):
            for i in range(m):  # needle의 각 문자와 haystack의 현재 윈도우를 비교
                if needle[i] != haystack[window_start + i]:  # 문자가 일치하지 않으면 비교 종료
                    break
                if i == m - 1:  # needle의 모든 문자가 일치하면 현재 윈도우 시작 인덱스 반환
                    return window_start

        # needle이 haystack 내에서 발견되지 않으면 -1 반환
        return -1

```

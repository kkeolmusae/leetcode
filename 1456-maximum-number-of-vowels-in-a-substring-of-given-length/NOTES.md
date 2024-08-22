# 풀이

- LeetCode 75, Medium
- Sliding Window
- Time: 3m
- 한번에 품. 확실히 Easy 하나 풀고 푸니깐 좀 빨리 방법을 찾는듯

## 내 코드 
```py
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        initCnt = 0
        for st in s[:k]:  # 일단 k 번째까지 미리 체크해서 개수 세보고
            if st in "aeiou":
                initCnt += 1

        result = initCnt
        for idx in range(k, len(s)):  # k 번째 다음부터 확인
            if s[idx] in "aeiou":  # 지금 차례의 문자가 모음이면 개수 증가
                initCnt += 1
            if s[idx - k] in "aeiou":  # 지금 차례 - k 문자가 모음이면 개수 감소
                initCnt -= 1

            result = max(result, initCnt)  # 최대 개수 갱신
        return result
```

## 다른 풀이

### Approach: Sliding Window
내 코드랑 아주 흡사함.
```py
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # 초반 k 개 개수 세팅
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)
        answer = count
        
        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i - k] in vowels)
            answer = max(answer, count)
        
        return answer
```
# 풀이
- Difficulty: Medium
- Topic:  Array / String
- Elapsed Time:  2m
- Status:  O
- Memo: 그냥 쉬운문제. 

## 내 풀이
```py
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        for lidx in range(len(s) - 1, -1, -1):  # 뒤에서 부터 문자 시작
            if s[lidx] != " ":  # 빈문자가 아니면 개수 증가
                cnt += 1
            elif cnt > 0 and s[lidx] == " ":
                # 만약 빈문자인데 cnt가 0보다 크면 마지막 단어가 끝났다는거니깐 리턴
                return cnt
        return cnt
```

## 다른 풀이
### Approach 1: String Index Manipulation
```py
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 문자열의 뒤에서부터 시작하기 위해 마지막 인덱스를 설정
        p = len(s) - 1
        
        # 문자열 끝에 있는 공백을 건너뜀
        while p >= 0 and s[p] == " ":
            p -= 1

        # 마지막 단어의 길이를 계산
        length = 0
        while p >= 0 and s[p] != " ":  # 공백이 아닌 문자를 발견할 때까지 진행
            p -= 1
            length += 1  # 길이를 증가시킴
        
        return length

```

### Approach 2: One-loop Iteration
내 코드랑 비슷하다
```py
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p, length = len(s), 0

        while p > 0:
            p -= 1
            if s[p] != " ":
                length += 1
            elif length > 0:
                return length

        return length
```

### Approach 3: Built-in String Functions
숏코딩 (isspace = 문자열이 모두 공백이면 True 반환. 그외는 False 반환)
```py
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return 0 if not s or s.isspace() else len(s.split()[-1])
```

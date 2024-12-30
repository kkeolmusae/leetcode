# 풀이
- Difficulty:  Medium
- Topic:  Sliding Window
- Elapsed Time:  (다른 컴퓨터에서 풀었어서 시간 정보가 없다)
- Status:  O
- Memo:  지난번에 못풀었었는데 이번에는 풀었다?  (다른 컴퓨터에서 풀었어서 메모가 없다)

## 내 풀이
```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        idx = {}
        st = ""
        result = 0
        start = 0

        for i in range(len(s)):  # 인덱스 기준으로 탐색
            curr_char = s[i]  # 현재 문자
            # 이미 등장한 문자이고, start 보다 뒤에 있을 때
            if curr_char in idx and idx[curr_char] >= start:
                # idx[curr_char]: 현재 문자의 이전 인덱스
                st = s[idx[curr_char] + 1 : i]  # start ~ 현재 문자까지 슬라이싱
                start = idx[s[i]] + 1  # start 갱신
            st += s[i]  # st 에 현재 문자 추가
            idx[s[i]] = i  # 현재 문자의 인덱스 저장
            result = max(result, len(st))  # 최대 길이 갱신

        return result
```

## 다른 풀이
### Approach 1: Sliding Window
```py
from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()  # 각 문자의 빈도를 저장할 Counter 객체

        left = right = 0  # 슬라이딩 윈도우의 왼쪽(left)과 오른쪽(right) 포인터 초기화

        res = 0  # 가장 긴 부분 문자열의 길이를 저장할 변수
        while right < len(s):  # 오른쪽 포인터가 문자열의 끝에 도달할 때까지 반복
            r = s[right]  # 현재 오른쪽 포인터의 문자
            chars[r] += 1  # 문자의 빈도 증가

            # 같은 문자가 중복되어 부분 문자열의 조건이 깨질 경우
            while chars[r] > 1:
                l = s[left]  # 왼쪽 포인터의 문자
                chars[l] -= 1  # 해당 문자의 빈도 감소
                left += 1  # 왼쪽 포인터 이동

            # 현재 부분 문자열의 길이를 계산하고 결과를 갱신
            res = max(res, right - left + 1)

            right += 1  # 오른쪽 포인터 이동
        return res
```

### Approach 2: Sliding Window Optimized
```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)  # 문자열의 길이
        ans = 0  # 가장 긴 부분 문자열의 길이를 저장할 변수
        # 각 문자가 마지막으로 등장한 위치 이후의 인덱스를 저장하는 딕셔너리
        charToNextIndex = {}

        i = 0  # 슬라이딩 윈도우의 시작 인덱스

        # 슬라이딩 윈도우의 끝 인덱스 `j`를 이동하며 탐색
        for j in range(n):
            # 현재 문자가 이미 슬라이딩 윈도우 안에 존재하면
            if s[j] in charToNextIndex:
                # 슬라이딩 윈도우의 시작 인덱스를 업데이트 (중복 제거)
                i = max(charToNextIndex[s[j]], i)

            # 현재 윈도우의 길이를 계산하고 최대 길이를 갱신
            ans = max(ans, j - i + 1)
            # 현재 문자의 다음 인덱스를 저장
            charToNextIndex[s[j]] = j + 1

        return ans

```
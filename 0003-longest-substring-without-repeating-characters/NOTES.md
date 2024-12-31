# 풀이
- Difficulty:  Medium
- Topic:  Two Pointers
- Elapsed Time:  30m
- Status:  O 
- Memo: 지난번에 못풀었는데 이번에 품. 근데 머리가 안굴러가서 오래 걸림...

## 내 풀이
```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        idx = {}  # 각 문자의 마지막 위치를 저장하는 딕셔너리
        st = ""  # 현재 확인 중인 부분 문자열
        result = 0  # 가장 긴 부분 문자열의 길이
        start = 0  # 현재 부분 문자열의 시작 인덱스

        for i in range(len(s)):  # 문자열의 각 문자에 대해 반복
            curr_char = s[i]  # 현재 문자
            # 현재 문자가 이미 등장했고, 시작 인덱스(start) 이후에 위치할 경우
            if curr_char in idx and idx[curr_char] >= start:
                # 이전에 등장한 현재 문자의 위치(idx[curr_char]) 이후부터 새로운 시작점 지정
                st = s[idx[curr_char] + 1 : i]  # start를 새로운 위치로 갱신
                start = idx[curr_char] + 1  # 시작 인덱스를 갱신
            st += s[i]  # 현재 문자를 부분 문자열에 추가
            idx[s[i]] = i  # 현재 문자의 인덱스를 저장
            result = max(result, len(st))  # 최대 길이 갱신

        return result
```

## 다른 풀이
### Approach 1: Sliding Window
```py
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()  # 각 문자와 그 빈도를 저장하는 Counter 객체
        left = right = 0  # 슬라이딩 윈도우의 왼쪽(left)과 오른쪽(right) 포인터
        res = 0  # 결과값, 가장 긴 부분 문자열의 길이

        # 오른쪽 포인터를 이동하며 문자열을 순회
        while right < len(s):
            r = s[right]  # 현재 오른쪽 포인터가 가리키는 문자
            chars[r] += 1  # 해당 문자의 빈도를 증가

            # 현재 윈도우에 중복 문자가 있으면, 윈도우 크기를 줄임
            while chars[r] > 1:  # 중복된 문자가 존재하는 경우
                l = s[left]  # 왼쪽 포인터가 가리키는 문자
                chars[l] -= 1  # 해당 문자의 빈도를 감소
                left += 1  # 왼쪽 포인터를 오른쪽으로 이동

            # 중복이 없는 현재 윈도우의 길이를 계산하고 최대값을 갱신
            res = max(res, right - left + 1)

            right += 1  # 오른쪽 포인터를 이동

        return res  # 가장 긴 중복 없는 부분 문자열의 길이 반환
```

### Approach 2: Sliding Window Optimized
```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)  # 문자열의 길이
        ans = 0  # 결과값, 가장 긴 중복 없는 부분 문자열의 길이
        # charToNextIndex는 각 문자가 마지막으로 나타난 위치 다음 인덱스를 저장
        charToNextIndex = {}

        i = 0  # 슬라이딩 윈도우의 시작 포인터

        # j는 슬라이딩 윈도우의 끝 포인터로 문자열을 순회
        for j in range(n):
            # 현재 문자가 이미 윈도우 안에 있는 경우, 중복을 제거하기 위해 시작 위치(i) 이동
            if s[j] in charToNextIndex:
                # i를 현재 문자 다음 위치로 이동 (기존 i보다 크거나 같아야 함)
                i = max(charToNextIndex[s[j]], i)

            # 현재 윈도우의 길이를 계산하고, 최대값 갱신
            ans = max(ans, j - i + 1)
            # 현재 문자의 다음 위치를 기록
            charToNextIndex[s[j]] = j + 1

        return ans  # 가장 긴 중복 없는 부분 문자열의 길이 반환
```
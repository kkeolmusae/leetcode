# 풀이
- Difficulty:  Medium
- Topic:  Sliding Window
- Elapsed Time:  7m
- Status:  O
- Memo: 풀긴 풀었는데 시간복잡도가 좀 똥임

## 내 풀이
s1 을 정렬한다음에, s2를 s1 길이만큼 체크하면서 정렬해서 비교함.
```py
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(s1))
        window_size = len(s1)
        lidx = 0

        while lidx + window_size <= len(s2):
            tmp = "".join(sorted(s2[lidx : lidx + window_size]))
            if s1 == tmp:
                return True
            lidx += 1
        return False
```

## 다른 풀이
### Approach 1: Brute Force
s1 의 모든 순열을 생성한 다음, s2 랑 비교하는 방법.
```py
class Solution:
    def __init__(self):
        self.flag = False  # 결과를 저장하는 플래그 변수

    def checkInclusion(self, s1: str, s2: str) -> bool:
        self.permute(s1, s2, 0)  # 순열 생성 및 확인
        return self.flag

    def swap(self, s: str, i0: int, i1: int) -> str:
        # 두 위치의 문자를 교환하여 새로운 문자열 생성
        if i0 == i1:
            return s
        s = list(s)
        s[i0], s[i1] = s[i1], s[i0]
        return ''.join(s)

    def permute(self, s1: str, s2: str, l: int):
        if l == len(s1):
            # s1이 s2의 부분 문자열인지 확인
            if s1 in s2:
                self.flag = True
        else:
            for i in range(l, len(s1)):
                # l번째 문자와 i번째 문자를 교환
                s1 = self.swap(s1, l, i)
                # 다음 단계로 재귀 호출
                self.permute(s1, s2, l + 1)
                # 원래 상태로 복원
                s1 = self.swap(s1, l, i)

```

### Approach 2: Using sorting:
s1 을 정렬한다음에, s2를 s1 길이만큼 체크하면서 정렬해서 비교하는 방법으로 내 코드와 똑같은 방법으로 접근함
```py
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 문자열 s1을 정렬
        s1_sorted = ''.join(sorted(s1))
        
        # s2에서 길이가 s1과 같은 모든 부분 문자열 확인
        for i in range(len(s2) - len(s1) + 1):
            # 현재 부분 문자열을 정렬하여 비교
            if s1_sorted == ''.join(sorted(s2[i:i + len(s1)])):
                return True
        
        return False
```

### Approach 3: Using Hashmap
정렬대신 문자 빈도 카운트로 해결한 방법.
```py
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # s1의 문자 빈도 카운트를 저장
        s1map = Counter(s1)
        
        # s2의 길이가 s1과 같은 윈도우에 대해 빈도 카운트를 비교
        for i in range(len(s2) - len(s1) + 1):
            s2map = Counter(s2[i:i + len(s1)])  # 현재 윈도우의 빈도 카운트
            if self.matches(s1map, s2map):
                return True
        
        return False
    
    def matches(self, s1map: Counter, s2map: Counter) -> bool:
        # 두 카운터의 빈도 값이 동일한지 확인
        for key in s1map:
            if s1map[key] != s2map.get(key, 0):
                return False
        return True

```

### Approach 4: Using Array [Accepted]
이것도 빈도수를 체크하는 방법인데, Approach 3이랑 조금 다름
```py
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # 알파벳의 빈도를 저장하는 배열 (a-z 기준 26개)
        s1arr = [0] * 26
        for char in s1:
            s1arr[ord(char) - ord('a')] += 1  # s1의 문자 빈도 기록
        
        # s2의 각 부분 문자열의 빈도와 비교
        for i in range(len(s2) - len(s1) + 1):
            s2arr = [0] * 26
            for j in range(len(s1)):
                s2arr[ord(s2[i + j]) - ord('a')] += 1  # 현재 윈도우의 문자 빈도 기록
            if self.matches(s1arr, s2arr):
                return True
        
        return False
    
    def matches(self, s1arr: list[int], s2arr: list[int]) -> bool:
        # 두 배열의 값이 동일한지 확인
        for i in range(26):
            if s1arr[i] != s2arr[i]:
                return False
        return True

```

### Approach 5: Sliding Window [Accepted]:
Sliding Window 를 사용한 가장 이상적인 방법 아닌가 싶음
- s1의 빈도를 배열에 저장하고,
- s2의 첫번쨰 윈도우 빈도를 초기화하고
- 슬라이딩 윈도우 방식으로 검사 (이동할때마다 새로운 문자 추가, 이전 문자 제거)
```py
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # 알파벳 빈도를 저장하는 배열 (a-z 기준 26개)
        s1arr = [0] * 26
        s2arr = [0] * 26
        
        # s1의 문자 빈도와 s2의 첫 윈도우 빈도를 초기화
        for i in range(len(s1)):
            s1arr[ord(s1[i]) - ord('a')] += 1
            s2arr[ord(s2[i]) - ord('a')] += 1
        
        # 슬라이딩 윈도우 방식으로 검사
        for i in range(len(s2) - len(s1)):
            if self.matches(s1arr, s2arr):
                return True
            # 윈도우를 오른쪽으로 이동: 새로운 문자 추가, 이전 문자 제거
            s2arr[ord(s2[i + len(s1)]) - ord('a')] += 1
            s2arr[ord(s2[i]) - ord('a')] -= 1
        
        # 마지막 윈도우 검사
        return self.matches(s1arr, s2arr)
    
    def matches(self, s1arr: list[int], s2arr: list[int]) -> bool:
        # 두 배열의 값이 동일한지 확인
        return s1arr == s2arr

```

### Approach 6: Optimized Sliding Window [Accepted]:
Approach 5 를 개선한 방법. count 라는 변수를 활용하여 s1과 동일한 빈도를 가지는 알파벳 개수를 저장해두는 것으로 `matches` 함수(배열 비교)를 사용안하게 됨 (성능 개선)
```py
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # 알파벳 빈도를 저장하는 배열
        s1arr = [0] * 26
        s2arr = [0] * 26
        
        # s1의 문자 빈도와 s2의 첫 윈도우 빈도를 초기화
        for i in range(len(s1)):
            s1arr[ord(s1[i]) - ord('a')] += 1
            s2arr[ord(s2[i]) - ord('a')] += 1
        
        # 동일한 빈도를 가지는 알파벳 개수
        count = sum(1 for i in range(26) if s1arr[i] == s2arr[i])
        
        for i in range(len(s2) - len(s1)):
            if count == 26:
                return True
            
            # 윈도우의 오른쪽 끝 문자 추가
            r = ord(s2[i + len(s1)]) - ord('a')
            s2arr[r] += 1
            if s2arr[r] == s1arr[r]:
                count += 1
            elif s2arr[r] == s1arr[r] + 1:
                count -= 1
            
            # 윈도우의 왼쪽 끝 문자 제거
            l = ord(s2[i]) - ord('a')
            s2arr[l] -= 1
            if s2arr[l] == s1arr[l]:
                count += 1
            elif s2arr[l] == s1arr[l] - 1:
                count -= 1
        
        return count == 26

```
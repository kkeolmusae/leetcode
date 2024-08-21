# 풀이
- LeetCode 75, Easy
- Two Pointers
- Time: 7m
- 딱히 어려움은 없었음. 

## 내 풀이
```py
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        sidx = 0
        tidx = 0

        while tidx < len(t):
            if s[sidx] != t[tidx]:  # 같은 문자 나올때 까지 tidx 증가
                tidx += 1
                continue
            sidx += 1  # 같은 문자 나오면 sidx, tidx 증가
            tidx += 1

            if sidx >= len(s):  # s 다 봤으면 subsequence니깐 True
                return True

        return False  # tidx가 범위를 넘어가서 끝난거면 subsequence 가 아닌거라 False
```

## 다른 풀이

### Approach 1: Divide and Conquer with Greedy
- s[left_index]가 t[right_index]와 같다면, s와 t의 다음 문자로 이동 (left_index와 right_index를 모두 증가).
- 그렇지 않다면, t의 다음 문자로만 이동 (right_index만 증가).
```py
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        def rec_isSubsequence(left_index, right_index):
            # 기본 종료 조건
            if left_index == LEFT_BOUND:
                return True  # s의 모든 문자가 찾았을 때
            if right_index == RIGHT_BOUND:
                return False  # t를 다 순회했는데 s의 문자가 남아 있을 때
            
            # s와 t의 현재 문자가 일치하는 경우
            if s[left_index] == t[right_index]:
                left_index += 1  # s의 다음 문자로 이동
            right_index += 1  # t의 다음 문자로 이동

            return rec_isSubsequence(left_index, right_index)

        return rec_isSubsequence(0, 0)
```

### Approach 2: Two-Pointers
짧고 간결하게 풀림. 좀 정석같은 느낌
```py
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        p_left = p_right = 0
        while p_left < LEFT_BOUND and p_right < RIGHT_BOUND:
            # 두 포인터를 모두 이동하거나, 오른쪽 포인터만 이동
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1

        return p_left == LEFT_BOUND

```

### Approach 3: Greedy Match with Character Indices Hashmap
이진검색(bisect)를 사용해서 푼 문제. DP로 푸는것보다는 나은데 굳이 이렇게 풀어야 하나 싶지만 넣음. 
```py
from collections import defaultdict
import bisect

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # t의 각 문자가 등장하는 인덱스를 저장하는 해시 테이블 생성
        letter_indices_table = defaultdict(list)
        for index, letter in enumerate(t):
            letter_indices_table[letter].append(index)

        curr_match_index = -1
        for letter in s:
            if letter not in letter_indices_table:
                return False  # 일치하는 문자가 없으므로, 바로 False 반환

            # 이진 검색을 통해 탐욕적(greedy)으로 일치하는 인덱스 찾기
            indices_list = letter_indices_table[letter]  # indices_list는 현재 문자가 t에서 등장하는 모든 인덱스 리스트
            match_index = bisect.bisect_right(indices_list, curr_match_index) 
             # 현재까지 매칭된 인덱스 이후에 나타나는 첫 번째 인덱스를 이진 검색을 통해 찾음

            if match_index != len(indices_list):
                curr_match_index = indices_list[match_index]
            else:
                return False # 적절한 일치가 없으면 False 반환

        return True

```
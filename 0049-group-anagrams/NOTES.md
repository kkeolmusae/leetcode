# 풀이
- Difficulty:  Medium
- Topic:  Hashmap
- Elapsed Time:  5m
- Status:  O (2 times)
- Memo: 딱히 어렵지 않았음.

## 내 풀이
이전에 풀었던건데 이전에 잘 풀었었네..?
```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp = []
        for idx in range(len(strs)):  # 정렬한 문자 추가
            tmp.append("".join(sorted(strs[idx])))

        anagrams = defaultdict(list)
        for idx in range(len(tmp)):  # 정렬한 문자를 key로 하여 그룹화
            anagrams[tmp[idx]].append(strs[idx])

        result = []
        for key in anagrams:  # 그룹화된 문자들을 리스트로 변환
            result.append(anagrams[key])
        return result
```

## 다른 풀이법
### Approach 0: 이전 코드
strs 에서 하나씩 꺼내서 정렬된 값을 key로 해서 dict에 넣어두고 전체 리턴 (N K logK) N: strs 개수, K: 문자열 최대 길이
```py
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        for s in strs: # N
            sorted_str = sorted(s) # KlogK (K 길이의 문자를 정렬하는데 필요한 시간)
            dic["".join(sorted_str)].append(s)
        return list(dic.values())
```

### Approach 1: Categorize by Sorted String
```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
```

### Approach 2: Categorize by Count
O(N K) 방법: 문자를 유니코드로 변경한 다음 해당 숫자에 ord('a')를 빼서 계산함으로서 a를 0으로 치환. 정렬을 하지 않고 문자열(s)의 문자들에 대한 순환만 하기때문에 O(NK)
```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
```
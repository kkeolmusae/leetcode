# 다른 풀이
문제 유형: Greedy 

### 내 풀이
나는 이렇게 품. 
1. 문자열을 읽어서 각 문자별로 최소인덱스, 최대 인덱스를 우선 저장하고 
2. 그 다음 다시 문자열을 읽어서 최소 인덱스랑 최대 인덱스 사이에 문자가 있으면 하나의 그룹으로 포함
3. 만약 아예 범위에서 벗어나면 다른 그룹으로 처리
- 시간복잡도: O(n)

```py
from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        answer = []
        n = len(s)

        class ob:
            def __init__(self) -> None:
                self.min = n + 1
                self.max = -1

        dic = defaultdict(ob)

        for idx in range(n):
            st = s[idx]

            dic[st].min = min(dic[st].min, idx)
            dic[st].max = max(dic[st].max, idx)

        min_idx = dic[s[0]].min
        max_idx = dic[s[0]].max
        cnt = 1
        for idx in range(1, n):
            alpha = s[idx]
            if (min_idx <= dic[alpha].min and dic[alpha].min <= max_idx) or (
                min_idx <= dic[alpha].max and dic[alpha].max <= max_idx
            ):
                cnt += 1
                min_idx = min(dic[alpha].min, min_idx)
                max_idx = max(dic[alpha].max, max_idx)
            else:
                answer.append(cnt)
                cnt = 1
                min_idx = dic[alpha].min
                max_idx = dic[alpha].max

        answer.append(cnt)

        return answer
```

### 다른 풀이
각 문자의 마지막 인덱스만 저장해서 품. 
시간 복잡도: O(n)
```py
class Solution(object):
    def partitionLabels(self, S):

        # 각 문자가 문자열 S에서 마지막으로 나타나는 인덱스를 저장하는 딕셔너리
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []

        for i, c in enumerate(S):  # 문자열 S의 각 문자와 인덱스를 순회합니다.

            # 현재 문자의 마지막 인덱스를 j와 비교하여 j를 업데이트합니다. 이는 현재 부분 문자열의 끝을 결정하는데 사용됩니다.
            j = max(j, last[c])

            # 현재 인덱스 i가 j와 같아지면, 현재 부분 문자열의 끝에 도달했음을 의미합니다.
            # 이때, 부분 문자열의 길이를 계산하여 ans에 추가하고, anchor를 업데이트하여 다음 부분 문자열의 시작 인덱스로 설정합니다.
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans
```
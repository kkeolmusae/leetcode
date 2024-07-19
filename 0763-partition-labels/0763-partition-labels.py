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